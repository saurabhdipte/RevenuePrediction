import pickle
from flask import Flask,render_template,request

app = Flask(__name__)
model=pickle.load(open('model.pkl', 'rb'))



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict',methods=['POST','GET'])
def predict():
    Temperature =float(request.form.get('temperature'))
    prediction = model.predict([[Temperature]])
    output=round(prediction[0],2) #since it is a list [0] represents the first element
    print(output)
    return render_template('index.html', prediction_text=f'Total revenue generated is Rs. {output}/-')

if __name__ == '__main__':
    app.run(debug=True)