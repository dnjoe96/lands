# MSSQL integration Application
A Flask Application to connect with an existing SQL server application query data.

## To clone repo
`git clone https://github.com/dnjoe96/lands.git`

## To run on your local machine
- create virtual environment
- create a .env file and provide the database URI
`DATABASE_URL="mssql+pyodbc://username:password@host:port/database?driver=your driver"`

- `pip3 install flask`
- `pip install -r requirements.txt`
- `export FLASK_APP=run.py`
- `flask run` 

## Prerequisites
- Python3
- ODBC

for further enquiries or suggestions, mail `donjoedbest@gmail.com` 