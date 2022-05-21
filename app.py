from flask import Flask, url_for, redirect, request, render_template, flash
from flask_bootstrap import Bootstrap
import os
import secrets
import pathlib
import random
from pprint import pprint
from PIL import Image
from werkzeug.utils import secure_filename
from forms import LoginForm, RegisterForm, UploadForm




project_limitations = []
project_themes = []
os.chdir('/Users/williammurphy/Desktop/art_jam_git')
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

print(f'APP ROOT: {app.root_path}')

# Upload Setup
UPLOAD_FOLDER = os.path.join(pathlib.Path(os.getcwd()).absolute(), 'pictures')
print(f'UPLOAD FOLDER: {UPLOAD_FOLDER}')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
# images = UploadSet('images', IMAGES)
# configure_uploads(app, images)

# Flask app configuration
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'secret'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LfMEAYgAAAAAHOnAz8LoPdGRCFPMcBaARlhsFc1'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LfMEAYgAAAAAMlG8kQB87XN9g0eAyDIRjlG5mYF'
app.config['TESTING'] = True

#


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

def save_image(from_file):
    """Attempts to save an uploaded image

    """
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(from_file.filename)
    print(f'random_hex {random_hex}')
    print(f'file ext: {f_ext}')
    picture_fn = random_hex + f_ext
    picture_path = os.path.join('/Users/williammurphy/Desktop/art_jam_git/pictures', picture_fn)
    output_size = (125, 125)
    i = Image.open(from_file)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    global current_file
    current_file = ''
    if form.validate_on_submit():
        if form.file.data:
            filename = secure_filename(form.file.data.filename)
            current_file = filename
            form.file.data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(f"File: {os.path.join(UPLOAD_FOLDER, filename)}")
            return render_template('upload.html', form=form, filename=filename)
    else:
        current_file = None
        # return redirect('profile')
    return render_template('upload.html', form=form, current_file=current_file)


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
