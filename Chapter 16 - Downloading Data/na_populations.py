from pygal.maps.world import World

wm = World()
wm.title = "Population of countries in North America"

wm.add('North America', {'ca': 34_126_000, 'mx': 113_423_000, 'us': 309_349_000})

wm.render_to_file('na_populations.svg')