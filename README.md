# photoGeoExtractor

The `photoGeoExtractor` package extracts geolocation metadata from JPEG photos, exporting it to a spreadsheet/csv file, building on [this](https://max-coding.medium.com/download-all-your-google-photos-and-extract-exif-metadata-into-a-csv-file-using-python-and-pandas-4a65de8392ab) code. 

To use, start by uploading your photos to Google Photos and then downloading them via Google Takeout. This is a quick process with a handy [tutorial](https://kb.uconn.edu/space/IKB/26398359570/Use+Google+Takeout+to+Export+Google+Photos). `photoGeoExtractor` takes as input either the resulting `.zip` file or an entire directory of images if unzipped. 


## Installation 
Until this package is on `PyPI`, users can install it manually: 

1. Create a virtual environment

        python -m venv yourenvname

2. Activate your virtual environment (here called `yourenvname`)

        source yourenvname/bin/activate # Mac

        .\yourenvname\Scripts\activate # Windows

3. Navigate to where you'd like to download this repository, and then get it from GitHub

        git clone https://github.com/scarioscia/photoGeoExtractor.git

4. Navigate into the newly created directory 

        cd ./photoGeoExtractor/

5. Install the program 

        pip install .


## Usage
The `photoGeoExtractor` program uses the `extract-metadata` command to take GPS information from photos downloaded via Google Takeout and export it to a table. It takes as input either a directory or a compressed (`.zip`) file containing the photos. The user defines a filename for metadata output. 

Replace `/path/to/album` with your input (directory or `.zip` file) and `/path/to/outfile.csv` with your desired output filename and location: 

`python3 -m photoGeoExtractor extract-metadata --input=/path/to/album --output=/path/to/outfile.csv`


## Improvements pending 
- Set default output filename for `--outfile`
- Create option to export only GPS-specific metadata  

