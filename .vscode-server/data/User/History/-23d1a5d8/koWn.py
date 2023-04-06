import boto3

dynamodb = boto3.resource('dynamodb',region_name='ap-southeast-2')

table = dynamodb.create_table(
    TableName='Music',
    KeySchema=[
        {
            'AttributeName': 'Partition',
            'KeyType': 'S'  #Partition key
        },
        {
            'AttributeName': 'Sort',
            'KeyType': 'N'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'artitst',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'web_url',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'image_url',
            'AttributeType': 'S'
        },

    ],
)