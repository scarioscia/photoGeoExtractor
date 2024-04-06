# photoGeoExtractor

A Python package to extract GPS metadata from photos via Google Takeout. Builds on code from [here](https://max-coding.medium.com/download-all-your-google-photos-and-extract-exif-metadata-into-a-csv-file-using-python-and-pandas-4a65de8392ab).

## Installation 
Until this package is on `PyPI`, users can install it manually: 

1. Create a virtual environment

`python -m venv yourenvname`

2. Activate your virtual environment 

`source yourenvname/bin/activate` (Mac)

`.\yourenvname\Scripts\activate` (Windows)

3. Navigate to where you'd like this repository to download, and then get it from GitHub

`git clone https://github.com/scarioscia/photoGeoExtractor.git`

4. Navigate into the newly created directory 

`cd ./photoGeoExtractor/`

5. Install the program 

` pip install .`


## Usage
The `photoGeoExtractor` program uses the `extract-metadata` command to take GPS information from photos downloaded via Google Takeout and export it to a table. It takes as input either a directory or a compressed (`.zip`) file containing the photos. The user defines a filename for metadata output. 

Replace `/path/to/album` with your input (directory or `.zip` file) and `outfile.csv` with your desired outfilename: 

`python3 -m photoGeoExtractor extract-metadata --input=/path/to/album --output=outfile.csv`


## Improvements pending 
- Add test photos for example 
- Add frontmatter tutorial for getting photos to Google Takeout 
- Set default output filename for `--outfile`
- Create option to export only GPS-specific metadata 
- Improve `README` description
- Upload to `PyPI`  

