import json

def handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Privet, Andrey! Yay! :D'
    }

if __name__ == '__main__':
    handler(None, None)

