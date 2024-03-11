from flask import Flask,render_template,request,url_for
import pickle
import numpy as np

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route("/")
def home():
    return  render_template("index.html")

@app.route("/predict",methods=['POST'])
def predict():
    try:
        Time=float(request.form.get("Time"))
        Amount=float(request.form.get("Amount"))
        V_values=float(request.form.get("Transaction"))
        features=np.array([[Time,Amount,V_values]])
        prediction=model.predict(features)
      
        
        if prediction[0]==1:
            text="Fraudulent Transaction"
        else:
            text="Legitimate Transaction"
        return render_template("index.html",prediction_text=text)
    except Exception as e:
        print(f"Error:{e}")
        return render_template("index.html",prediction_text="Error")
    
if __name__=="__main__":
    app.run(debug=True)