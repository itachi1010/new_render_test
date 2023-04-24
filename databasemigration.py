import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db import connections

with open('dump.json') as f:
    data = json.load(f)

with connections['default'].cursor() as cursor:
    for obj in data:
        obj['pk'] = None
        obj['model'] = obj['model'].replace('appname.', '')  # Replace appname with your app's name
        sql = f"INSERT INTO {obj['model']} ({','.join(obj['fields'].keys())}) VALUES ({','.join(['%s']*len(obj['fields']))})"
        cursor.execute(sql, list(obj['fields'].values()))