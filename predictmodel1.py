import RFclassifiermodel1 as mdl1

import getfilename as fn
import xlrd
import csv
import pandas as pd

inputfile=fn.get_filename()
print(inputfile)
f = open(r"E:\Sem V\Research paper\FinalImplementation\FAudioWaveform\data\audiofilename.txt", 'w+')
f.write(str(inputfile))
f.close()

df1 = pd.read_csv(r"E:\Sem V\Research paper\FinalImplementation\newdatamodel1.csv")
rows=df1.shape[0]
#print(rows)
#print(df._get_value(0,0,takeable=True))
for i in range(rows): 
    if(df1._get_value(i,0,takeable=True)==inputfile):
        features1=df1.iloc[i,1:9]
        break
print(features1)
features1=features1.values.reshape(1,-1)
#print(features1.shape)

model1=mdl1.get_split_trained_model()
predictedclass1=str(model1.predict(features1))
print("Valence class is:",predictedclass1)

f = open(r"E:\Sem V\Research paper\FinalImplementation\emotionclassmodel1.txt", 'w')
f.write(predictedclass1) # could be write(), read(), readline(), etc...
f.close()


'''
df2 = pd.read_csv(r"E:\Sem V\Research paper\FinalImplementation\newdatamodel1.csv")
rows=df2.shape[0]
print(rows)
#print(df._get_value(0,0,takeable=True))
for i in range(rows): 
    if(df2._get_value(i,0,takeable=True)==inputfile):
        features2=df2.iloc[i,1:4]
        break
print(features2)
features2=features2.values.reshape(1,-1)
print(features2.shape)

model2=mdl2.get_final_model()
predictedclass2=model2.predict(features2)
print(predictedclass2)

f = open(r"E:\Sem V\Research paper\FinalImplementation\emotionclassmodel2.txt", 'w+')
f.write(*predictedclass2) # could be write(), read(), readline(), etc...
f.close()
'''
