import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds017636.mlab.com:17636/heroku
host = "ds017636.mlab.com"
port = 17636
db_name = "heroku"
username = "1"
password = "1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=username, password=password)


def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
