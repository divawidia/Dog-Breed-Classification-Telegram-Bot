# Dog Breed Classifier Telegram Bot
Telegram bot to help you classify/know what dog breed from uploaded image/photo, and help you to give more information about the dog breed.
This backend app (include deployment of deep learning model) was created using Flask framework.
For more detailed app description and deep learning model used for chatbot, can be seen [here](https://github.com/divawidia/Dog-Breed-Classification-Telegram-Bot)

## Techstack

<p align="center">
    <a href="https://www.python.org/"><img alt="Python v3.10.x" src="https://img.shields.io/badge/Python-v3.10.x-c2c330?style=for-the-badge&logo=python"></a>
    <a href="https://flask.palletsprojects.com/en/3.0.x/"><img alt="Flask v3.0.x" src="https://img.shields.io/badge/Flask-v3.0.x-7CC8D2?style=for-the-badge&logo=flask"></a>
    <a href="https://www.mongodb.com/"><img alt="MongoDB v7.0.11" src="https://img.shields.io/badge/MongoDB-v7.0.11-00684A?style=for-the-badge&logo=mongodb"></a>
    <a href="https://gunicorn.org/"><img alt="Gunicorn 22.0" src="https://img.shields.io/badge/Gunicorn-v22.0-469745?style=for-the-badge&logo=gunicorn"></a>
    <br/>
    <a href="https://www.tensorflow.org/"><img alt="Tensorflow 2.16.0" src="https://img.shields.io/badge/Tensorflow-v2.16.0-FF8500?style=for-the-badge&logo=tensorflow"></a>
    <br/>
    <a href="https://cloud.google.com/?hl=en">
        <img src="https://img.shields.io/badge/Google Cloud Platform-FFFFFF?style=for-the-badge&logo=googlecloud" alt="Google Cloud Platform">
    </a>
    <a href="https://cloud.google.com/run/?hl=en">
        <img src="https://img.shields.io/badge/Cloud Run-FFFFFF?style=for-the-badge&logo=googlecloud" alt="Cloud Run">
    </a>
    <a href="https://cloud.google.com/artifact-registry/">
        <img src="https://img.shields.io/badge/Artifact Registry-FFFFFF?style=for-the-badge&logo=googlecloud" alt="Artifact Registry">
    </a>
    <a href="https://cloud.google.com/build?hl=en">
        <img src="https://img.shields.io/badge/Cloud Build-FFFFFF?style=for-the-badge&logo=googlecloud" alt="Cloud Build">
    </a>
    <a href="https://hub.docker.com/r/eloufirhatim/helper/tags" title="Docker image">
        <img src="https://img.shields.io/docker/v/eloufirhatim/helper?label=Docker&logo=docker&style=for-the-badge" alt="Docker image">
    </a>
    <br/>
    <a href="https://swagger.io/">
        <img src="https://img.shields.io/badge/Swagger-v3.1.0-85EA2D?style=for-the-badge&logo=swagger" alt="Swagger">
    </a>
    <a href="https://www.postman.com/">
        <img src="https://img.shields.io/badge/Postman-v11.2.0-FF6C37?style=for-the-badge&logo=postman" alt="Postman">
    </a>
</p>

## Features
* Classify dog breed by uploading image
* Using CNN with Resnet50 transfer learning trained on dog breed dataset to classify dog breed
* Retrieve dog breed detail data based on dog breed name

## Installation
1. Clone this repository:

	```
	$ git clone https://github.com/divawidia/dog-breed-classification-api.git
	```
2. Virtual Environment Setup:
    It is preferred to create a virtual environment per project, rather then installing all dependencies of each of your 
    projects system wide. Once you install [virtual env](https://virtualenv.pypa.io/en/stable/installation/), and move to 
    your projects directory through your terminal, you can set up a virtual env with:

    ```bash
    python3 -m venv .venv
    ```
3. Activate the Virtual Environment
    * In Linux:

    ```bash
    . venv/bin/activate
    ```

    * In Windows:

    ```bash
    venv/Scripts/activate
    ```
3. Install the Required Packages:

    ```bash
    pip3 install -r requirements.txt
    ```
4. Copy the .env.example file and Rename to .env
    After copy and rename the file to .env, fill the required environment variables such as:
    * DB_HOST = 
    * DB_CLUSTER = 
    * DB_USERNAME = 
    * DB_PASSWORD = 
5. Set Up the Database
    First you need to create the cluster manually in your mongodb atlas/localhost.
    Match the cluster name that has been created in the DB_DATABASE variable in .env file with the database created on the mongodb atlas/localhost.
    
    To setup a MongoDB migration, you need to run:
    ```bash
    python database/migrate.py
    ```
6. Running the Application

    Once you have setup your database, you are ready to run the application.
    You can go ahead and run the application with a simple command:

    ```bash
    flask run
    ```
7. Go to the swagger api documentation
    Once you have run your flask app , you can go to the swagger api documentation by enter this url:

    ```bash
    http://127.0.0.1:5000/api/v1/docs
    ```

## Deployment
If you want to deploy this application to GCP Environment, you can follow this [tutorial](https://youtu.be/LRJX8hvQ6oQ?si=ED0mv_e--rZNxlsn)

## API Documentation
The API documentation of the Teman Ngorte Chatbot application can be seen in the following Swagger API documentation, you can try out the API by clicking the button bellow :

[![View in Swagger](https://jessemillar.github.io/view-in-swagger-button/button.svg)](https://dog-breed-classifier-api-7zz24sawna-et.a.run.app/api/v1/docs/)