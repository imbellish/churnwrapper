import requests
import settings
import json


class ChurnOver(object):
    
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                raise AttributeError("API conflict: '%s' is part of the '%s' API" % (key, self.__class__.__name__))
            if key not in settings.VALID_FIELDS:
                raise KeyError("'%s' is not a valid field" % (key, ))
            if key == 'entitystatus' and value not in settings.VALID_ENTITY_STATUS:
                raise AttributeError("'%s' is not a valid entity status")
            else:
                setattr(self, key, value)

    def call(self):
        data = json.dumps(self.__dict__)
        return data

