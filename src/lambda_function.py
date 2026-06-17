import json

def handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello World!'
    }

if __name__ == '__main__':
    handler(None, None)

