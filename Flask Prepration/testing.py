### building URL dynamically 
### variable rules 

from flask import Flask


testing = Flask(__name__)


@testing.route('/')
def welcome():
    return "Working as data scientist in pf"


@testing.route('/Faheem')
def pf():
    return "welcome in programmers force"



if __name__ == '__main__':
    testing.run(debug=True) 