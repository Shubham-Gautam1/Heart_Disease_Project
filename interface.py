from flask import Flask,render_template,request
import pickle,json
import numpy as np

with open('Log_model.pkl','rb') as file:
    log_reg = pickle.load(file)

with open('project_data.json') as file:
    data = json.load(file)



app = Flask(__name__)

@app.route('/')


@app.route('/Homepage')
def Homepage():
    return render_template('home.html')

@app.route('/submit',methods=['GET'])
def submit():

    male = request.args.get('male')
    age = request.args.get('age')
    currentSmoker = request.args.get('currentSmoker')
    cigsPerDay = request.args.get('cigsPerDay')
    BPMeds = request.args.get('BPMeds')
    prevalentStroke = request.args.get('prevalentStroke')
    prevalentHyp = request.args.get('prevalentHyp')
    diabetes = request.args.get('diabetes')
    totChol = request.args.get('totChol')
    sysBP = request.args.get('sysBP')
    diaBP = request.args.get('diaBP')
    BMI = request.args.get('BMI')
    heartRate = request.args.get('heartRate')
    glucose = request.args.get('glucose')

    

    array = np.zeros(len(data['columns']))
    array[0]=data['male'][male]
    array[1]=age
    array[2]=data['currentSmoker'][currentSmoker]
    array[3]=cigsPerDay
    array[4]=data['BPMeds'][BPMeds]
    array[5]=data['prevalentStroke'][prevalentStroke]
    array[6]=data['prevalentHyp'][prevalentHyp]
    array[7]=data['diabetes'][diabetes]
    array[8]=totChol
    array[9]=sysBP
    array[10]=diaBP
    array[11]=BMI
    array[12]=heartRate
    array[13]=glucose
    
    

    pred = log_reg.predict([array])[0]
    return render_template('after.html', data=pred)

if __name__=='__main__':
    app.run(host="0.0.0.0",port=8080)