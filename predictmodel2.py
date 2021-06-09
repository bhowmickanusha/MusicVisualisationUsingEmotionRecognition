import RFclassifiermodel2 as mdl2

import getfilename as fn
import csv
import pandas as pd

inputfile=fn.get_filename()
print(inputfile)
f = open(r"E:\Sem V\Research paper\FinalImplementation\FAudioWaveform\data\audiofilename.txt", 'w+')
f.write(str(inputfile))
f.close()

df2 = pd.read_csv(r"E:\Sem V\Research paper\FinalImplementation\newdatamodel2.csv")
rows=df2.shape[0]
#print(rows)
for i in range(rows): 
    if(df2._get_value(i,0,takeable=True)==inputfile):
        features2=df2.iloc[i,1:4]
        break
print(features2)
features2=features2.values.reshape(1,-1)
#print(features2.shape)

model2=mdl2.get_split_trained_model()

predictedclass2=model2.predict(features2)
print("Arousal class is: ",predictedclass2)
f = open(r"E:\Sem V\Research paper\FinalImplementation\emotionclassmodel2.txt", 'w+')
f.write(str(predictedclass2))
# could be write(), read(), readline(), etc...
f.close()
