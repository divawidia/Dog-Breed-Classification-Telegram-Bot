import logging
import requests
from telegram import ReplyKeyboardRemove,ReplyKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
import os

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

PREDICT, BREED_ROUTE, END_ROUTE = range(3)
reply_keyboard = [["Iyaa", "Ngga dulu deh"]]

# URL_LOCALHOST = "http://127.0.0.1:5000"
URL_HOSTED = "https://dog-breed-classifier-api-7zz24sawna-et.a.run.app"

def query_predict_breed(filename):
    API_URL = f"{URL_HOSTED}/api/v1/predict"
    with open(filename, 'rb') as file:
        response = requests.post(API_URL, files={'image': file})
    return response.json()

def query_breed_detail(breed):
    API_URL = f"{URL_HOSTED}/api/v1/dogs"
    params = {"breed" : breed,}
    response = requests.get(API_URL, params=params)
    return response.json()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("User : %s start the bot", user.first_name)
    
    await update.message.reply_text(
        "Hai :) Kirim foto anjing apa aja, nanti aku tebak anjing ras apa itu"
    )
    return PREDICT


async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    photo_file = await update.message.photo[-1].get_file()
    file_unique_id = update.message.photo[-1].file_unique_id
    saving_path = f"temp_foto/{file_unique_id}.jpg"
    await photo_file.download_to_drive(saving_path)
    logger.info("Photo of %s: %s", user.first_name, f"{file_unique_id}.jpg")
    
    await update.message.reply_text(
        'Foto sedang diproses... mohon tunggu sebentar... \n*(estimasi proses: 30-60 detik)'
    )
    global api_response
    api_response = query_predict_breed(saving_path)
    os.remove(saving_path)

    if api_response['data']['dog_breed'] == None:
        await update.message.reply_text(
            'Hmmm... sepertinya itu bukan foto anjing deh, coba kirim foto yang berisi anjing lebih jelas lagi!',
        )

        return PREDICT
    else:
        await update.message.reply_text(
            'Aku tebak ini '+ str(api_response['data']['confidence']) + ' anjing ras '+ api_response['data']['dog_breed'] + ', mau tau info lebih detail tentang anjing ' + str(api_response['data']['dog_breed']) + '?',
            reply_markup=ReplyKeyboardMarkup(
                reply_keyboard, one_time_keyboard=False, input_field_placeholder="Iya atau Tidak?"
            ),
        )

        return BREED_ROUTE
    
async def breed_detail(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    breed = api_response['data']['dog_breed']
    logger.info("User : %s want to know the breed detail of %s", user.first_name, breed)
    breed_detail_data = query_breed_detail(breed)

    await update.message.reply_text(
        f"Okee berikut ini merupakan info detail mengenai anjing ras {breed}.\n\n"
        f"{breed_detail_data['data']['description']}\n\n"
        f"Tempramen : {breed_detail_data['data']['demeanor_category']}\n\n"
        f"Peringkat popularitas : {breed_detail_data['data']['popularity']}\n\n"
        f"Group : {breed_detail_data['data']['group']}\n\n"
        f"Tinggi : {round(breed_detail_data['data']['min_height'],1)}-{round(breed_detail_data['data']['max_height'],1)} cm\n\n"
        f"Berat : {round(breed_detail_data['data']['min_weight'],1)}-{round(breed_detail_data['data']['max_weight'],1)} kg\n\n"
        f"Angka Harapan Hidup : {breed_detail_data['data']['min_expectancy']}-{breed_detail_data['data']['max_expectancy']} tahun\n\n"
        f"Kategori Sikap : {breed_detail_data['data']['demeanor_category']}\n\n"
        f"Tingkat Sikap : {int(breed_detail_data['data']['demeanor_value']*10)}/10\n\n"
        f"Frekuensi Perawatan Anjing : {breed_detail_data['data']['grooming_frequency_category']}\n\n"
        f"Tingkat Perawatan Anjing : {int(breed_detail_data['data']['grooming_frequency_value']*10)}/10\n\n"
        f"Kerontokan Anjing : {breed_detail_data['data']['shedding_category']}\n\n"
        f"Tingkat Kerontokan Anjing : {int(breed_detail_data['data']['shedding_value']*10)}/10\n\n"
        f"Keaktifan Anjing : {breed_detail_data['data']['energy_level_category']}\n\n"
        f"Tingkat Keaktifan Anjing : {int(breed_detail_data['data']['energy_level_value']*10)}/10\n\n"
        f"Kemampuan Dilatih : {breed_detail_data['data']['trainability_category']}\n\n"
        f"Tingkat Kemampuan Dilatih : {int(breed_detail_data['data']['trainability_value']*10)}/10\n\n"
        "Mau pengen tau tipe ras anjing dari foto lagi?",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=False, input_field_placeholder="Iya atau Tidak?"
        ),
    )

    return END_ROUTE

async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    await update.message.reply_text(
        "Kirim foto anjing apa aja lagi! nanti aku tebak anjing ras apa itu"
    )

    return PREDICT

async def end_confirmation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        text="Baiklah, mau pengen tau tipe ras anjing dari foto lagi?", 
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Iya atau Tidak?"
        ),
    )

    return END_ROUTE

async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("User %s ended the conversation.", user.first_name)
    await update.message.reply_text(
        "Okee, sampai jumpa kembali!",
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END

telegram_bot_token = str(os.environ.get("TELEGRAM_BOT_TOKEN"))

def main() -> None:
    """Run the bot."""
    application = Application.builder().token(telegram_bot_token).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            PREDICT: [
                MessageHandler(filters.PHOTO, predict)
            ],
            BREED_ROUTE: [
                MessageHandler(filters.Regex("^(Iyaa)$"), breed_detail),
                MessageHandler(filters.Regex("^(Ngga dulu deh)$"), end_confirmation),
            ],
            END_ROUTE: [
                MessageHandler(filters.Regex("^(Iyaa)$"), start_over),
                MessageHandler(filters.Regex("^(Ngga dulu deh)$"), end),
            ]
        },
        fallbacks=[CommandHandler("end", end)],
    )

    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()