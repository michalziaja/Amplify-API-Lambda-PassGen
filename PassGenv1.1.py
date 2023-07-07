import string
import random
import json

def lambda_handler(event, context):
    num_characters = int(event['characters'])

    password = generate_password(num_characters)

    return {
        'statusCode': 200,
        'body': json.dumps('Your Password: ' + password)
    }

def generate_password(num_characters):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choices(characters, k=num_characters))
    return password
