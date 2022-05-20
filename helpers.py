"""
helpers.py
~~~~~~~~~~
This module contains all helper functions that are needed for the Flask app
"""
import os
import secrets

def save_image(form_file):
    """Attempts to save an uploaded image"""
