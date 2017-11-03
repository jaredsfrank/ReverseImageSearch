"""
Runs reverse image search on image, given url.

Requires that MRISA server is running (http://mrisa.mage.me.uk/).

Example: 
    python image_search.py \
    --image_path=fish.jpg

This will return 

"""
import argparse
import ast
import google_search
import pycurl
import json
import requests


parser = argparse.ArgumentParser()
parser.add_argument("--image_path", 
    help="Path to image query",
    type=str)
args = parser.parse_args()


def predict_from_path(path):
    """Returns google reverse image search prediction given image path."""
    url = upload_image(path)
    return predict_from_url(url)

def predict_from_url(url):
    """Returns google reverse image search prediction given image url."""
    r = google_search.reverse_search(url)
    return r["best_guess"]

def upload_image(path):
    """Uploads image to uploads.im and returns url.

    Equivalent to following curl call:
        curl --form "fileupload=@test.jpg" http://uploads.im/api?upload

    """
    r = requests.post('http://uploads.im/api?upload',
                  files=dict(input=open(path, 'rb')))
    return r.json()["data"]["img_url"]


if __name__ == "__main__":
    print(predict_from_path(args.image_path))