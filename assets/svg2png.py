#!/usr/bin/env python3

import os
import sys
from cairosvg import svg2png


def convert_svg_to_png(input_folder, output_folder, resolutions):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all SVG files in the input folder
    file_list = [
        filename for filename in os.listdir(input_folder) if filename.endswith(".svg")
    ]

    for filename in file_list:
        # Create a folder for each SVG file
        svg_folder = os.path.join(output_folder, os.path.splitext(filename)[0])
        if not os.path.exists(svg_folder):
            os.makedirs(svg_folder)

        # Build the input file path
        input_path = os.path.join(input_folder, filename)

        # Convert SVG to PNG for each resolution
        for resolution in resolutions:
            # Build the output file path
            output_path = os.path.join(svg_folder, f"{resolution}x{resolution}.png")

            # Convert SVG to PNG
            svg2png(
                url=input_path,
                write_to=output_path,
                output_width=resolution,
                output_height=resolution,
            )

            print(f"Converted {filename} to {resolution}x{resolution} PNG.")


if __name__ == "__main__":
    # Set the input and output folder paths
    input_folder = "svgs"
    output_folder = "pngs"

    # Set the desired resolutions for PNG files
    resolutions = [28, 36, 48, 64, 72, 96, 144, 192]

    # Call the function to convert SVG to PNG
    convert_svg_to_png(input_folder, output_folder, resolutions)
