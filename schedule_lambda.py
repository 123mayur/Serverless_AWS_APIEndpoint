import boto3
import json
import datetime
import calendar
from croniter import croniter
import pandas as pd
db = boto3.resource('dynamodb')
table = db.Table('Myapp')


def create_schedule(event):
    payload = json.loads(json.dumps(event))
    table.put_item(Item=payload)
    return json.dumps({"message":"your schedule is created"})

def fetch_all():
    response= table.scan()['Items']
    return json.dumps(response)

def get_schedule(event):
    key = json.loads(json.dumps(event))
    responce = table.get_item(Key=key).get('Item')
    if responce:
        s_date = responce['s_date']
        cron = croniter(s_date)
        date = cron.get_next(datetime.datetime)
        dates = pd.date_range(date, periods=5, freq='D')
        mylist =[]
        for x in dates:
            days = calendar.day_name[x.weekday()]
            mylist.append(days)
        return json.dumps(mylist)
    else:
        return json.dumps({"message":"shedule not fount"})

def update_schedule(event):
    payload = json.loads(json.dumps(event))
    id = payload['id']
    key ={'id':id}
    attribute_updates = {key: {'Value': value, 'Action': 'PUT'}
                         for key, value in payload}
    table.update_item(Key=key, AttributeUpdates=attribute_updates)
    return json.dumps({"message":"successfull"})

def delete_schedule(event):
    id = json.loads(json.dumps(event))
    key = id
    table.delete_item(Key=key)
    return json.dumps({"message":"schedule is deleted"})











