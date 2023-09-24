import json
from decimal import Decimal


def serialize(data):
    return json.dumps(data)


def deserialize(data):
    return json.loads(data)


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super(MyEncoder, self).default(obj)



