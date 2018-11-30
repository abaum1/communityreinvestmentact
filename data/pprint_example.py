import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

f = 'neighbors_midmod_2008.json'
with open(f) as infile:
	neighbors_dict = json.load(infile)

pp.pprint(neighbors_dict)