import os
import time
import logging
from PIL import Image
from alive_progress import alive_bar

def is_image(extension: str) -> bool:
    """Check if the extension belongs to an image."""
    return extension.lower() in ['.jpg', '.png', '.jpeg', '.webp', '.bmp', '.gif', '.ico', '.raw', '.tif', '.tiff']

def compress_images_in_folder(folder_path: str):
    """Finds all images in the specified folder and compresses them."""
    # Count images first
    images = []
    for filename in os.listdir(folder_path):
        _, extension = os.path.splitext(filename)
        if is_image(extension):
            images.append(filename)
            
    if not images:
        print("No images found to compress.")
        return

    print("Compressing images...")
    with alive_bar(len(images)) as bar:
        for filename in images:
            filepath = os.path.join(folder_path, filename)
            try:
                picture = Image.open(filepath)
                # Keep original format or convert to JPEG if necessary, but saving back to original path
                picture.save(filepath, optimize=True, quality=60)
            except Exception as e:
                logging.error(f"Failed to compress {filename}: {e}")
            
            time.sleep(0.1)
            bar()
