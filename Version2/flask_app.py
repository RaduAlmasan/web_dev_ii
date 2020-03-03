import os

from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/api/images_list/<int:number>')
def images_list(number):
    image_files = os.listdir("static/images")
    print(image_files)
    return send_from_directory("api", "images.json")

@app.route('/static/<path:path>', methods=['GET'])
def static_file(path):
    return send_from_directory("static", path)