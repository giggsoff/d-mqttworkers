import ssl
import sys
import time
import paho.mqtt.client
import paho.mqtt.publish
from flask import Flask
import thread
import json

level = 0.
timer = 3.
maxval = 100.
temp = 20.
id = 12345

app = Flask(__name__)

@app.route('/level/<new_level>')
def setlevel(new_level):
	global level
	oldlevel = str(level)
	level = new_level
	return "Old level: "+oldlevel+"\n"

def on_connect(client, userdata, flags, rc):
	print('connected')

def main():
	i = 1
	while True:
		data = {'i':id,'l':level,'m':maxval,'t':temp,'d':int(round(time.time()))}
		paho.mqtt.publish.single(
			topic='topic1',
			payload=json.dumps(data),
			qos=2,
			hostname='127.0.0.1',
			port=1884,
			client_id='client2',
			#auth={
			#	'username': '[username]',
			#	'password': '[password]'
			#},
			#tls={
			#	'ca_certs': '/etc/ssl/certs/DST_Root_CA_X3.pem',
			#	'tls_version': ssl.PROTOCOL_TLSv1_2
			#}
		)
		time.sleep(timer)
		i=i+1

def flaskThread():
	app.run(debug=True, use_reloader=False)

if __name__ == '__main__':
	thread.start_new_thread(flaskThread,())
	main()
	sys.exit(0)
