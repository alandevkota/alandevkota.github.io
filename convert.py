from PIL import Image

# Open the JPG image
image = Image.open("./assets/img/headshot.jpg")

# Convert the image to PNG format
image.save("./assets/img/headshot.png")

# Print a success message
print("Image successfully converted!")