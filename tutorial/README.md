## Tutorial 

I've uploaded a `.zip` file that includes three photos downloaded via Google Takeout. To test the program, you can `cd` into this directory and execute: 

		python3 -m photoGeoExtractor extract-metadata --input=./photoGeoExtractor_sample_imgs.zip --output=./photoGeoExtractor_sample_imgs_create.csv

An example of the output generated with this default command is also in this directory at `example_photoGeoExtractor_sample_imgs.csv`. 

### Flags

You can also output all columns using the optional `--all` flag or try the `--custom` flag followed by comma-separated column names: 
		`python3 -m photoGeoExtractor extract-metadata --input=./photoGeoExtractor_sample_imgs.zip --output=./all_photoGeoExtractor_sample_imgs_all.csv --all`

		`python3 -m photoGeoExtractor extract-metadata --input=./photoGeoExtractor_sample_imgs.zip --output=./all_photoGeoExtractor_sample_imgs_custom.csv --custom offset_time,offset_time_original,offset_time_digitized,shutter_speed_value`
