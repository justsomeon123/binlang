import json,pathlib,sys
objects = json.load(open("objects.json"))
file = sys.argv[1]
filecontent = pathlib.Path(file).read_text().splitlines()