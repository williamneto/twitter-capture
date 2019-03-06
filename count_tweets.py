import json

FILE_NAME = "mangueira.json"

with open(FILE_NAME) as file:
    data = json.load(file)
    print("%s > %s" % (FILE_NAME, len(data)))