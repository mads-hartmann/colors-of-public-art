import os
import urllib
import argparse
from common import data


def download(desired_count):
    for art in data.load_from_json()[0:desired_count]:
        if art.image_url and art.object_id:
            filename = 'static/images/{}.jpg'.format(art.object_id)
            if not os.path.exists(filename):
                print 'Downloading {} to {}'.format(art.image_url, filename)
                urllib.urlretrieve(art.image_url, filename)
            else:
                print 'Skipping {}'.format(filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', help='Object id start interval', type=int)
    args = parser.parse_args()
    download(args.count)
