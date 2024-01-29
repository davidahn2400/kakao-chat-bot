# app.py
from flask import Flask, render_template
import random

#Flask 객체 인스턴스 생성
app = Flask(__name__)

luck = ["myimage1", "myimage2", "myimage3", "myimage4", "myimage5", 
        "myimage6", "myimage7"]

menu = random.choice(luck)

if menu == "myimage1":
  @app.route('/03')
  def myimage1():
    return render_template("myimage1.html")

if menu == "myimage2":
  @app.route('/08')
  def myimage2():
    return render_template("myimage2.html")

if menu == "myimage3":
  @app.route('/29')
  def myimage3():
    return render_template("myimage3.html")
  
if menu == "myimage4":
  @app.route('/05')
  def myimage4():
    return render_template("myimage4.html")

if menu == "myimage5":
  @app.route('/14')
  def myimage5():
    return render_template("myimage5.html")
  
if menu == "myimage6":
  @app.route('/38')
  def myimage6():
    return render_template("myimage6.html")
  
if menu == "myimage7":
  @app.route('/09')
  def myimage7():
    return render_template("myimage7.html")


@app.route('/') # 접속하는 url
def index():
  return render_template('index.html')

if __name__=="__main__":
  app.run()
  # host 등을 직접 지정하고 싶다면
  # app.run(host="127.0.0.1", port="5000", debug=True)


  