# pip freeze > requirements.txt export library to file txt
# https://www.youtube.com/watch?v=rfdNIOYGYVI
from flask import Flask, render_template , request , send_file
from flask import redirect , url_for
from time import sleep
from functions.function import get_Link_img , get_Link_Img_from_WEB , lai_Ngan_hang , speak

app = Flask(__name__ , static_folder="./web")

@app.get("/")
def index():
    return render_template('index.html' , title = "Home")

'''Lấy link ảnh từ Group Facebook'''
@app.post("/get_link_group")
def home():
    "https://www.facebook.com/groups/697332711026460/media/photos"
    link = get_Link_Img_from_WEB(request.form.get("url"))
    return link


@app.post("/test" )
def salvador():
    link = get_Link_img("https://www.facebook.com/groups/697332711026460/media/photos")
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
    return render_template("test.html")

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
    print(request.form.get("token"))
    print(request.form.get("content"))
    return redirect("/api/tts")

@app.get("/api/tts")
def get_TTS_MP3():
    return speak("Như thế này liệu có bán được API không nhỉ")


# if __name__ == '__main__':
#     app.run(debug=True)