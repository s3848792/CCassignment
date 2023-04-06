from decimal import Decimal
import json
import boto3


if __name__ == '__main__':
    with open("a1.json") as json_file:
        music = json.load(json_file, parse_float=Decimal)
        music_list = music["songs"]
    load_music(music_list)