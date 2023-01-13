import numpy as np
from flask import Flask, render_template, redirect, url_for, request
import logging

#print('Hi')

#WSGI Application
app = Flask(__name__)

logging.basicConfig(filename='record.log', level=logging.DEBUG, format =
                    f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/final_report/<int:score>')
def report(score):
    if score <= 33:
        res = 'Fail'
    else:
        res='Pass'
    exp = {'SCORE':score, 'RESULT':res}
    return render_template('result.html', result = exp)

'''@app.route('/fail/<int:score>')
def fail(score):
    return f'The person has failed with score {score}' '''

'''@app.route('/results/<int:marks>')
def results(marks):
    #result = ''
    if marks<34:
        result = 'fail'
    else:
        result= 'success'
        
    return redirect(url_for(result,score=marks)) '''

@app.route('/submit', methods = ['GET','POST'])
def submit():
    #total_score=np.random.randint(89)
    #total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science = float(request.form['datascience'])
        app.logger.info('Info level log')
        total_score = (science+maths+c+data_science)/4
    elif request.method=='GET' :
        total_score = np.random.randint(89)
    return redirect(url_for('report',score=total_score))




#print(__name__)

if __name__  == '__main__':
    #print('Hi')
    app.run(debug = True)