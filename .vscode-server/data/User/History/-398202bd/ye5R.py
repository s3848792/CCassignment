from decimal import Decimal
import json
import boto3


def load_music(songs, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Music')
    for song in songs:
        print(song)
        title = song["title"]
        artist = song["artist"] 
        print("Adding song:", artist, title)
        table.put_item(Item=song)


if __name__ == '__main__':
    with open("a1.json") as json_file:
        music_list = json.load(json_file, parse_float=Decimal)
    load_music(music_list)