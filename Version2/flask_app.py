import os

from flask import Flask, send_from_directory
app = Flask(__name__)

app.route('/api/images_list/<int:number>')
def images_list(number):
    image_files = sorted(os.listdir("static/images"))
    image_files = [ f for f in image_files if ".jpeg" in f ]
    image_entries = [ '"' + f + '":"images/' + f + '"' for f in image_files ]
    image_json = "{" + ",".join(image_entries) + "}"
    return image_json



@app.route('/index.html', methods=['GET'])
@app.route('/', methods=['GET'])
def index_file():
    return send_from_directory("","index.html")

@app.route('/photos', methods=['GET'])
def get_photos():
    return send_from_directory("", "photos.html")

@app.route('/static/<path:path>', methods=['GET'])
def static_file(path):
    return send_from_directory("static", path)