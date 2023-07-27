import traceback
from flask import Flask
from flask import request,render_template

class ML:
    def __init__(self):
        self.available_models = {
            "face_detection": "/additional_drive/ML/face_detection",
            "car_detection": "/additional_drive/ML/car_detection",
            "shoe_detection": "/additional_drive/ML/shoe_detection",
            "cloth_detection": "/additional_drive/ML/cloth_detection",
            "signal_detection": "/additional_drive/ML/signal_detection",
            "water_level_detection": "/additional_drive/ML/water_level_detection",
            "missile_detection": "/additional_drive/ML/missile_detection"
        }
        self.loaded_models_limit = 2
        self.loaded_models = {
            model: self.load_weights(model)
            for model in list(self.available_models)[:self.loaded_models_limit]
        }
    
        self.frequency = {"face_detection": 1,
                         "car_detection": 1,
                         "shoe_detection":0,
                         "cloth_detection":0,
                         "signal_detection":0,
                         "water_level_detection":0,
                         "missile_detection":0}
    
    def load_weights(self, model):
        return self.available_models.get(model,None)

    def load_balancer(self, new_model):
    # Creating list for both models
        List1 = list(self.loaded_models.keys())[0]
        List2 = list(self.loaded_models.keys())[1]

    # Frequency value of 2 models
        frequency1 = self.frequency[List1]  # Use square brackets to access dictionary value
        frequency2 = self.frequency[List2]  # Use square brackets to access dictionary value

    # Get frequency of model and get new frequency
        new_freq = self.frequency[new_model]
        self.loaded_models[new_model] = new_freq

        if frequency1 <= frequency2:
            del self.loaded_models[List1]  # Use square brackets to delete dictionary key-value pair
            self.loaded_models[new_model] = self.available_models[new_model]
        else:
            del self.loaded_models[List2]  # Use square brackets to delete dictionary key-value pair
            self.loaded_models[new_model] = self.available_models[new_model]

        value = self.frequency[new_model]
        self.frequency[new_model] = value + 1

           
           
           
           
       
       
            


app = Flask(__name__)
ml = ML()

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/get_loaded_models', methods=['GET', 'POST'])
def get_loaded_models():
    return ml.loaded_models

@app.route('/process_request', methods=['GET', 'POST'])
def process_request():
    try:
        model = request.form["model"]
        if model not in ml.loaded_models:
            ml.load_balancer(model)
        return "processed by "+ ml.loaded_models[model]
    except:
        return str(traceback.format_exc())

app.run(host='0.0.0.0', port=5000)


