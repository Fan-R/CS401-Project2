import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
    date = pickle.load(f)

tf_transformer = pickle.load(open('tfidf1.pkl','rb'))

@app.route('/api/american',methods=['POST'])
def predict():
    tfidf = TfidfVectorizer(stop_words = "english",vocabulary = tf_transformer.vocabulary_)

    data = request.get_json(force=True)
    feature = list(data['text'])
    feature_vect = tfidf.fit_transform(feature)

    prediction = model.predict(feature_vect)[0]
    version = "1.0"
    # model_date = "XXX"

    return jsonify({"is_american ":int(prediction),"version":version,"model_date":date})

if __name__ == "__main__":
    app.run(debug=True)