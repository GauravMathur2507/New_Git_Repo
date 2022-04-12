from flask import Flask, request
from flasgger import Swagger
import pickle
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
Swagger(app)

pickled_model = open("pickle_diabetes_model.pkl","rb")
regression = pickle.load(pickled_model)

@app.route('/')  #decorators
def home():
    return "Welcome to Diabetes Regression Model"

@app.route('/predict')
def predict_diabetes():

    """Lets try Swagger from flasgger
    ---
    parameters:
        - name: age
          in: query
          type: number
          required: true  
        - name: sex
          in: query
          type: char
          required: true
        - name: bmi
          in: query
          type: number
          required: true
        - name: bp
          in: query
          type: number
          required: true
        - name: s1
          in: query
          type: number
          required: true
        - name: s2
          in: query
          type: number
          required: true
        - name: s3
          in: query
          type: number
          required: true
        - name: s4
          in: query
          type: number
          required: true
        - name: s5
          in: query
          type: number
          required: true
        - name: s6
          in: query
          type: number
          required: true

    responses:
        200:
            description: The result is    
    """

    age1 = request.args.get("age")
    sex1 = request.args.get("sex")
    bmi = request.args.get("bmi")
    bp = request.args.get("bp")
    s11 = request.args.get("s1")
    s12 = request.args.get("s2")
    s13 = request.args.get("s3")
    s14 = request.args.get("s4")
    s15 = request.args.get("s5")
    s16 = request.args.get("s6")

    result = regression.predict([[age1, sex1, bmi, bp,s11,s12,s13,s14,s15,s16]])

    return f"The target prediction is {result}"

if __name__ == "__main__":
    app.run()