from flask import Flask, url_for, redirect, request, render_template
from flask_bootstrap import Bootstrap
import os
import pathlib
import random
from pprint import pprint
from forms import LoginForm, RegisterForm


project_limitations = []
project_themes = []
os.chdir('/Users/williammurphy/project_git/flask_artjam')
# Read in project limitations
# print(pathlib.Path(os.getcwd()).absolute())
with open(os.path.join(pathlib.Path(os.getcwd()).absolute(), 'art_jam_files', 'limits.txt')) as f:
    for line in f.readlines():
        project_limitations.append(line.strip('\n'))

# Read in project themes
with open(os.path.join(pathlib.Path(os.getcwd()).absolute(), 'art_jam_files', 'themes.txt')) as f:
    for line in f.readlines():
        project_themes.append(line.strip('\n'))

# Flask App
app = Flask(__name__)
Bootstrap(app)

# Upload Setup
UPLOAD_FOLDER = os.path.join(pathlib.Path(os.getcwd()).absolute(), 'uploads')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'secret'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LfMEAYgAAAAAHOnAz8LoPdGRCFPMcBaARlhsFc1'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LfMEAYgAAAAAMlG8kQB87XN9g0eAyDIRjlG5mYF'
app.config['TESTING'] = True



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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('profile')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect('profile')
    return render_template('register.html', form=form)



# App Error Route Functions #
#######################################################################################
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500







if __name__ == '__main__':
    app.run(debug=True)
