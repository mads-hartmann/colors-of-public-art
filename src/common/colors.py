from collections import defaultdict
import json


colors = {
    "lightpink": (255, 182, 193),
    "pink": (255, 192, 203),
    "crimson": (220, 20, 60),
    "lavenderblush": (255, 240, 245),
    "palevioletred": (219, 112, 147),
    "hotpink": (255, 105, 180),
    "deeppink": (255, 20, 147),
    "mediumvioletred": (199, 21, 133),
    "orchid": (218, 112, 214),
    "thistle": (216, 191, 216),
    "plum": (221, 160, 221),
    "violet": (238, 130, 238),
    "fuchsia": (255, 0, 255),
    "fuchsia": (255, 0, 255),
    "darkmagenta": (139, 0, 139),
    "purple": (128, 0, 128),
    "mediumorchid": (186, 85, 211),
    "darkviolet": (148, 0, 211),
    "darkorchid": (153, 50, 204),
    "indigo": (75, 0, 130),
    "blueviolet": (138, 43, 226),
    "mediumpurple": (147, 112, 219),
    "mediumslateblue": (123, 104, 238),
    "slateblue": (106, 90, 205),
    "darkslateblue": (72, 61, 139),
    "ghostwhite": (248, 248, 255),
    "lavender": (230, 230, 250),
    "blue": (0, 0, 255),
    "mediumblue": (0, 0, 205),
    "darkblue": (0, 0, 139),
    "navy": (0, 0, 128),
    "midnightblue": (25, 25, 112),
    "royalblue": (65, 105, 225),
    "cornflowerblue": (100, 149, 237),
    "lightsteelblue": (176, 196, 222),
    "lightslategray": (119, 136, 153),
    "slategray": (112, 128, 144),
    "dodgerblue": (30, 144, 255),
    "aliceblue": (240, 248, 255),
    "steelblue": (70, 130, 180),
    "lightskyblue": (135, 206, 250),
    "skyblue": (135, 206, 235),
    "deepskyblue": (0, 191, 255),
    "lightblue": (173, 216, 230),
    "powderblue": (176, 224, 230),
    "cadetblue": (95, 158, 160),
    "darkturquoise": (0, 206, 209),
    "azure": (240, 255, 255),
    "lightcyan": (224, 255, 255),
    "paleturquoise": (175, 238, 238),
    "aqua": (0, 255, 255),
    "aqua": (0, 255, 255),
    "darkcyan": (0, 139, 139),
    "teal": (0, 128, 128),
    "darkslategray": (47, 79, 79),
    "mediumturquoise": (72, 209, 204),
    "lightseagreen": (32, 178, 170),
    "turquoise": (64, 224, 208),
    "aquamarine": (127, 255, 212),
    "mediumaquamarine": (102, 205, 170),
    "mediumspringgreen": (0, 250, 154),
    "mintcream": (245, 255, 250),
    "springgreen": (0, 255, 127),
    "mediumseagreen": (60, 179, 113),
    "seagreen": (46, 139, 87),
    "honeydew": (240, 255, 240),
    "darkseagreen": (143, 188, 143),
    "palegreen": (152, 251, 152),
    "lightgreen": (144, 238, 144),
    "limegreen": (50, 205, 50),
    "lime": (0, 255, 0),
    "forestgreen": (34, 139, 34),
    "green": (0, 128, 0),
    "darkgreen": (0, 100, 0),
    "lawngreen": (124, 252, 0),
    "chartreuse": (127, 255, 0),
    "greenyellow": (173, 255, 47),
    "darkolivegreen": (85, 107, 47),
    "yellowgreen": (154, 205, 50),
    "olivedrab": (107, 142, 35),
    "ivory": (255, 255, 240),
    "beige": (245, 245, 220),
    "lightyellow": (255, 255, 224),
    "lightgoldenrodyellow": (250, 250, 210),
    "yellow": (255, 255, 0),
    "olive": (128, 128, 0),
    "darkkhaki": (189, 183, 107),
    "palegoldenrod": (238, 232, 170),
    "lemonchiffon": (255, 250, 205),
    "khaki": (240, 230, 140),
    "gold": (255, 215, 0),
    "cornsilk": (255, 248, 220),
    "goldenrod": (218, 165, 32),
    "darkgoldenrod": (184, 134, 11),
    "floralwhite": (255, 250, 240),
    "oldlace": (253, 245, 230),
    "wheat": (245, 222, 179),
    "orange": (255, 165, 0),
    "moccasin": (255, 228, 181),
    "papayawhip": (255, 239, 213),
    "blanchedalmond": (255, 235, 205),
    "navajowhite": (255, 222, 173),
    "antiquewhite": (250, 235, 215),
    "tan": (210, 180, 140),
    "burlywood": (222, 184, 135),
    "darkorange": (255, 140, 0),
    "bisque": (255, 228, 196),
    "linen": (250, 240, 230),
    "peru": (205, 133, 63),
    "peachpuff": (255, 218, 185),
    "sandybrown": (244, 164, 96),
    "chocolate": (210, 105, 30),
    "saddlebrown": (139, 69, 19),
    "seashell": (255, 245, 238),
    "sienna": (160, 82, 45),
    "lightsalmon": (255, 160, 122),
    "coral": (255, 127, 80),
    "orangered": (255, 69, 0),
    "darksalmon": (233, 150, 122),
    "tomato": (255, 99, 71),
    "salmon": (250, 128, 114),
    "mistyrose": (255, 228, 225),
    "lightcoral": (240, 128, 128),
    "snow": (255, 250, 250),
    "rosybrown": (188, 143, 143),
    "indianred": (205, 92, 92),
    "red": (255, 0, 0),
    "brown": (165, 42, 42),
    "firebrick": (178, 34, 34),
    "darkred": (139, 0, 0),
    "maroon": (128, 0, 0),
    "white": (255, 255, 255),
    "whitesmoke": (245, 245, 245),
    "gainsboro": (220, 220, 220),
    "lightgrey": (211, 211, 211),
    "silver": (192, 192, 192),
    "darkgray": (169, 169, 169),
    "gray": (128, 128, 128),
    "dimgray": (105, 105, 105),
    "black": (0, 0, 0)
}


def from_rgb(r, g, b):
    best_diff = 765
    match_color = None
    for name, (color_r, color_g, color_b) in colors.items():
        r_diff = abs(color_r - r)
        g_diff = abs(color_g - g)
        b_diff = abs(color_b - b)
        sum_diff = r_diff + g_diff + b_diff

        if sum_diff < best_diff:
            best_diff = sum_diff
            match_color = name

        if best_diff < 5:
            return match_color

    return match_color


def hist_from_image(image):
    pixels = 0
    hist = defaultdict(int)

    for (r, g, b) in image.getdata():
        color = from_rgb(r, g, b)
        pixels += 1
        hist[color] += 1

    total_number_of_colors = sum(hist.values())

    for k, v in hist.items():
        new_value = float(v) / float(total_number_of_colors)
        hist[k] = new_value

    return hist


def save_hist_to_cache(filename, hist):
    cache_filename = '{}.hist.cache'.format(filename)
    with open(cache_filename, 'w') as cache_file:
        json.dump(hist, cache_file)


def hist_from_cache(filename):
    cache_filename = '{}.hist.cache'.format(filename)
    try:
        with open(cache_filename) as json_data:
            return json.load(json_data)
    except:
        return None
