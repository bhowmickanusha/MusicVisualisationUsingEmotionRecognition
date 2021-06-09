import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
def get_csv_data():
    read_file = pd.read_excel (r"E:\Sem V\Research paper\FinalImplementation\datamodel1.xlsx")
    read_file.to_csv (r"E:\Sem V\Research paper\FinalImplementation\datamodel1.csv",  
                  index = None, 
                  header=True)
    

def split_dataset():
    from sklearn.model_selection import train_test_split
    data = pd.read_csv(r"E:\Sem V\Research paper\FinalImplementation\datamodel1.csv")
    data.info()
    #all_X=data.iloc[:, 1:9]
    #all_y=data.emotionclass
    data.emotionclass.value_counts()
    train, test = train_test_split(data, test_size = 0.3,random_state=1234)
    print(train.shape)
    print(test.shape)
    train_X = train.iloc[:, 1:9]
    train_y=train.emotionclass
    test_X= test.iloc[:, 1:9]
    test_y =test.emotionclass
    print(train_X.shape)
    print(train_y.shape)
    print(test_X.shape)
    print(test_y.shape)
    return train_X,train_y,test_X,test_y



def get_split_trained_model():
    train_X,train_y,test_X,test_y=split_dataset()
    modelrf=RandomForestClassifier()
    params = {'criterion':['gini','entropy'],
          'n_estimators':[10,15,20,25,30,35],
          'min_samples_leaf':[1,2,3],
          'min_samples_split':[3,4,5,6,7,10], 
          'random_state':[123],
          'n_jobs':[-1]}
    modelrf1 = GridSearchCV(modelrf, param_grid=params, n_jobs=-1)
    modelrf1.fit(train_X,train_y)
    print("Best Hyper Parameters:\n",modelrf1.best_params_)
    predict_model_accuracy(modelrf1,test_X,test_y)
    return modelrf1

def predict_model_accuracy(modelrf1,test_X,test_y):
    prediction=modelrf1.predict(test_X)    
    print("Accuracy:",metrics.accuracy_score(prediction,test_y))
    print("Confusion Metrix:\n",metrics.confusion_matrix(prediction,test_y))

'''
def get_final_model():
    all_X,all_y,train_X,train_y,test_X,test_y=split_dataset()
    model=RandomForestClassifier()
    params = {'criterion':['gini','entropy'],
          'n_estimators':[10,15,20,25,30],
          'min_samples_leaf':[1,2,3],
          'min_samples_split':[3,4,5,6,7], 
          'random_state':[123],
          'n_jobs':[-1]}
    modelrf = GridSearchCV(model, param_grid=params, n_jobs=-1)
    #modelrf.fit(all_X,all_y)
    print("Best Hyper Parameters:\n",modelrf.best_params_)
    return modelrf
'''
