from flask import Flask,render_template,request
import joblib
app=Flask(__name__)
model=joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    hours=float(request.form['hours'])
    predicted_grade=model.predict([[hours]])[0]
    return render_template('index.html',prediction_text=f'The predicted grade for studying {hours} hours is: {predicted_grade:.2f}')
if __name__=='__main__':
    app.run(debug=True)
