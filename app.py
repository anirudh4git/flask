from flask import Flask, render_template, redirect, url_for

#print('Hi')

#WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome To my webpage'

@app.route('/success/<int:score>')
def success(score):
    return f'The person has passed with score {score}'

@app.route('/fail/<int:score>')
def fail(score):
    return f'The person has failed with score {score}'

@app.route('/results/<int:marks>')
def results(marks):
    #result = ''
    if marks<34:
        result = 'fail'
    else:
        result= 'success'
        
    return redirect(url_for(result,score=marks))


#print(__name__)

if __name__  == '__main__':
    #print('Hi')
    app.run(debug = True)