from PIL import Image
import os

# Set the input and output folder paths
input_folder = "/***your path***"
output_folder = "***Your path***/resized"
new_size = (800, 600)  # Set the desired width and height

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith((".jpg", ".jpeg", ".png", ".gif")):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Open the image
        image = Image.open(input_path)

        # Resize the image
        image = image.resize(new_size, Image.ANTIALIAS)

        # Save the resized image to the output folder
        image.save(output_path)

        print(f"Resized {filename} and saved to {output_path}")

print("All images resized and saved.")
