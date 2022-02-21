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

@app.route('/api/american',methods=['POST'])
def predict():
    tfidf = TfidfVectorizer(stop_words = "english",vocabulary = tf_transformer.vocabulary_)
    feature = list(request.form['text'])
    feature_vect = tfidf.fit_transform(feature)

    prediction = model.predict(feature_vect)[0]
    version = "1.0"
    model_date = "XXX"
    return render_template('index.html', prediction_text="is_american: {} \n version: {} \n model_date: {}".format(prediction,version,model_date))

if __name__ == "__main__":
    app.run(debug=True)