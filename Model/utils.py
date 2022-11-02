import pandas as pd 
import numpy as np
import pickle
import json
import config




class HeartDisease():
    def __init__(self,age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
        self.age=age
        self.sex=sex
        self.cp=cp
        self.trestbps=trestbps
        self.chol=chol
        self.fbs=fbs
        self.restecg=restecg
        self.thalach=thalach
        self.exang=exang
        self.oldpeak=oldpeak
        self.slope=slope
        self.ca=ca
        self.thal=thal

    def load_model(self):
        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_dict=json.load(f)

        with open(config.PICKLE_FILE_PATH ,'rb') as f:
            self.model=pickle.load(f)

    def get_heart_disease(self):
        self.load_model()
        array = np.zeros(len(self.json_dict['columns']))


        array[0]=self.age 
        array[1]=self.sex
        array[2]=self.cp
        array[3]=self.trestbps
        array[4]=self.chol
        array[5]=self.fbs
        array[6]=self.restecg
        array[7]=self.thalach
        array[8]=self.exang
        array[9]=self.oldpeak
        array[10]=self.slope
        array[11]=self.ca
        array[12]=self.thal
        
        result = self.model.predict([array])[0]
        result1= "heart disease present" if result==1 else "healty human"
        return result1

if __name__ == "__main__":
    age=64
    sex=1
    cp=3
    trestbps=110
    chol=211
    fbs=0
    restecg=0
    thalach=144
    exang=1
    oldpeak=1.8
    slope=1
    ca=0
    thal=2

    Obj = HeartDisease(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    result=Obj.get_heart_disease()
    print(result)








        
        
        
        
       
