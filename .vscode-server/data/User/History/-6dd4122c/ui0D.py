import boto3
import requests
from pathlib import Path


def printImages(table):
    response = table.scan()
    data = response['Items']
    save_location = Path("/home/ubuntu/Assignment1/images")
    for item in  data:
        img_data = requests.get(item['img_url']).content
        with open(save_location / item['title'], 'wb') as handler:
            handler.write(img_data)



    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

if __name__ == '__main__':
    dynamodb=None
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Music')
    printImages(table);