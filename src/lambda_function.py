import json

def handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Privet, Andrey!'
    }

if __name__ == '__main__':
    handler(None, None)

