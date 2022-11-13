import os
import pydevd_pycharm
from flask import Flask, request

app = Flask(__name__)

def get_method():
    return "get method call was successfull!"

def post_method():
    return "post method call was successfull!"

@app.route('/details', methods=['GET', 'POST'])
def details():
    if request.method == 'GET':
        content = request.json
        query_param = request.args
        print(content)
        print("-----------------------")
        print("-----------------------")
        print(query_param.get("name"))
        return get_method()
    if request.method == 'POST':
        content = request.json
        query_param = request.args
        print(content)
        print("-----------------------")
        print(content["delimeter"])
        print("-----------------------")
        print(query_param.get("name"))
        return post_method()

def attach():
  if os.environ.get('WERKZEUG_RUN_MAIN'):
    print('Connecting to debugger...')
    pydevd_pycharm.settrace('0.0.0.0', port=9000, stdoutToServer=True, stderrToServer=True)

if __name__ == '__main__':
  print('Starting hello-world server...')
  # comment out to use Pycharm's remote debugger
  # attach()

  app.run(host='0.0.0.0', port=8080)
