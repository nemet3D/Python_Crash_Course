import json

from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LS, RotateStyle as RS

from country_codes import get_country_code

# Load the data into a list.
filename = 'gdp_json.json'
with open(filename) as f:
    gdp_data = json.load(f)

# Build a dictionary of gdp data.
cc_gdp = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == '2016':
        country = pop_dict['Country Name']
        gdp = int(float(pop_dict['Value']))
        code = get_country_code(country)
        if code:
            cc_populations[code] = population

# Group the countries into 3 population levels.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10_000_000:
        cc_pops_1[cc] = pop
    elif pop < 100_000_000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# Se how many countries are in each level.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RS('#336699', base_style=LS)
wm = World(style=wm_style)
wm.title = 'World gdp in 2016, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-100m', cc_pops_2)
wm.add('>100m', cc_pops_3)

wm.render_to_file('world_gdp.svg')