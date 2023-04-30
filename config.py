import json_store as js

config = js.open('config.json')

assert isinstance(config['OPENAPI_KEYS'], list), 'OPENAPI_KEYS must be an Array'
assert len(config['OPENAPI_KEYS']) > 0, 'OPENAPI_KEYS should have 1 or more item'
