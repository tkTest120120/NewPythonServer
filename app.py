# pip freeze > requirements.txt export library to file txt
# https://www.youtube.com/watch?v=rfdNIOYGYVI
from flask import Flask, render_template
from function.function import get_Link_img , get_Link_Img_from_WEB

app = Flask(__name__)


@app.route("/")
def home():
    link = get_Link_Img_from_WEB("https://www.facebook.com/groups/697332711026460/media/photos")
    return link


@app.route("/test")
def salvador():
    link = get_Link_img("https://www.facebook.com/groups/697332711026460/media/photos")
    return link


# if __name__ == '__main__':
#     app.run(debug=True)