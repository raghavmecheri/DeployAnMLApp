install:
	python3 -m pip install --upgrade pip
	pip install -r requirements.txt

freeze: FORCE
	pip freeze > requirements.txt

dev:
	uvicorn main:app --port 5000 --reload

FORCE: 
