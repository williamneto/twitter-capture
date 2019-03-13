import json

FILE_NAME = "tweetsreader/tweets/euapoionovaprevidencia.json"

with open(FILE_NAME) as file:
    data = json.load(file)
    print("%s > %s" % (FILE_NAME, len(data)))