from flask import Flask,render_template,url_for,request
import pandas as pd
import pickle

model = pickle.load(open(r"model/pickle/random_forest.pkl","rb"))
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    data_list =[]
    column = ['T','TM','Tm','SLP','H','VV','V','VM']
    for val in column:
        print (val)
        data_list.append(request.form[val])

    data = pd.DataFrame([data_list], columns = column)
    
    predicted_result = model.predict(data)
    
    print (predicted_result)
    
    if predicted_result < 12 :
        return render_template('good.html')
    elif predicted_result < 35.4 :
        return render_template('moderate.html')
    else:
        return render_template('unhealthy.html')



if __name__=="__main__":
    app.run(debug=True)