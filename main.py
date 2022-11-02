import re
from Model.utils import HeartDisease
from flask import Flask,render_template,request,jsonify

app = Flask(__name__)  # api instance

@app.route("/")
def hello_flask():
    print("We are in home api")
    return render_template("index.html")

@app.route("/heart_disease",methods=['POST'])
def disease():
    age=int(request.form.get('age'))
    sex=int(request.form.get('sex'))
    cp=int(request.form.get('cp'))
    trestbps=int(request.form.get('trestbps'))
    chol=int(request.form.get('chol'))
    fbs=int(request.form.get('fbs'))
    restecg=int(request.form.get('restecg'))
    thalach=int(request.form.get('thalach'))
    exang=int(request.form.get('exang'))
    oldpeak=float(request.form.get('oldpeak'))
    slope=int(request.form.get('slope'))
    ca=int(request.form.get('ca'))
    thal=int(request.form.get('thal'))

    Obj = HeartDisease(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    result=Obj.get_heart_disease()

    return render_template("index.html",prediction=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001,debug=True)