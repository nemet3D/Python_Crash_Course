import json

from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LS, RotateStyle as RS

from country_codes import get_country_code

year = 2016

# Load the data into a list.
filename = 'gdp_json.json'
with open(filename) as f:
    gdp_data = json.load(f)

# Build a dictionary of GDP data.
cc_gdps = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == year:
        country = gdp_dict['Country Name']
        gdp = int(float(gdp_dict['Value']))
        code = get_country_code(country)
        if code:
            cc_gdps[code] = gdp

# Group the countries into 3 GDP levels.
cc_gdp_1, cc_gdp_2, cc_gdp_3 = {}, {}, {}
for cc, gdp in cc_gdps.items():
    if gdp < 10_000_000_000:
        cc_gdp_1[cc] = gdp
    elif gdp < 50_000_000_000:
        cc_gdp_2[cc] = gdp
    else:
        cc_gdp_3[cc] = gdp

# Se how many countries are in each level.
print(len(cc_gdp_1), len(cc_gdp_2), len(cc_gdp_3))

wm_style = RS('#336699', base_style=LS)
wm = World(style=wm_style)
wm.title = 'World GDP in ' + str(year) + ' by Country'
wm.add('<10b', cc_gdp_1)
wm.add('10b-50b', cc_gdp_2)
wm.add('>50b', cc_gdp_3)

wm.render_to_file('world_gdp.svg')