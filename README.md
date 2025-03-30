# Superheroes Challenge

Superheroes Challenge is a Flask-based API that allows users to manage heroes, their superpowers, and their strengths. The project includes a **SQLite database**, **SQLAlchemy ORM**, and **Flask-Migrate** for database migrations.  

---

## Features  
- Retrieve a list of all heroes  
- Get details of a specific hero, including their powers  
- Retrieve all available superpowers  
- Get details of a specific power  
- Update a power's description using `PATCH`  
- Assign powers to heroes with a strength level 
- Graceful Error Handling:You'll be notified of errors in case the data you are trying to fetch doesn't exist,   or errors in updating or creating new data.

---

## Installation  

### Clone the Repository then navigate to it
```sh
git clone p4-superheroes-challenge
cd p4-superheroes-challenge
```

### Create a Virtual Environment Inside server Subfolder 
```sh
cd server
python -m venv venv
source venv/bin/activate 
```

### Install Dependencies  
```sh
pip install -r requirements.txt
```
### Create a flask app environment variable
```sh
export FLASK_APP=app.py
```

### Set Up the Database  
```sh
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### Seed the Database  
```sh
python seed.py
```

### Run the Application  
```sh
flask run
```
Server will start at `http://127.0.0.1:5000/` 

---

## Usage  
Open POSTMAN to test the APIs functionalities.

### Get All Heroes  
**URL** : `http://127.0.0.1:5000/GET/heroes`

### Get a Specific Hero  
**URL** : `http://127.0.0.1:5000/GET/heroes/<id>`

### Get All Powers  
**URL** : `http://127.0.0.1:5000/GET/powers`

### Get a Specific Power
***URL** : `http://127.0.0.1:5000/GET/powers/<id>`

### Update a Power  
**URL** :`http://127.0.0.1:5000/PATCH/powers/<id>`
**RAW-BODY** :{
            "description": "Valid Updated Description"
}

### Add a Power
**URL** : `http://127.0.0.1:5000/POST/hero_powers`
**RAW-BODY** : {
 "strength": "Average",
 "power_id": 1,
 "hero_id": 3
}