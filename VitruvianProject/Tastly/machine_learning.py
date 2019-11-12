import pandas as pd
import numpy as np
#import xgboost as xgb
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.model_selection import cross_val_score, KFold
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Simulate database
#df = pd.read_csv("Tastly (Responses) - Form Responses 1.csv")
#df.set_axis(['gender', 'age', 'country', 'music', 'beverage', 'smoke'], axis=1, inplace=True)
# Function to generate predictions from user input    
def feature_predict(user_input, df, feat):
    
    feature = df[feat].copy()
    age = df['age'].copy()
    categ_X = df.drop(columns=[feat, 'age']) 
    agg_categ_X = categ_X.append(user_input, ignore_index=True).drop(columns=['age'])
    
    enc_X = pd.get_dummies(agg_categ_X, drop_first=True)
    
    sc = StandardScaler()
    age = sc.fit_transform(np.array(age).reshape(-1, 1))
    user_age = sc.transform(np.array(user_input['age']).reshape(1, -1))
    
    ml_user_input = pd.DataFrame(enc_X.iloc[-1, :]).transpose()
    ml_user_input['age'] = user_age[0][0]
    
    enc_X.drop(df.tail(1).index,inplace=True)
    enc_X['age'] = age
    
    y = feature
    X = enc_X
    
    classifier = RandomForestClassifier(n_estimators=200)
    classifier.fit(X, y)
    
    feature_pred = classifier.predict(ml_user_input)
    
    return feature_pred[0]