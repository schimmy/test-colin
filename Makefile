make:
	virtualenv -p python3 solargrade/colin-test-env
	source ./colin-test-env/bin/activate
	pip install -r requirements.txt
	cd angular-frontend && npm install

run:
	python ./solargrade/manage.py runserver &
	cd angular-frontend && ng serve --open
