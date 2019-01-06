from pygal.maps.world import World

wm = World()
wm.title = "North, Central and South America"

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cu', 'cr', 'do', 'gt', 'hn', 'ht', 'jm', 'ni', 'pa', 'pr', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe',
    'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')