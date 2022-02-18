from datetime import datetime, timedelta, timezone
import jwt
from time import sleep
from functions import function

# secret_key = 'your-256-bit-secret'
#
# def create_TOKEN(nguoi_tao , thoi_han):
#     dt = datetime.now(tz=timezone.utc) + timedelta(seconds=60)
#     encoded_token = jwt.encode(
#         {"iss": nguoi_tao, "iat": datetime.now(), 'exp': dt, 'user_id': "abc", 'email': "nancy@gmail.com"},
#         secret_key, algorithm='HS256')
#     return encoded_token
# a = create_TOKEN("admin" , 1)
# print(a)
# # sleep(2)
# # decode above token
# def decode_verify_TOKEN():
#     try:
#         decode_token = jwt.decode(a, secret_key, algorithms=['HS256'])
#         print(decode_token)
#         return True
#     except jwt.exceptions.ExpiredSignatureError :
#         print("Token đã hết hạn rồi ")
#         return False
# decode_verify_TOKEN()
from gtts import gTTS
tts = gTTS(text="xin thu lai nha", lang="vi", slow=False)
tts.save("./ai.mp3")
# playsound.playsound("sound.mp3", True)
# os.remove("sound.mp3")
print("\n\nxong")

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