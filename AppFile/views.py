from flask import render_template, redirect, request, session
from AppFile import app
import time, os, cv2

@app.get("/")
def home():
    session['ID'] = app.config['ID']
    app.config['ID'] += 1
    
    return render_template("./HTMLFile/home.html", NUM=session['ID'])

@app.get("/wait")
def wait():
    num = session['ID']
    time.sleep(30)
    return str(num)

@app.get("/upload")
def upload():
    return render_template("./HTMLFile/upload.html")

@app.route("/result", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        video = request.files['video']
        fileFormat = os.path.splitext(video.filename)[1]
        fileName = str(session['ID']) + fileFormat
        if request.form["num"] == '0':
            path = os.getcwd() + "\AppFile\static\\" + fileName
        elif request.form["num"] == '1':
            path = ".\AppFile\static\\" + fileName
        
        session['path'] = path
        video.save(path)
        return redirect("/result")
    
    return render_template("./HTMLFile/result.html", path=os.getcwd())