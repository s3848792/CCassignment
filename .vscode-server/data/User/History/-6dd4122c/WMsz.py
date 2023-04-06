import boto3
import requests


def printImages(table):
    response = table.scan()
    data = response['Items']
    save_location = Path("/home/ubuntu/Assignment1/images")
    for item in  data:
        print(item['img_url'])
        img_data = requests.get(img_url).content
        with open('images', 'image_name.jpg', 'wb') as handler:
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