# coding: utf8

from flask import render_template, Flask, request
import json, os

app = Flask(__name__)


@app.route('/')
def index():
    dirs = ['/tmp', '/etc', '/opt']
    return render_template('index.html', dirs=dirs)


@app.route('/log/')
def log():
    filename = request.args.get('file', '')
    with open(filename) as f:
        content = f.read()
    return render_template('log_frame.html', log_path=filename, log_content=content)


@app.route('/get_json/')
def get_json():
    dir_path = request.args.get('dir', '/tmp')
    a = []
    b = 1
    for i in os.listdir(dir_path):
        file_path = os.path.join(dir_path, i)
        if os.path.isdir(file_path):
            a.append({'id': b, 'name': i, 'file': file_path, 'isParent': True})
        else:
            a.append({'id': b, 'name': i, 'file': file_path, 'isParent': False})

    return json.dumps(a, indent=4)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

