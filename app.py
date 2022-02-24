import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Flask, request, jsonify,render_template,url_for
import pickle

app = Flask(__name__)
version = "4.1"

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
    date = pickle.load(f)

tf_transformer = pickle.load(open('tfidf1.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

# for CLI
@app.route('/api/american',methods=['POST'])
def predict():
    tfidf = TfidfVectorizer(stop_words = "english",vocabulary = tf_transformer.vocabulary_)

    data = request.get_json(force=True)
    feature = [data['text']]
    feature_vect = tfidf.fit_transform(feature)

    prediction = model.predict(feature_vect)[0]

    return jsonify({"is_american ":int(prediction),"version":version,"model_date":date})

# front-end version
@app.route('/api/american/html',methods=['POST'])
def html_predict():
    tfidf = TfidfVectorizer(stop_words = "english",vocabulary = tf_transformer.vocabulary_)
    feature = [request.form['text']]
    feature_vect = tfidf.fit_transform(feature)
    prediction = model.predict(feature_vect)[0]

    return render_template('index.html', prediction="is_american: {}".format(prediction),version = "version: {}".format(version),date = "model_date: {}".format(date))

if __name__ == "__main__":
    app.run(debug=True)