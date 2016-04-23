import json


def default(f, default_value):
    try:
        return f()
    except:
        return default_value


def get_image(obj):
    try:
        return [
            field['value'].encode('utf-8')
            for field in default(lambda: obj['media_0']['values']['field'], [])
            if default(lambda: field['name'].encode('utf-8') == 'filename', False)
        ][0]
    except:
        return None


class Dimensions(object):
    def __init__(self, width, height, depth, unit):
        self.width = width
        self.height = height
        self.depth = depth
        self.unit = unit

    def __str__(self):
        return 'Dimensions({},{},{},{})'.format(
            self.width,
            self.height,
            self.depth,
            self.unit)

    def __repr__(self):
        return str(self)

    @classmethod
    def from_json(cls, obj):
        try:
            dimensions = default(lambda: obj['dimensions']['value'].encode('utf-8'), '')
            components = dimensions.split(' ')
            if len(components) == 4:
                width = components[0]
                height = components[2]
                unit = components[3]
                return Dimensions(width, height, None, unit)
            elif len(components) == 6:
                width = components[0]
                height = components[2]
                depth = components[4]
                unit = components[5]
                return Dimensions(width, height, depth, unit)
            else:
                raise Exception('Can\'t parse {}'.format(dimensions))
        except:
            return None


class Location(object):
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    @classmethod
    def from_json(cls, obj):
        latitude = default(lambda: float(obj['lat']['value']), 0)
        longitude = default(lambda: float(['lng']['value']), 0)
        return Location(longitude, latitude)

    def __str__(self):
        return 'Location({},{})'.format(
            self.longitude,
            self.latitude)

    def __repr__(self):
        return str(self)


class Art(object):
    def __init__(self, title, classification, object_id, dimensions, primary_maker, image_url, location, display_date):
        self.title = title
        self.classification = classification
        self.object_id = object_id
        self.dimensions = dimensions
        self.primary_maker = primary_maker
        self.image_url = image_url
        self.location = location
        self.display_date = display_date

    @classmethod
    def from_json(cls, obj):
        classification = default(lambda: obj['classifications']['value'].encode('utf-8'), '')
        dimensions = Dimensions.from_json(obj)
        object_id = default(lambda: int(obj['id']['value']), None)
        title = default(lambda: obj['title']['value'].encode('utf-8'), 'No Title')
        primary_maker = default(lambda: obj['primaryMaker']['value'].encode('utf-8'), 'Unknown Artist')
        display_date = default(lambda: str(obj['displayDate']['value'])[0:4], None)
        image_url = get_image(obj)
        location = Location.from_json(obj)
        return Art(title, classification, object_id, dimensions, primary_maker, image_url, location, display_date)

    @property
    def filename(self):
        return 'static/images/{}.jpg'.format(self.object_id)

    def __str__(self):
        return 'Art({},{},{},{},{},{}, {}, {})'.format(
            self.title,
            self.classification,
            self.object_id,
            self.dimensions,
            self.primary_maker,
            self.image_url,
            self.location,
            self.display_date)

    def __repr__(self):
        return str(self)


def parse(json_object):
    objects = json_object['objects']
    for obj in objects:
        art = Art.from_json(obj)
        if art.classification == 'Maleri':
            yield art


def load_from_json():
    with open('data/dump.json') as json_data:
        json_object = json.load(json_data)
        return list(parse(json_object))
