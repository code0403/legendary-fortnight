import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

student_db = pd.read_csv("students.csv")
# print(student_db.shape)
# print(student_db)
student_db = student_db.drop_duplicates()
# print(student_db)
# student_db = student_db.isnull().sum()
# print(student_db)
# student_db = pd.DataFrame(student_db).drop(['gender'], axis=0)
student_db = student_db.drop(['gender'], axis=1)
student_db = student_db.drop(['age'], axis=1)
student_db.isnull().sum()
# print(student_db)

tot_students = len(student_db.index)
tot_features = len(student_db.columns)
# print(tot_students, tot_features)


list_var = []
Y1=[]

for a1 in range (0,tot_features,1) :
    Y1=[]
    Y1.append(student_db.iloc[:,[a1]].values)
    v1=np.var(Y1)
    list_var.append(v1)
list_var.remove(list_var[0])
list_var.remove(list_var[0])

# print(f"\nVariance List : \n{list_var}\n")

feat=[]
for a3 in range (2, tot_features, 1) :
    feat.append(a3)


plt.plot(feat,list_var,color='blue', linestyle='dashed', linewidth = 2,
marker='o', markerfacecolor='red', markersize=8)
plt.xlabel('Feature IDs')
plt.ylabel('Feature Variance')
plt.title('Feature Selection based on Variance')
plt.show()



g = sns.PairGrid(student_db.loc[:,["gradyear","NumberOffriends","basketball","football","soccer","softball","volleyball","baseball","tennis"]])
#g =sns.PairGrid(student_db.loc[:,["gradyear","NumberOffriends","Gender","dance","music","god","blonde"]])
#"step", which means the histogram will be drawn as a line plot.
g.map_diag(plt.hist, histtype="step", linewidth=3) # Diagonal subplots represent thedistribution of each individual variable.
g.map_offdiag(plt.scatter) #Off-diagonal subplots represent the relationship between pairs ofvariables.
delay=0
while delay<2000 :
    delay=delay+1

plt.show()


