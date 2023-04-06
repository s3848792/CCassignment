from decimal import Decimal
import json
import boto3

def printImages(music_table):
    for item in music_table:
        response = item.get_item(Key={'artist': artist, 'title': title})
        print(response['item'])

if __name__ == '__main__':
    dynamodb=None
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Music')
    printImages(table);