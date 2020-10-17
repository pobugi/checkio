IMAGE_NAME = checkio_es
VERSION = 1.0

build:
	docker build -t $(IMAGE_NAME):$(VERSION) .
run:
	docker run -p 8000:5000 --name image --rm $(IMAGE_NAME):$(VERSION)

lint:
	docker run --rm -v $(PWD):/code eeacms/pylint
