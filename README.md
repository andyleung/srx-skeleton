
# This is a skeleton file for building a webapp for SRX using PyEZ library. 

### Mac: 
----------------
```sh
	$ mongod &
	$ python app.py
```

### Ubuntu: 
------------------
```sh
	$ python app.py
```

## Geo Data Download:
-----------------
There is a file 'GeoLiteCity.dat' you need to download and place under the "static" directory for displaying Geo data.
1. Download GeoLiteCity.dat 
2. http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
3. gunzip GeoLiteCity.dat.gz


## Installation with Vagrant and VirtualBox
-----------------
1. Install vagrant
2. Install virtual box
3. git clone https://github.com/andyleung/session-analyzer

```sh
	# cd session-analyzer
	# python app.py
```

## Manually build all the python libraries
1. Update ubuntu:
-----------------

```sh 

		$ sudo apt-get update
		$ sudo apt-get install python-pip
```

2. Install Mongodb:
-------------------

```sh 

		$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10

		$ echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list

		$ sudo apt-get update
		$ sudo apt-get install -y mongodb-org
``` 

3. Install Python Library:
--------------------------


```sh 
		$ sudo pip install pymongo
		$ sudo pip install flask
		$ sudo apt-get install git
```

4. A. Install Python lxml module:
---------------------------------

```sh
		$ sudo apt-get install libxml2-dev libxslt-dev python-dev
		$ sudo pip install pycrypto
		$ sudo apt-get install zlib1g-dev
		$ sudo pip install lxml 
```

4. B. Build junos-eznc:
-----------------------

```sh
		$ sudo pip install junos-eznc
```

5. Install wkhtmltopdf
----------------------

6. To run:  
------------------
```sh
		 % cd session-analyzer
		 % python app.py
```
