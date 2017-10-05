source .venv/bin/activate

pip install -r requirements.txt
pip freeze > requirements.txt

gunicorn --reload rest_api_sample.app