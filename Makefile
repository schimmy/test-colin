make: build test run

build:
	virtualenv -p python3 solargrade/colin-test-env
	cd  solargrade/colin-test-env/bin && source activate && cd -
	pip install -r solargrade/requirements.txt
	cd angular-frontend && npm install

run:
	python ./solargrade/manage.py runserver &
	cd angular-frontend && ng serve --open

test:
	python ./solargrade/manage.py test ./solargrade
	cd angular-frontend && ng test --watch=false
