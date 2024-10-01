
from flask import Flask, render_template, request
import pickle
import numpy as np

with open('F:/vs code/commerce/data_science_assin_NB_model.pkl','rb') as f :
    model = pickle.load(f)
    

app = Flask(__name__)

@app.route('/')
def man():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = float(request.form['b'])
    data3 = float(request.form['c'])
    
    if data1 == 'male' or 'Male' or 'MALE' or 'M' or 'm':
        data1 = 1
    else :
        data1 = 0
        
    arr = np.array([[data1, data2, data3]])
    
    pred = int(model.predict(arr))
    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)

