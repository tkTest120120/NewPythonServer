from datetime import datetime, timedelta, timezone
import jwt
from time import sleep

secret_key = 'your-256-bit-secret'

def create_TOKEN(nguoi_tao , thoi_han):
    dt = datetime.now(tz=timezone.utc) + timedelta(days= thoi_han)
    encoded_token = jwt.encode(
        {"iss": nguoi_tao, "iat": datetime.now(), 'exp': dt, 'user_id': "abc", 'email': "nancy@gmail.com"},
        secret_key, algorithm='HS256')
    return encoded_token

def decode_verify_TOKEN(token):
    try:
        decode_token = jwt.decode(token, secret_key, algorithms=['HS256'])
        print(decode_token)
        return "Token ok"
    except jwt.exceptions.ExpiredSignatureError :
        return "Token đã hết hạn rồi"
    except jwt.exceptions.DecodeError:
        return "Token không hợp lệ"