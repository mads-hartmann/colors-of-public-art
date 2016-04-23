import operator
import json
import collections
import argparse
from common import data
from common import colors

def colordump(path):
    years = collections.defaultdict(dict)

    for art in data.load_from_json():
        if art.display_date:
            hist = colors.hist_from_cache(art.filename)
            if hist:
                top = sorted(hist.items(), key=operator.itemgetter(1), reverse=True)
                for color in [name for (name, _) in top]:
                    if color not in years[art.display_date]:
                        years[art.display_date][color] = 0
                    years[art.display_date][color] += 1

    years_top_five = collections.defaultdict(int)

    for year, year_colors in years.iteritems():
        top = sorted(year_colors.items(), key=operator.itemgetter(1), reverse=True)
        years_top_five[year] = [color for [color, count] in top]

    json.dump(path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', help='Where to store the json dump')
    args = parser.parse_args()
    colordump(args.output)
