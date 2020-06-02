 ## Description

This is a simple web clone of the instagram website. A user can create an account and sign into it. A user can then upload images, and follow other users. A user can view photos uploaded by other users in the home page of app.
 # BEHAVIOUR DRIVEN DEVELOPMENT(BDD)
Behaviour 	Input 	Output
-Navigate to website 
-Click on a profile &User profile is displayed
 -Adding Comments: 
 	.Comments for that photo is displayed
  .Click on add a comment link and type your comment 
-Navigate to search input 	Type in a user profile e.g Salem 	That searched profile is displayed

 ## Set Up and Installations
 # Prerequisites

    Ubuntu Software
    Python3.6
    Postgres
    python virtualenv

 # Clone the Repo

Run the following command on the terminal: git clone https://github.com/saa-lem/Instagram.git Clone.git && cd Instagram
Activate virtual environment

Activate virtual environment using python3.6 as default handler

virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate

 # Install dependancies

Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt
Create the Database

psql
CREATE DATABASE instagram;

 # .env file

Create .env file and paste paste the following filling where appropriate:

SECRET_KEY = '<Secret_key>'
DBNAME = 'instaclone'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True



 # Run initial Migration

python3.6 manage.py makemigrations app
python3.6 manage.py migrate

 # Run the app

python3.6 manage.py runserver

Open terminal on localhost:8000
 # Known bugs

Like and Follow functionality do not work
 # Technologies used

- Python 3.6
- HTML
- Bootstrap 4
- Heroku
- Postgresql

 # Further help

Contact me at salemowino18@gmail.com if you run into any issue or have any questions
License

Copyright (c) 2020 Saa-lem


