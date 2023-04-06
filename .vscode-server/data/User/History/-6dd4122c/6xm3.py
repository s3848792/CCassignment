import boto3

def printImages(table):
    response = table.scan()
    data = response['Items']
    for item in  data:
            print(item['web_url'])

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

if __name__ == '__main__':
    dynamodb=None
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Music')
    printImages(table);