from flask import Flask, render_template,request, session,request
from flask_session import Session

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def cam():
    if(request.method=="POST"):
        img_id = request.form.get("count")
        print(f"img{img_id}")
    return render_template("index.html")


   
