install:
		poetry install

# build:
# 		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --force-reinstall dist/*.whl

lint:
		poetry run flake8 

dev:
		poetry run flask --app page_analyzer:app run

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app


retry:
	poetry install
	poetry build
	poetry publish --dry-run
	python3 -m pip install --force-reinstall dist/*.whl


build:
	./build.sh