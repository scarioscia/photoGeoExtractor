# -*- coding: utf-8 -*-

"""Command line interface for photoGeoExtractor."""

import click
import pandas as pd
from .utils import process_files, convert_deg_min_sec_to_decimal_coords, get_flash_data

@click.group(help='photoGeoExtractor')
def main():
    """Run photoGeoExtractor."""

@main.command()
@click.option('--input', help='Zip file or directory containing photos to scan', type=str)
@click.option('--output', help='Output filename for photo metadata', type=str)
@click.option('-v', '--verbose', help='Log everything', is_flag=True)
@click.option('--all', help='Include all columns in the output CSV file', is_flag=True)
@click.option('--custom', help='List of column names separated by commas for custom CSV output', type=str)

def extract_metadata(input, output, verbose, all, custom):
    """Get metadata from Google Takeout photos."""
    result = process_files(input)

    if result:
        df = pd.DataFrame(result)

        # Convert coordinates to decimal format
        df["gps_longitude_dec"] = df.apply(lambda x: convert_deg_min_sec_to_decimal_coords(x.gps_longitude, x.gps_longitude_ref), axis=1)
        df["gps_latitude_dec"] = df.apply(lambda x: convert_deg_min_sec_to_decimal_coords(x.gps_latitude, x.gps_latitude_ref), axis=1)

        # Convert datetime columns to datetime objects
        df.datetime_original = pd.to_datetime(df.datetime_original, format='%Y:%m:%d %H:%M:%S', errors="coerce")
        df.datetime = pd.to_datetime(df.datetime, format='%Y:%m:%d %H:%M:%S')
        df.datetime_digitized = pd.to_datetime(df.datetime_digitized, format='%Y:%m:%d %H:%M:%S')

        # Extract flash data
        df["flash_fired"] = df.apply(lambda x: get_flash_data(x.flash), axis=1)
        df.gps_altitude = pd.to_numeric(df.gps_altitude)

        # Select columns based on flags
        if custom:
            custom_columns = custom.split(',')
            df = df[custom_columns]
        elif all:
            pass  # Do not filter columns
        else:
            default_columns = ['filename', 'datetime', 'gps_latitude_ref', 'gps_latitude', 'gps_longitude_ref', 'gps_longitude', 'gps_altitude_ref', 'gps_altitude', 'gps_longitude_dec', 'gps_latitude_dec']
            df = df[default_columns]


        # Save DataFrame to CSV
        df.to_csv(output, index=False)
        print(f"Data has been saved to {output}")
    else:
        print("No images found in the provided directory or ZIP file.")

if __name__ == '__main__':
    main()
