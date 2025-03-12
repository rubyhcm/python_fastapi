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
3. Create 'app/schemas.py'

#### Check packages

`pip freeze`

#### Validate email

`pip install email-validator`

#### Encrypt password

`pip install 'passlib[bcrypt]'`

`pip install --upgrade bcrypt`

`pip uninstall bcrypt`

`pip install bcrypt==4.0.1`

#### JWT

`pip install 'python-jose[cryptography]'`

#### ENV file

`pip install python-dotenv`

#### Using

`user.__dict__ == user.first`

#### Migration

`pip install alembic`

`alembic init alembic` to init

`alembic revision -m 'create notes table'` to create migration

`alembic upgrade head` or `alembic upgrade 3f2cb1cd21cd`to run migration

`alembic downgrade -1` or `alembic downgrade 3f2cb1cd21cd` to downgrade

`alembic current` to check status

#### Requirement

`pip freeze > requirements.txt`

`pip install -r requirements.txt` to install
