# FastAPI-CRUD-APP
A simple CRUD operation API

## Installation
In order to run the app, it is recommended you first create and activate a virtual environment:
```bash
python -m venv env
# python3 -m venv env if on an older system where python 2.7
# is the default version used when calling "python"

# Activate Virtual Environment
# Windows
env\Scripts\activate

# Unix-based
source env/bin/activate
```
Once the virtual environment is activated simply run `pip install -r requirements.txt`
## MySQL DataBase
In order to use MySQL DataBase for CRUD operations, it is recommended to install XAMPP server to use the MYSQL server on port 3306(Default)

![alt text](https://github.com/sahith0007/FastAPI-CRUD-APP/blob/main/Screenshot%20(60).png?raw=true)

To download XAMPP server click [here](https://www.apachefriends.org/download.html)


## Run the app
There are multiple options available when running the app.
The way you're likely going to want to do it is by running the command
```bash
uvicorn main:app --reload
```

It will run the default port 8000(you can change it if another program is running on it), then you can run
```bash
uvicorn main:app --reload --port <PORT>
```
where the `<PORT>` is a number of your choosing.
For the rest of the options when running a uvicorn app, visit https://www.uvicorn.org/#command-line-options.
