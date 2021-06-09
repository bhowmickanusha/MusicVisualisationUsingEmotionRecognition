import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

def get_csv_data():
    read_file = pd.read_excel (r"E:\Sem V\Research paper\FinalImplementation\datamodel2.xlsx")
    read_file.to_csv (r"E:\Sem V\Research paper\FinalImplementation\datamodel2.csv",  
                  index = None, 
                  header=True)

def split_dataset():
    data = pd.read_csv(r"E:\Sem V\Research paper\FinalImplementation\datamodel2.csv")
    data.info()
    data.classtype2.value_counts()
    train, test = train_test_split(data, test_size = 0.3,random_state=1234)
    print(train.shape)
    print(test.shape)
    train_X = train.iloc[:, 1:4]
    train_y=train.classtype2
    test_X= test.iloc[:, 1:9]
    test_y =test.classtype2
    print(train_X.shape)
    print(train_y.shape)
    print(test_X.shape)
    print(test_y.shape)
    return train_X,train_y,test_X,test_y

def get_split_trained_model():
    train_X,train_y,test_X,test_y=split_dataset()
    modelrf=RandomForestClassifier()
    params = {'criterion':['gini','entropy'],
          'n_estimators':[10,15,20,25,30],
          'min_samples_leaf':[1,2,3],
          'min_samples_split':[3,4,5,6,7], 
          'random_state':[123],
          'n_jobs':[-1]}
    modelrf2 = GridSearchCV(modelrf, param_grid=params, n_jobs=-1)
    modelrf2.fit(train_X,train_y)
    print("Best Hyper Parameters:\n",modelrf2.best_params_)
    predict_model_accuracy(modelrf2,test_X,test_y)
    return modelrf2

def predict_model_accuracy(modelrf2,test_X,test_y):
    prediction=modelrf2.predict(test_X)
    print("Accuracy:",metrics.accuracy_score(prediction,test_y))
    print("Confusion Metrix:\n",metrics.confusion_matrix(prediction,test_y))
