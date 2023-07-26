### building URL dynamically 
### variable rules 

from flask import Flask, redirect, url_for


testing = Flask(__name__)


@testing.route('/')
def welcome():
    return "Working as data scientist in pf"


@testing.route('/success/<int:score>')
def success(score):
    return "<html><body><h1> The result is passed </h1> </body></html>"

@testing.route('/fail/<int:score>')
def fail(score):
    return "The student has fail and the score is: " +str(score)

@testing.route('/results/<int:marks>')
def results(marks):
    result = " "
    if marks>50:
        result = "success"
    else:
        result = "fail"
    
    return redirect(url_for(result,score=marks))


if __name__ == '__main__':
    testing.run(debug=True) 