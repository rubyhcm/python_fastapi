#### Create envirement

`python3 -m venv <name>`
ex: python3 -m venv venv

#### Run virtual envirement

`source venv/bin/activate`

#### Insrall fastapi

`pip install "fastapi[standard]"`

#### Run server

`fastapi dev app/main.py`

or

`uvicorn main:app`
`uvicorn main:app --reload`

#### API docs

http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc

#### Install Postgres

`pip install psycopg2`

```python
# app/main.py
try:
    conn = psycopg2.connect(
        host="localhost",
        database="fastapi",
        user="postgres",
        password="",
        cursor_factory=RealDictCursor
    )
    cursor = conn.cursor()
    print("Database connection was successful")
except Exception as error:
    print("Connecting to database failed")
    print("Error: ", error)
```

#### Steps

1. Create `app/main.py`
2. Create `__init__.py`

# SQL Alchemy

Using ORM

#### Install SQL Alchemy

`pip install sqlalchemy`

#### Steps

1. Create 'app/database.py'
2. Create 'app/models.py'
