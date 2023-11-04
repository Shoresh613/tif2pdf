from PIL import Image
import os

# Directory where your 8-bit GIF images are located
input_directory = "./"

# Directory where you want to save the 1-bit colormap GIF images
output_directory = "./output_directory"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# List all files in the input directory
input_files = os.listdir(input_directory)

for input_file in input_files:
    # Check if the file is a GIF image
    if input_file.lower().endswith(".gif"):
        input_path = os.path.join(input_directory, input_file)
        output_path = os.path.join(output_directory, input_file+".tif")

        # Open the 8-bit GIF image
        image = Image.open(input_path)

        # Convert the image to 1-bit colormap
        image = image.convert("1", dither=Image.NONE)

        # Save the image as a 1-bit colormap GIF
        image.save(output_path, "TIFF")

        print(f"Converted {input_file} to 1-bit colormap TIFF")

print("Conversion completed.")
