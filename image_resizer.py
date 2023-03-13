from PIL import Image

def resize_image(filename, scale):
    with Image.open(filename) as img:
        width, height = img.size
        new_size = (int(width * scale), int(height * scale))
        resized_img = img.resize(new_size)
        resized_img.save(f"resized_{filename}")
