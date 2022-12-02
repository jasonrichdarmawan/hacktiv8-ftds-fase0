import pandas as pd
import numpy as np
import joblib
from flask import Flask, request, jsonify

# App Initialization
app = Flask(__name__)

# Load The Models

with open('final_pipeline.pkl', 'rb') as file_1:
    model_pipeline = joblib.load(file_1)
    
import tensorflow as tf

model_ann = tf.keras.models.load_model('titanic_model.h5')

# Route : Homepage
@app.route('/')
def home():
    return '<h1>It works!</h1>'

@app.route('/predict', methods=['POST'])
def titanic_predict():
    args = request.json
    
    data_inf = {
        'PassengerId': args.get('PassengerId'),
        'Pclass': args.get('Pclass'),
        'Name': args.get('Name'),
        'Sex': args.get('Sex'),
        'Age': args.get('Age'),
        'SibSp': args.get('Sibsp'),
        'Parch': args.get('Parch'),
        'Ticket': args.get('Ticket'),
        'Fare': args.get('Fare'),
        'Cabin': args.get('Cabin'),
        'Embarked': args.get('Embarked')
    }
    
    print('[DEBUG] Data Inference : ', data_inf)
    
    # Transform Inference-Set
    data_inf = pd.DataFrame(data_inf)
    data_inf_transform = model_pipeline.transform(data_inf)
    y_pred_inf = model_ann.predict(data_inf_transform)
    y_pred_inf = np.where(y_pred_inf >= 0.5, 1, 0)
    
    label = [
        "Not Survived" if instance == 0 
        else "Survived" 
        for instance in y_pred_inf
    ]
    
    print('[DEBUG] Result : ', y_pred_inf, label)
    print('')
    
    response = jsonify(
        result = str(y_pred_inf),
        label_names = label
    )
    
    return response

if __name__ == '__main__':
    # host='0.0.0.0' to have have the server available externally as well.
    # make sure to remove parameter port when deploying.
    app.run(host='0.0.0.0', port=5001)