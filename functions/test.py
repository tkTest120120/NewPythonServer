from datetime import datetime, timedelta, timezone
import jwt
from time import sleep

# secret_key = 'your-256-bit-secret'
#
# dt = datetime.now(tz=timezone.utc) + timedelta(seconds=1)
# encoded_token = jwt.encode(
#     {"iss": "admin", "iat": datetime.now(), 'user_id': "abc", 'email': "nancy@gmail.com", 'exp': dt},
#     secret_key, algorithm='HS256')
# print(encoded_token)
# sleep(2)
# # decode above token
# decode_token = jwt.decode(encoded_token, secret_key, algorithms=['HS256'])
#
# content = decode_token
# print(content)
# print(content['user_id'])
# print('mã thông báo json được truy xuất thành công')


# jwt_payload = jwt.encode(
#     {"exp": datetime.now(tz=timezone.utc) + timedelta(seconds=1)},
#     "secret",
#     algorithm='HS256'
# )
#
# sleep(2)
#
# # JWT payload is now expired
# # But with some leeway, it will still validate
# try:
#     jwt_decode = jwt.decode(jwt_payload, "secret", algorithms=["HS256"])
# except jwt.exceptions.ExpiredSignatureError:
#     print("token đã hết hạn rồi ")