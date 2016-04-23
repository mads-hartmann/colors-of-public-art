import os
import colors
import argparse
import sys
from PIL import Image
from common import data


def analyze(start, end):
    for art in data.load_from_json()[start:end]:
        filename = art.filename
        if os.path.exists(filename):
            hist = colors.hist_from_cache(filename)
            if not hist:
                try:
                    print 'Processing {}'.format(filename)
                    image = Image.open(filename)
                    hist = colors.hist_from_image(image)
                    colors.save_hist_to_cache(filename, hist)
                except:
                    print 'Failing to process image {}'.format(filename)
            else:
                print 'Skipping {}'.format(filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--start',
        help='Object id start interval',
        type=int,
        default=0)

    parser.add_argument(
        '--end',
        help='Object id end interval',
        type=int,
        default=sys.maxint)

    args = parser.parse_args()
    analyze(args.start, args.end)
