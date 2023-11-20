from PIL import Image
import os

# Define the source folder where the images are located
source_folder = "./input_folder"

# Define the destination folder where the watermarked images will be saved
destination_folder = "./output_folder"

# Define the path to the watermark image
watermark_path = "watermark.png"

# Load the watermark image
watermark = Image.open(watermark_path)

# Define the transparency level (0-255, 0 being completely transparent, 255 being opaque)
watermark_transparency = 80  # Adjust as needed

# Create a directory if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# List all files in the source folder
image_files = os.listdir(source_folder)

# Loop through each image file in the source folder
for image_file in image_files:
    if image_file.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
        # Open the image
        image = Image.open(os.path.join(source_folder, image_file))

        # Check the image mode, and process only RGB images
        if image.mode == 'RGB':
            # Calculate the position to place the watermark in the center
            watermark_position = ((image.width - watermark.width) // 2, (image.height - watermark.height) // 2)

            # Create a watermark with the specified transparency
            watermark_with_transparency = Image.new('RGBA', watermark.size)
            for x in range(watermark.width):
                for y in range(watermark.height):
                    r, g, b, a = watermark.getpixel((x, y))
                    watermark_with_transparency.putpixel((x, y), (r, g, b, watermark_transparency))

            # Paste the watermark with transparency onto the image
            image.paste(watermark_with_transparency, watermark_position, watermark_with_transparency)

            # Save the watermarked image to the destination folder
            watermarked_image_path = os.path.join(destination_folder, image_file)
            image.save(watermarked_image_path)

            print(f"Watermarked and saved: {watermarked_image_path}")
        else:
            print(f"Image already has a watermark or is not in RGB mode: {image_file}")

print("All images processed and watermarked with the specified transparency.")

