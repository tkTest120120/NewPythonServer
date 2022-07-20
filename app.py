# pip freeze > requirements.txt export library to file txt
# https://www.youtube.com/watch?v=rfdNIOYGYVI
from flask import Flask, render_template , request , send_file , send_from_directory
from flask import redirect , url_for
from time import sleep
import os
from functions.function import get_Link_img , get_Link_Img_from_WEB , lai_Ngan_hang , speak, speak_Public_MP3
from functions.token_jwt import decode_verify_TOKEN
import json
import base64

app = Flask(__name__ , static_folder="./web" , static_url_path="")

@app.get("/")
def index():
    return render_template('index.html' , title = "Home")

@app.get("/getip" )
def salvador():
    return request.host
    # link = get_Link_img("https://www.facebook.com/groups/697332711026460/media/photos")
    # return link

'''Lấy link ảnh từ Group Facebook'''
@app.post("/get_link_group")
def home():
    "https://www.facebook.com/groups/697332711026460/media/photos"
    link = get_Link_Img_from_WEB(request.form.get("url"))
    return link

@app.post("/upload")
def upload_img():
    return f"upload image successfully ! \n\n{request.files['pic']}"

''' Tính lãi ngân hàng'''
@app.get("/lai")
def ui_lai_tiet_kiem():
    return render_template("tinh_lai.html")

@app.post("/tinh_lai")
def tinh_lai():
    tien_gui = request.form.get("tien_gui")
    lai_suat = request.form.get("lai_suat")
    so_ngay_gui = request.form.get("so_ngay_gui")

    print(tien_gui , lai_suat , so_ngay_gui)

    return render_template(
        "tinh_lai.html" ,
        lai = lai_Ngan_hang(
            tien_gui,
            lai_suat,
            so_ngay_gui
        )
    )

''' Tag trong youtube '''
@app.get("/tag_youtube")
def input_tag():
    return render_template("youtube_tag.html")

@app.post("/tag_youtube")
def get_tag_youtube():
    youtube_tag = ""
    for i in str(request.form.get("tag_text")).replace("\r" , "").split("\n"):
        youtube_tag += i + ",\n"

    return render_template("youtube_tag.html" , youtube_tag = youtube_tag)

''' Trả file '''
@app.get("/api/input_tts")
def get_Input_TTS():
    return render_template("tts_form.html")

@app.post("/api/tts")
def get_TTS_token():
    # token_TTS = request.form.get("token")
    # token_TTS = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTY0NTE5NjgxMywiZXhwIjoxNjQ1MzQ0NDEzLCJ1c2VyX2lkIjoiYWJjIiwiZW1haWwiOiJuYW5jeUBnbWFpbC5jb20ifQ.pMto1n-XbgFTZ5Fvk5hVSOkN-N4ijBxugn5FcxN0an8"

    # with open(os.getcwd() + "/private/token.txt" , "w+") as f :
    #     f.write(token_TTS)
    #     f.close()

    text = request.form.get("content")
    # print(text)
    speak(text)
    return redirect("/api/tts")

@app.get("/api/tts")
def get_TTS_MP3():
    # token_TTS = ""

    # with open(os.getcwd() + "//private/token.txt" , "r") as f :
    #     token_TTS = f.read()
    #     f.close()
    # print(f"token_TTS : {token_TTS}")

    # decode_Token = decode_verify_TOKEN(token_TTS)

    # if decode_Token == "Token đã hết hạn rồi":
    #     return decode_Token
    # elif decode_Token == "Token không hợp lệ":
    #     return decode_Token
    # elif decode_Token == "Token ok" :
    #     print(f"decode_Token : {decode_Token}")
    #     path = str(os.getcwd())
    #     fileName = path + "/private/sound.mp3"
    #
    #     return send_file(fileName)
    # Free
    path = str(os.getcwd())
    fileName = path + "/private/sound.mp3"

    return send_file(fileName)

''' Chuyển văn bản thành giọng nói '''
@app.post("/api/tts_public")
def tts_Public():
    speak_Public_MP3(request.form.get("text"))
    return "/sound.mp3"

''' Google text to speech '''
@app.get("/google_tts")
def input_google_tts():
    return render_template("./google_text_to_speech/google_tts.html" , outputTTS = False)

@app.post("/google_tts")
def google_TTS():
    path = str(os.getcwd())

    text = json.loads(request.form.get("google_tts_text"))

    with open(path + f"/web/output.wav", "wb") as out:
        # Write the response to the output file.
        out.write(base64.b64decode(text["audioContent"]))
        print('Audio content written to file "output.wav"')
        print('Nội dung âm thanh được ghi vào tệp ...')
        out.close()

    return render_template("./google_text_to_speech/google_tts.html" , outputTTS = True)

'''test'''
@app.get("/test")
def test_UI_Template():
    return render_template("test.html")

if __name__ == '__main__':
    app.run(debug=True)