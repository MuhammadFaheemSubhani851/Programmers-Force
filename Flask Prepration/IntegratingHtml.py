### Integrate HTML with Flask
### HTTP verb Get and Post 

from flask import Flask, redirect, url_for, render_template, request 


testing = Flask(__name__)


@testing.route('/')
def welcome():
    return render_template('index.html')


@testing.route('/success/<int:score>')
def success(score):
    
    res= " "
    if score>=50:
       res="PASS"
    else:
        res = "FAIL"
    
    return render_template('result.html', result = res)



@testing.route('/fail/<int:score>')
def fail(score):
    return "The student has fail and the score is: " +str(score)


### result checker 
@testing.route('/results/<int:marks>')
def results(marks):
    result = " "
    if marks>50:
        result = "success"
    else:
        result = "fail"
    
    return redirect(url_for(result,score=marks))

### result checker through html page 
@testing.route('/submit', methods=['POST','Get'])
def submit():
    total_score=0
    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c= float(request.form['c'])
        data_science= float(request.form['datascience'])
        
        total_score = (science+ maths + c + data_science)/4
        
    res = " "
    if total_score>=50:
        res="success"
    else:
        res="fail"
        
    return redirect(url_for(res, score=total_score))
        
        
if __name__ == '__main__':
    testing.run(debug=True) 