from flask import Flask

app = Flask(__name__)
print("app is working")
# وقتی اینجوری دامین رو ست کنی، اگه واسه دامین اصلی ریکوست بفرستی، میره تو این تابع
@app.route('/')
def index():
    # اینجا هم لینک اون ایمیج رو قرار میدی، میتونه بصورت متغیر هم باشه
    return "https://wallpapercave.com/wp/wp14144128.jpg"

if __name__ == '__main__':
    app.run()