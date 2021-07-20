from flask import Flask, render_template, request
#import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.linear_model import RidgeClassifier

app=Flask(__name__)
model=pickle.load(open('loan_predict.pkl','rb'))
@app.route('/',methods=['GET'])

def Home():
    return render_template('index.html')



ridge=RidgeClassifier()

@app.route("/predict", methods=['POST'])
def predict():
    if request.method=='POST':
        ApplicantIncome=int(request.form['ApplicantIncome'])
        CoApplicantIncome=int(request.form['CoApplicantIncome'])
        LoanAmount=int(request.form['LoanAmount'])
        Loan_Amount_Term=int(request.form['Loan_Amount_Term'])
        Credit_History=request.form['Credit_History']
        if(Credit_History=='Credit_History_Good'):
            Credit_History_Good=1
            
        else:
            Credit_History_Good=0
         
        Married=request.form['Married']
        if(Yes_Married=='Yes_Married'):
            Yes_Married=1
            
        else:
            Yes_Married=0
            
        Children=request.form['Children']
        if(Children=='one'):
            one=1
            two=0
            three_plus=0
        elif(Children=='two'):
            one=0
            two=1
            three_plus=0
        elif(Children=='three_plus'):
            one=0
            two=0
            three_plus=1
            
        else:
            one=0
            two=0
            three_plus=0
        Graduated=request.form['Graduated']
        
        if(Graduated=='NotGraduated'):
            NotGraduated=1
        else:
            NotGraduated=0
            
        Employed=request.form['Employed']
        if(Employed=='yes_employed'):
            yes_employed=1
            
        else:
            yes_employed=0
        
        Living_area=request.form['Living_area']
        if(Living_area=='urban'):
            urban=1
            semiurban=0
            
        elif(living_area=='semiurban'):
            urban=0
            semiurban=1
            
        else:
            urban=0
            semiurban=0
            
        Gender=request.form['Gender']
        if(Gender=='male'):
            male=1
        else:
            male=0
            
            
        prediction=model.predict([[ApplicantIncome,CoApplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History_Good,Yes_Married,
                                  
                                  one,two,three_plus,NotGraduated,yes_employed,urban,semiurban,male]])  
    
    
        return render_template('index.html',prediction_text='your loan will approved {}'.format(prediction))

    else:
        return render_template('index.html')
    
    
if __name__=="__main__":
    app.run(debug=True)
       