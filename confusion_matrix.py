import pandas as pd
from sklearn.metrics import confusion_matrix
import seaborn as sns
import  matplotlib.pyplot  as plt 
from sklearn.metrics import accuracy_score
from sklearn.metrics import  precision_score

data=pd.read_excel("test.xlsx")

predictions=data["prediction"].values
truth=data["truth"].values

cm=confusion_matrix(truth,predictions,labels=["fresh","rotten"])

plt.figure(figsize=(5,5))
sns.heatmap(cm,annot=True,xticklabels=["fresh","rotten"],yticklabels=["fresh","rotten"])

print( accuracy_score(truth,predictions))

print(precision_score(truth,predictions,pos_label="fresh"),precision_score(truth,predictions,pos_label="rotten"))

plt.show()