import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Flask, request, jsonify, render_template,url_for
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
tf_transformer = pickle.load(open('tfidf1.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    tfidf = TfidfVectorizer(stop_words = "english",vocabulary = tf_transformer.vocabulary_)
    
    # int_features = [int(x) for x in request.form.values()]
    # final_features = [np.array(int_features)]
    feature = list(request.form['text'])
    feature_vect = tfidf.fit_transform(feature)

    prediction = model.predict(feature_vect)[0]
    if prediction == 0:
        output = "Not from USA"
    else:
        output = "From USA"

    return render_template('index.html', prediction_text='Twitter: {}'.format(output))

# @app.route('/results',methods=['POST'])
# def results():

#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)