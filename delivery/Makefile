install: 
	pip install -e .['dev']

initi_db:
	FLASK_APP=delivery/app.py flask create-db
	FLASK_APP=delivery/app.py flask db upgrade

test:
	pytest tests/ -v --cov=delivery 
