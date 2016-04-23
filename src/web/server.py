import operator
import collections
from flask import Flask
from flask import render_template
from flask import request
from PIL import Image
from common import data
from common import colors


app = Flask(__name__)
app.arts = data.load_from_json()


def sort_by_value(d):
    return sorted(d, key=operator.itemgetter(1), reverse=True)


@app.route('/', methods=['GET'])
def colors_page():
    color_matches_mapping = collections.defaultdict(int)

    for art in app.arts:
        hist = colors.hist_from_cache(art.filename)
        if hist:
            top_five = sort_by_value(hist.items())[0:5]
            color_names = [name for (name, _) in top_five]
            for color_name in color_names:
                color_matches_mapping[color_name] += 1

    color_matches = sort_by_value(color_matches_mapping.items())

    return render_template(
        'colors.jinja.html',
        color_name_mapping=colors.colors,
        color_matches=color_matches)


@app.route('/colors/<color_name>', methods=['GET'])
def color_page(color_name):
    # pagination
    page = int(request.args.get('page', '1'))
    page_size = int(request.args.get('pagesize', '25'))
    start = (page - 1) * page_size
    end = page * page_size

    # arts with the given color
    (r, g, b) = colors.colors[color_name]
    arts = []

    for art in app.arts:
        hist = colors.hist_from_cache(art.filename)
        if hist:
            top_five = sort_by_value(hist.items())[0:5]
            matches = [(name, percentage) for (name, percentage) in top_five if name == color_name]
            if matches:
                (name, percentage) = matches[0]
                arts.append((art, percentage))

    arts = sort_by_value(arts)[start:end]
    hasmore = len(arts) == page_size

    return render_template(
        'color.jinja.html',
        colorname=color_name,
        arts=arts,
        r=r, g=g, b=b,
        pagenumber=page,
        hasmore=hasmore)


@app.route('/artist/<artist_name>', methods=['GET'])
def artist_page(artist_name):
    arts = [
        art for
        art in app.arts
        if art.primary_maker.decode('utf-8') == artist_name
    ]
    return render_template(
        'artist.jinja.html',
        artist_name=artist_name,
        arts=arts)


@app.route('/art/<object_id>', methods=['GET'])
def art_page(object_id):
    art = next(art for art in app.arts if art.object_id == int(object_id))
    image = Image.open(art.filename)

    hist = colors.hist_from_cache(art.filename)
    if not hist:
        hist = colors.hist_from_image(image)
        colors.save_hist_to_cache(art.filename, hist)

    top_five = sort_by_value(hist.items())[0:5]

    return render_template(
        'art.jinja.html',
        art=art,
        color_name_mapping=colors.colors,
        color_histogram=top_five)


if __name__ == '__main__':
    app.debug = True
    app.static_folder = '../../static'
    app.run('0.0.0.0', port=8080)
