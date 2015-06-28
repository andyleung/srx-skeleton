__author__ = 'aleung@juniper.net'


#
# Copyright (c) 2008 - 2015 
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#

from flask import Flask, render_template, request, redirect, url_for, jsonify
from jnpr.junos import Device
from jnpr.junos.exception import ConnectAuthError, ConnectTimeoutError, ConnectError 
from lxml import etree
import json

app = Flask(__name__)
device = {}

# route for handling the SRX login 
@app.route('/', methods=['GET','POST'])
@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
    	hostname = request.form['hostname'] 
        username = request.form['username'] 
        password = request.form['password']
        #
        # Retrieve device information
        #
        dev = Device(hostname,user=username,password=password)

        try:
            dev.open()

        except ConnectAuthError:
            error = 'Wrong Credentials. Please try again.'
            return render_template('login.html',error=error)

        except ConnectTimeoutError:
            error = 'Timeout. Host not reachable?'
            return render_template('login.html',error=error)

        except ConnectError:
            error = 'Huh... something wrong. Try again?'
            return render_template('login.html',error=error)

        print "Login success"
        #  Print device info
        global device
        device = dev.facts
        print "Device Name: ", device['hostname']
        print device
        dev.close()
        return redirect(url_for('get_device'))
    return render_template('login.html', error=error)

@app.route('/device_info')
def get_device():
    data = device
    return render_template('device.html', data=data)

app.secret_key = "juniper"

if __name__ == '__main__':
	app.run( host='0.0.0.0', port=5000, debug=True)



