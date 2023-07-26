

from flask import Flask, redirect, url_for, render_template, request 


testing = Flask(__name__)


@testing.route('/')
def welcome():
    return render_template('index1.html')
    

 

### result checker through html page 
@testing.route('/done', methods=['POST'])
def done():
    square = 0
    if request.method == 'POST':

        num1 = int(request.form['num'])
        square = num1*num1
     
    return render_template('result1.html', square1 = square)
        


if __name__ == '__main__':
    testing.run(debug=True) 