dev:
	PYTHONDONTWRITEBYTECODE=1 python main.py

format:
	black . -l 80
	isort .
	mypy .
	flake8 .
