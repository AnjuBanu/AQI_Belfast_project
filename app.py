from flask import Flask,render_template,request
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
        print (request.form[val])
        if request.form[val] == "":
            return render_template('home.html')
        else:
            data_list.append(request.form[val])

    data = pd.DataFrame([data_list], columns = column)
    
    predicted_result = model.predict(data)
    
    print (predicted_result)
    
    if predicted_result < 50 :
        return render_template('good.html', result = predicted_result)
    elif predicted_result < 100 :
        return render_template('moderate.html', result = predicted_result)
    elif predicted_result < 150 :
        return render_template('unhealthy_sensitive.html', result = predicted_result)
    elif predicted_result < 200 :
        return render_template('unhealthy.html', result = predicted_result)
    elif predicted_result < 200 :
        return render_template('very_unhealthy.html', result = predicted_result)
    else:
        return render_template('hazardous.html', result = predicted_result)





if __name__=="__main__":
    app.run(debug=True)