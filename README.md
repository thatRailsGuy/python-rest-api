Setup virtualenv:
`virtualenv -p python3 .venv`

Install requirements:
`source .venv/bin/activate`
`pip install -r requirements.txt`
`pip freeze > requirements.txt`



database setup:
`source .venv/bin/activate`
`python rest_api_sample/utils/database.py`




running server:
`source .venv/bin/activate`
`gunicorn --reload rest_api_sample.app`