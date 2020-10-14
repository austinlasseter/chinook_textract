import json
import boto3


def lambda_handler(event, context):

    bucket="sagemaker-chinook-textract"
    document="chinook.png"
    client = boto3.client('textract')



    #process using S3 object
    response = client.detect_document_text(
        Document={'S3Object': {'Bucket': bucket, 'Name': document}})

    #Get the text blocks
    blocks=response['Blocks']
    
    output = {
        'statusCode': 200,
        'body': json.dumps(blocks)
    }               
    
    body = json.loads(output['body'])
    
    # get just the data we want
    extracted_data=[]
    for block in body:
        if block['BlockType'] != 'PAGE':
            extracted_data.append(block['Text'])
    # save it to json        
    json_string = json.dumps(extracted_data)
    
    # store it on s3
    s3 = boto3.client('s3')
    
    s3.put_object(
         Body=str(json.dumps(json_string)),
         Bucket="sagemaker-chinook-textract",
         Key='chinook_output.json'
    )
    
