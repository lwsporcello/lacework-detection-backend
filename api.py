# a simple flask api in python
# requires pip3 install flask
# change the IP and port as necessary on last line

from flask import Flask, json, request

api = Flask(__name__)

my_json = [{"id":1, "name":"my_name"}]

@api.route('/api', methods=['GET'])
def get_json():
  return json.dumps(my_json)

@api.route('/api', methods=['POST'])
def post_json():
  data_json = request.json
  print(data_json)
  return json.dumps({"Success":True}), 200

if __name__ == '__main__':
    api.run(host="0.0.0.0", port=8888)
