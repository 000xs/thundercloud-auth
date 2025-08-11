import os
import jwt
import time
import bcrypt
from dotenv import load_dotenv

load_dotenv()

secret_key = os.getenv("JWT_SECRET")
if not secret_key:
    raise Exception("JWT_SECRET not set in .env file")

def password_hash(password: str) -> bytes:
    """Hash a plain text password with bcrypt."""
    plain_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(plain_bytes, salt)

def valid_hashed_password(plain_password, hashed_password) -> bool:
    """Verify a plain password against its hashed version."""
    plain_bytes = plain_password.encode('utf-8') if isinstance(plain_password, str) else plain_password
    hash_bytes = hashed_password if isinstance(hashed_password, bytes) else hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_bytes, hash_bytes)

def generate_token(user_id, user_name) -> str:
    """Generate a JWT for the user."""
    payload = {
        'user_id': user_id,
        'user_name': user_name,
        'exp': time.time() + 30*24*60*60  # 30 days
    }
    return jwt.encode(payload, secret_key, algorithm='HS256')

def verify_token(token):
    """Verify a JWT token and return payload or None."""
    try:
        return jwt.decode(token, secret_key, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
