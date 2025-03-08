#### Create envirement

python3 -m venv <name>
ex: python3 -m venv venv

#### Run virtual envirement

source venv/bin/activate

#### Insrall fastapi

pip install "fastapi[standard]"

#### Run server

`fastapi dev main.py`

or

`uvicorn main:app`
`uvicorn main:app --reload`

#### API docs

http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc

#### Steps

1. Create app/main.py
2. Create **init**..py
