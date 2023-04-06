import logging
import boto3
from botocore.exceptions import ClientError
import os
import requests
from pathlib import Path



def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def printImages(table):
    response = table.scan()
    data = response['Items']
    save_location = Path("/home/ubuntu/Assignment1/images")
    for item in  data:
        img_data = requests.get(item['img_url']).content
        filename = item['title'] + '.jpg'
        with open(save_location / 'image.jpg', 'wb') as handler:
            handler.write(img_data)


        object_name = os.path.basename('image.jpg')
        s3_client = boto3.client('s3')
        try:
            response = s3_client.upload_file(save_location / 'image.jpg', 's3848792assignment1', object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True

        # with open(save_location / filename, 'wb') as handler:
        #     handler.write(img_data)



    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

if __name__ == '__main__':
    dynamodb=None
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Music')
    printImages(table);