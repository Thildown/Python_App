.PHONY: init run test build clean

init:
	pip install -r requirements.txt

run:
	python app.py

test:
	python -m unittest test.py

build:
	docker build -t health-calculator-service:latest .

clean:
	rm -rf __pycache__
	rm -rf *.pyc