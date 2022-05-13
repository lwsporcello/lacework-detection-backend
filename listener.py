# a simple flask api in python
# requires pip3 install flask
# change the IP and port as necessary on last line

from flask import Flask, json, request, send_file, abort
#import logging
#import os

#define flask api
api = Flask(__name__)

#define endpoints
@api.route('/', methods=['POST'], defaults={'path': ''})
@api.route('/<path:path>', methods=['POST'])
def post_data(path):
  data_json = request.json
  url = request.url
  print("---")
  print(url)
  print(data_json)
  return json.dumps({"success":True}), 200

if __name__ == '__main__':
    api.run(host="0.0.0.0", port=8080)
