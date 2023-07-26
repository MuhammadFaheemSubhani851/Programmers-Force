from flask import Flask, render_template, request
import hashlib
import os



testing = Flask(__name__)

@testing.route('/')
def welcome():
    return render_template('index2.html')


@testing.route('/uploadImage', methods=['POST','GET'])
def uploadImage():
    if request.method == 'POST':
        
        image_file = request.files['imageFile']
        
        
        im_path = os.path.join(image_file.filename)
        image_file.save(im_path)
        with open(im_path, "rb") as f:
            im_bytes = f.read()
            im_hash = str(hashlib.md5(im_bytes).hexdigest())


        
    return render_template('result2.html', image_hash = im_hash)
        
        
        
        
        
        
if __name__ == '__main__':
    testing.run(debug=True)         
        