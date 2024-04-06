# -*- coding: utf-8 -*-

"""This module contains all the utility functions used in the photoGeoExtractor repo."""

import os 
import zipfile
import re
import io
import exif

# Function to get EXIF data from photo data
def get_exif_data(photo_data):
    try:
        fp = io.BytesIO(photo_data)
        exif_image = exif.Image(fp)
        result = {}
        for field in exif_image.list_all():
            try:
                result[field] = exif_image[field]
            except:
                pass
        return result
    except:
        return {}

# Function to convert degrees, minutes, seconds to decimal coordinates
def convert_deg_min_sec_to_decimal_coords(deg_min_sec, ref):
    try:
        decimal_deg = deg_min_sec[0] + deg_min_sec[1]/60 + deg_min_sec[2]/3600
        decimal_deg = round(decimal_deg, 5)
        if ref == "S" or ref == "W":
            return -decimal_deg
        return decimal_deg
    except:
        return None

# Function to process files in a directory or a ZIP file
def process_files(input_path):
    result = []
    if os.path.isdir(input_path):  # If input is a directory
        files = os.listdir(input_path)
        for filename in files:
            if re.match(".*\.jpg$", filename):
                photo_data = open(os.path.join(input_path, filename), 'rb').read()
                file_data = {"filename": filename}
                file_data.update(get_exif_data(photo_data))
                result.append(file_data)
    elif input_path.endswith(".zip"):  # If input is a ZIP file
        archive = zipfile.ZipFile(input_path, 'r')
        for archived_file in archive.filelist:
            if re.match(".*\.jpg$", archived_file.filename):
                photo_data = archive.read(archived_file.filename)
                file_data = {"filename": archived_file.filename}
                file_data.update(get_exif_data(photo_data))
                result.append(file_data)
    else:
        print("Unsupported input format. Please provide a directory or a .zip file of images.")
    return result

def get_flash_data(flash):
    try:
        return flash.flash_fired
    except:
        return None
