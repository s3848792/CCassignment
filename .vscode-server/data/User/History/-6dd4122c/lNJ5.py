from decimal import Decimal
import json
import boto3

def load_music(songs, dynamodb=None):


if __name__ == '__main__':
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Music')
    printImages();