from flask import Flask, render_template, request
from datetime import datetime
import requests
import pprint
from src.qr_code.qrcode_generator import create_qrcode


app = Flask(__name__)

pp = pprint.PrettyPrinter(indent=4)
@app.route('/')
def home():
  dt = datetime.now().strftime("%Y")
  return render_template('index.html', date=dt)


@app.route('/guess/<name>')
def get_guess_page(name):
  dt = requests.get("https://api.agify.io", params={'name':name}).json()
  dt2 = requests.get("https://api.genderize.io", params={'name':name}).json()
  dt3 = {
    "some": {
      "thing": {
        "else": "SomethingElse",
        "other": "SomethingOther"
      },
      "stuff":"SomeStuff"
    }
  }
  dt.update(dt2)
  dt.update(dt3)
  print(dt)
  return render_template('guess.html', data=dt)


@app.route('/blog')
def get_blog_page():
  resp = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
  resp = resp.json()
  return render_template("blog.html", data=resp) 
# https://api.npoint.io/85201ce7a6ed16897d61
#  https://api.npoint.io/c790b4d5cab58020d391

@app.route('/qr_code', methods=["GET", "POST"])
@app.route('/qrcode', methods=["GET", "POST"])
def qrcode():
  if request.method == "GET":
    return render_template("qr_code.html")
  elif request.method == "POST":
    data={}
    url = request.form['url']
    print(url)
    img =  create_qrcode(url, base64encode=True)
    data['img'] = img
    data['url'] = url
    return render_template("qr_code.html", data=data)


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    # app.run()
    app.run(debug=True) # Just use this for developing


print("done")