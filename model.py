import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
from datetime import datetime

today = datetime.now()
print("Today's date:", today)

# load the training and test dataset
df_train = pd.read_csv('training.csv',sep = ';')
df_test = pd.read_csv('test.csv',sep = ';')

# extrat X and y from the dataset
train = df_train[['text','country_code']].copy()
train['is_US'] = 0
train.loc[train['country_code'] == 'US','is_US']=1

test = df_test[['text','country_code']].copy()
test['is_US'] = 0
test.loc[test['country_code'] == 'US','is_US']=1

y_train = train['is_US']
y_test = test['is_US']

# clean the text data and transfer it into a vector
TF_vectorizer = TfidfVectorizer(stop_words='english')
X_train = TF_vectorizer.fit_transform(train['text'])
print(X_train.shape)
X_test = TF_vectorizer.transform(test['text'])
print(X_test.shape)

# save the tfidf tranformer for later uage
pickle.dump(TF_vectorizer, open("tfidf1.pkl", "wb"))


# logistic regression model 
clf = LogisticRegression(random_state=0).fit(X_train,y_train)
print("train acc is {}".format(clf.score(X_train,y_train)))
print("test acc is {}".format(clf.score(X_test,y_test)))

# save the model
with open('model.pkl','wb') as f:
    pickle.dump(clf, f)
    pickle.dump(today,f)

