from flask import Flask, url_for, redirect, request, render_template

import os
import pathlib
import random
from pprint import pprint

project_limitations = []
project_themes = []
# Read in project limitations
with open(os.path.join(pathlib.Path(os.getcwd()).absolute(), 'art_jam_files', 'limits.txt')) as f:
    for line in f.readlines():
        project_limitations.append(line.strip('\n'))

# Read in project themes
with open(os.path.join(pathlib.Path(os.getcwd()).absolute(), 'art_jam_files', 'themes.txt')) as f:
    for line in f.readlines():
        project_themes.append(line.strip('\n'))

# Flask App
app = Flask(__name__)
# Upload Setup
UPLOAD_FOLDER = os.path.join(pathlib.Path(os.getcwd()).absolute(), 'uploads')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# App Route Functions #
#######################################################################################
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    theme = project_themes[random.randint(0, len(project_themes)-1)]
    style = project_limitations[random.randint(0, len(project_limitations)-1)]
    return render_template('index.html', style=style, theme=theme)

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/current', methods=['GET', 'POST'])
def current():
    return render_template('current.html')

@app.route('/previous', methods=['GET', 'POST'])
def previous():
    return render_template('previous.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        pass
        # f = request.files['file']
        # f.save(sec)
    return render_template('upload_form.html')




# App Error Route Functions #
#######################################################################################
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500







if __name__ == '__main__':
    app.run()
