"""Uses cloudinary to host local image and return image url.

Not currently used, since uploads.im works well enough
"""

import cloudinary
from cloudinary.utils import cloudinary_url
from cloudinary.uploader import upload
import configparser

config = configparser.ConfigParser()
config.read("cloudinary_auth.ini")
cloud_name = str(config.get("credentials", "cloud_name"))
api_key = str(config.get("credentials", "api_key"))
api_secret = str(config.get("credentials", "api_secret"))

cloudinary.config(
	cloud_name = cloud_name,
	api_key = api_key,
	api_secret = api_secret
)

def upload_image(path, name):
	"""Returns new image url given path to local image."""
	result = upload(path, public_id = name)
	return result["secure_url"]

if __name__ == "__main__":
	print upload_image("test.jpg", "dog")