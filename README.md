# Dog Breed Classifier Telegram Bot
Telegram bot to help you classify/know what dog breed from uploaded image/photo, and help you to give more information about the dog breed.
The dog breed classification method is using API from this [repositry](https://github.com/divawidia/dog-breed-classification-api). 
For more detailed app description and deep learning model used for chatbot, can be seen [here](https://github.com/divawidia/Dog-Breed-Classification-Telegram-Bot)
You can try this bot by cliking this [link](https://t.me/deteksi_hewan_bot)

- Screenshot

	<a href="https://ibb.co.com/P5RQNB6"><img src="https://i.ibb.co.com/FB9VKGD/Screenshot-2024-07-01-11-46-49-402-org-telegram-messenger.jpg" alt="Screenshot-2024-07-01-11-46-49-402-org-telegram-messenger" border="0" height="600"></a>
	<a href="https://ibb.co.com/X2q7jHc"><img src="https://i.ibb.co.com/6nkHrQj/Screenshot-2024-07-01-11-47-17-477-org-telegram-messenger.jpg" alt="Screenshot-2024-07-01-11-47-17-477-org-telegram-messenger" border="0" height="600"></a>
	<a href="https://ibb.co.com/wLTK78f"><img src="https://i.ibb.co.com/H20rCRj/Screenshot-2024-07-01-11-48-00-003-org-telegram-messenger.jpg" alt="Screenshot-2024-07-01-11-48-00-003-org-telegram-messenger" border="0" height="600"></a>
	<a href="https://ibb.co.com/jhJqmmY"><img src="https://i.ibb.co.com/CBP4ggy/Screenshot-2024-07-01-11-48-05-545-org-telegram-messenger.jpg" alt="Screenshot-2024-07-01-11-48-05-545-org-telegram-messenger" border="0" height="600"></a>
	<a href="https://ibb.co.com/tMwcnBr"><img src="https://i.ibb.co.com/HDLYR78/Screenshot-2024-07-01-11-49-51-602-org-telegram-messenger.jpg" alt="Screenshot-2024-07-01-11-49-51-602-org-telegram-messenger" border="0" height="600"></a>
## Techstack

<p align="center">
    <a href="https://www.python.org/"><img alt="Python v3.10.x" src="https://img.shields.io/badge/Python-v3.10.x-c2c330?style=for-the-badge&logo=python"></a>
    <a href="https://core.telegram.org/api"><img alt="Telegram Bot API" src="https://img.shields.io/badge/Telegram Bot Api-v7.4-24A2E0?style=for-the-badge&logo=telegram"></a>
    <a href="https://docs.python-telegram-bot.org/en/stable/index.html"><img alt="python-telegram-bot v21.3" src="https://img.shields.io/badge/python telegram bot-v21.3-24A2E0?style=for-the-badge&logo=telegram"></a>
</p>

## Features
* Classify dog breed by uploading image
* Retrieve dog breed detail data based on dog breed name

## Installation
1. First, head over to [BotFather](https://t.me/BotFather) and create your own telegram bot with the `/newbot` command. After choosing an appropriate name and telegram handle for your bot, note down the **bot token** provided to you.
2. Clone this repository:

	```
	$ git clone https://github.com/divawidia/dog-breed-classification-api.git
	```
3. Virtual Environment Setup:
    It is preferred to create a virtual environment per project, rather then installing all dependencies of each of your 
    projects system wide. Once you install [virtual env](https://virtualenv.pypa.io/en/stable/installation/), and move to 
    your projects directory through your terminal, you can set up a virtual env with:

    ```bash
    python3 -m venv .venv
    ```
4. Activate the Virtual Environment
    * In Linux:

    ```bash
    . venv/bin/activate
    ```

    * In Windows:

    ```bash
    venv/Scripts/activate
    ```
5. Install the Required Packages:

    ```bash
    pip3 install -r requirements.txt
    ```
6. Copy the .env.example file and Rename to .env
    After copy and rename the file to .env, fill the TELEGRAM_BOT_TOKEN variable with your bot token:
    * TELEGRAM_BOT_TOKEN = 
    
6. Running the Application

    Once you have setup your bot token, you are ready to run the bot.
    You can go ahead and run the application with a simple command:

    ```bash
    python3 tele_bot.py
    ```

## Deployment
If you want to deploy this bot, you can follow this [tutorial](https://tjtanjin.medium.com/how-to-host-a-telegram-bot-on-ubuntu-a-step-by-step-guide-a38fb8c04f72)
