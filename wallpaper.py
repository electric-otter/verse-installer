import os
import ctypes

def set_wallpaper(image_path):
    """
    Sets the desktop wallpaper to the image at the given path.

    Args:
        image_path: The path to the image file.
    """
    try:
        SPI_SETDESKWALLPAPER = 20
        if os.name == 'nt':
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
        elif os.name == 'posix':
            os.system(f"gsettings set org.gnome.desktop.background picture-uri file://{image_path}")
        else:
            print("Operating system not supported.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    image_path = "wallpaper.png"
    set_wallpaper(image_path)
