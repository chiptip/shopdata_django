# shopdata_django

a django project to test drive amazon associates api

to start:

1. install dependencies
		pip install -r config/requirements.pip
1. create settings_local.py with the following specifications
	* Amazon client ID, ```CLIENT_ID```
	* Amazon client secret, ```CLIENT_SECRET```
	* enable https rundev server ```DEBUG_APPS = ("sslserver",)```
1. start https test server
		python manage.py runsslserver 0.0.0.0:1337
1. setup local host reference to test dns in ```/etc/hosts```
		127.0.0.1	test.shopdata.io
1. sign up Amazon API and register url ```https://test.shopdata.io:1337```
1. in browser, to visit ```https://test.shopdata.io:1337```
