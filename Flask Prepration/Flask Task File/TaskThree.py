from flask import Flask,redirect, url_for, render_template, request


testing = Flask(__name__)

@testing.route('/')
def welcome():
    return render_template('index3.html')


@testing.route('/gen', methods=['POST','GET'])
def gen():
    if request.method == 'POST':
        num1 = int(request.form['num'])

        
    return render_template('result3.html', num1 = num1)
        
        
        
        
        
if __name__ == '__main__':
    testing.run(debug=True)         
        