"""
helpers.py
~~~~~~~~~~
This module contains all helper functions that are needed for the Flask app
"""
import os
import secrets
import pathlib
from PIL import Image

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"BASE DIR: {base_dir}")

print(f'CURRENT DIR: {os.getcwd()}')
print(f'ROOT: {pathlib.Path(os.getcwd()).root}')



def save_image(from_file):
    """Attempts to save an uploaded image

    """
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(from_file)
    print(f'random_hex {random_hex}')
    print(f'file ext: {f_ext}')
    picture_fn = random_hex + f_ext
    picture_path = os.path.splitext('/Users/williammurphy/Desktop/art_jam_git')




