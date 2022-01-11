import tensorflow as tf  
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
  
import numpy as np
from glob import glob 

import logging
import os


# mengambil data daftar nama ras anjing
dog_names = [item[20:-1] for item in sorted(glob("dogImages/train/*/"))]

# mendefinisikan model resnet50
resnet50_model = ResNet50(weights='imagenet')

def path_to_tensor(img_path):
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path, target_size=(224, 224))
    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)

# def paths_to_tensor(img_paths):
#     list_of_tensors = [path_to_tensor(img_path) for img_path in tqdm(img_paths)]
#     return np.vstack(list_of_tensors)

def ResNet50_predict_labels(img_path):
    # returns prediction vector for image located at img_path
    img = preprocess_input(path_to_tensor(img_path))
    return np.argmax(resnet50_model.predict(img))

### returns "True" if a dog is detected in the image stored at img_path
def dog_detector(img_path):
    prediction = ResNet50_predict_labels(img_path)
    return ((prediction <= 268) & (prediction >= 151))

Resnet50_model = tf.keras.models.load_model('saved_models/weights.best.Resnet50.hdf5')

def Resnet50_predict_breed(img_path):
    # extract bottleneck features
    bottleneck_feature = ResNet50(weights='imagenet', include_top=False).predict(preprocess_input(path_to_tensor(img_path)))
    # obtain predicted vector
    predicted_vector = Resnet50_model.predict(bottleneck_feature)
    # return dog breed that is predicted by the model
    return dog_names[np.argmax(predicted_vector)]


telegram_bot_token = "1875996906:AAGqrhz5kHMNOv_JBksWY4GBwkfIMmr4VCA"
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hai :) Kirim foto anjing apa aja nanti aku tebak anjing ras apa itu")

def downloadImage(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Foto sedang diproses ...")
    downloaded_path = "foto"
    file_id = update.message.photo[-1].file_id
    file_unique_id = update.message.photo[-1].file_unique_id

    new_file= context.bot.get_file(file_id)
    saving_path= os.path.join(downloaded_path, "{}.jpg".format(file_unique_id))
    new_file.download(saving_path)

    if dog_detector(saving_path):
        itemsStrings = "Aku tebak ini adalah anjing ras " + str(Resnet50_predict_breed(saving_path))
    else:
        itemsStrings = 'Hmmm sepertinya itu bukan foto anjing deh, coba kirim foto anjing!'

    context.bot.send_message(chat_id=update.effective_chat.id, text=itemsStrings)


downloadImage_handler = MessageHandler(Filters.photo & (~Filters.command), downloadImage)
dispatcher.add_handler(downloadImage_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
