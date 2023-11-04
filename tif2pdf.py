import os
import tempfile
import argparse
from PIL import Image
from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen import canvas

def create_pdf(input_directory, output_pdf):
    # Get the cover page and possible other color pages
    image_files = [j for j in os.listdir(input_directory) if j.lower().endswith('.jpg')]

    # Get a list of all TIF files in the directory
    image_files += [f for f in os.listdir(input_directory) if f.lower().endswith('.tif')]

    # Sort the files (optional)
    image_files.sort()

    # Create a PDF file
    c = canvas.Canvas(output_pdf)

    # Iterate through the TIF files and add them to the PDF at their original size
    for image_file in image_files:
        image_path = os.path.join(input_directory, image_file)

        # Open the TIF image using Pillow (PIL)
        img = Image.open(image_path)

        # Convert to monochrome if not already (1-bit image)
        #if img.mode != '1':
        #    img = img.convert('1')

        # Get the original image dimensions
        width, height = img.size

        # Set the PDF page size to match the image dimensions
        c.setPageSize(portrait((width, height)))

        # Save the image as a temporary file
        temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
        img.save(temp_file.name, 'PNG')

        # Add the temporary image file to the PDF
        c.drawImage(temp_file.name, 0, 0, width=width, height=height)
        c.showPage()

        # Close and remove the temporary file
        temp_file.close()
        os.remove(temp_file.name)

    # Save the PDF file
    c.save()

    print(f'PDF created: {output_pdf}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert JPG and monochrome TIF images to a PDF.')
    parser.add_argument('input_directory', help='Directory containing JPG and/or monochrome TIF images')
    parser.add_argument('output_pdf', help='Output PDF file name')
    args = parser.parse_args()

    create_pdf(args.input_directory, args.output_pdf)
