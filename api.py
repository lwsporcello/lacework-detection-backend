# a simple flask api in python
# requires pip3 install flask
# change the IP and port as necessary on last line

from flask import Flask, json, request, send_file, abort
import logging
import os

#define flask api
api = Flask(__name__)

#define constants
BIN_DIR = "/home/ubuntu/se-det-demo/bin"

#set up logging
handler = logging.FileHandler("/var/log/api.log")
log = logging.getLogger('werkzeug')
log.addHandler(handler)
log.setLevel(logging.INFO)

#define endpoints
@api.route('/bin/<path:file>', methods=['GET'])
def download_file(file):
	try:
		return send_file(BIN_DIR+"/"+file, download_name=file), 200
	except:
		abort(404)

@api.route('/lw-beacon', methods=['POST'])
def post_json():
  data_json = request.json
  log.info(data_json)
  return json.dumps({"Success":True}), 200

if __name__ == '__main__':
    api.run(host="0.0.0.0", port=8002)
