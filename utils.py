import os
import jwt
import time
from dotenv import load_dotenv

load_dotenv()
 

secret_key = os.getenv("JWT_SECRET")

if secret_key is None:
    raise Exception("JWT_SECRET not set in .env file")
    

def generate_token(user_id ,user_name):
    payload = {'user_id': user_id,'user_name': user_name, 'exp': time.time() + 30*24*60*60}  # expires in 30 days
    return jwt.encode(payload, secret_key, algorithm='HS256')

def verify_token(token):
    try:
        return jwt.decode(token, secret_key, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    
 