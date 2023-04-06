from decimal import Decimal
import json
import boto3


def load_movies(movies, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Music')
    for song in movies:
        artist = song['year']
        title = song['title']
        print("Adding song:", artist, title)
        table.put_item(Item=song)


if __name__ == '__main__':
    with open("moviedata.json") as json_file:
    movie_list = json.load(json_file, parse_float=Decimal)
    load_movies(movie_list)