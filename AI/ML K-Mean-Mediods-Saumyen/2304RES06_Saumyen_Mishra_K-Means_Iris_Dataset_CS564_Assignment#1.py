#********************************************************************************************************************************************************************************************************************************
#Importing CSV & Converting to dataframe
#********************************************************************************************************************************************************************************************************************************

import pandas as pd
import matplotlib.pyplot as plt
import math

url="https://raw.githubusercontent.com/SaumyenMishraIITP/iris/main/Iris.csv" # raw-github-link
df=pd.read_csv(url)                                                          # converting csv to dataframe
df=df.drop(['Id'], axis=1)                                                   # removing the column 'Id'

#print (df)
#print(df.index[0])
#print(df.columns[3])

tot_rows=len(df.index)                                                       # Counting no. of rows in dataframe
tot_cols=len(df.columns)                                                     # Counting no. of columns in dataframe

#********************************************************************************************************************************************************************************************************************************
#Exploratory data analysis
#********************************************************************************************************************************************************************************************************************************

n_setosa=0
n_versicolor=0
n_virginica=0

sum_setosa_sep_len=0
sum_setosa_sep_wid=0
sum_setosa_pet_len=0
sum_setosa_pet_wid=0

sum_versicolor_sep_len=0
sum_versicolor_sep_wid=0
sum_versicolor_pet_len=0
sum_versicolor_pet_wid=0

sum_virginica_sep_len=0
sum_virginica_sep_wid=0
sum_virginica_pet_len=0
sum_virginica_pet_wid=0

for i in range(0,tot_rows,1) :
  if  (df.iat[i,4]=="Iris-setosa") :
    df.iat[i,4] = 0
    n_setosa = n_setosa+1

    sum_setosa_sep_len = sum_setosa_sep_len + df.iat[i,0]
    sum_setosa_sep_wid= sum_setosa_sep_wid + df.iat[i,1]
    sum_setosa_pet_len = sum_setosa_pet_len + df.iat[i,2]
    sum_setosa_pet_wid = sum_setosa_pet_wid + df.iat[i,3]

  elif  (df.iat[i,4]=="Iris-versicolor") :
    df.iat[i,4] = 1
    n_versicolor = n_versicolor+1

    sum_versicolor_sep_len = sum_versicolor_sep_len + df.iat[i,0]
    sum_versicolor_sep_wid= sum_versicolor_sep_wid + df.iat[i,1]
    sum_versicolor_pet_len = sum_versicolor_pet_len + df.iat[i,2]
    sum_versicolor_pet_wid = sum_versicolor_pet_wid + df.iat[i,3]

  elif (df.iat[i,4]=="Iris-virginica") :
      df.iat[i,4] = 2
      n_virginica = n_virginica+1

      sum_virginica_sep_len = sum_virginica_sep_len + df.iat[i,0]
      sum_virginica_sep_wid = sum_virginica_sep_wid + df.iat[i,1]
      sum_virginica_pet_len = sum_virginica_pet_len + df.iat[i,2]
      sum_virginica_pet_wid = sum_virginica_pet_wid + df.iat[i,3]


mean_setosa_sep_len = sum_setosa_sep_len/n_setosa
mean_setosa_sep_wid = sum_setosa_sep_wid/n_setosa
mean_setosa_pet_len = sum_setosa_pet_len/n_setosa
mean_setosa_pet_wid = sum_setosa_pet_wid/n_setosa

mean_versicolor_sep_len = sum_versicolor_sep_len/n_versicolor
mean_versicolor_sep_wid = sum_versicolor_sep_wid/n_versicolor
mean_versicolor_pet_len = sum_versicolor_pet_len/n_versicolor
mean_versicolor_pet_wid = sum_versicolor_pet_wid/n_versicolor

mean_virginica_sep_len = sum_virginica_sep_len/n_virginica
mean_virginica_sep_wid = sum_virginica_sep_wid/n_virginica
mean_virginica_pet_len = sum_virginica_pet_len/n_virginica
mean_virginica_pet_wid = sum_virginica_pet_wid/n_virginica

initial_centroids=[[mean_setosa_sep_len,mean_setosa_sep_wid,mean_setosa_pet_len,mean_setosa_pet_wid], [mean_versicolor_sep_len,mean_versicolor_sep_wid,mean_versicolor_pet_len,mean_versicolor_pet_wid], [mean_virginica_sep_len,mean_virginica_sep_wid,mean_virginica_pet_len,mean_virginica_pet_wid]]


#print(f"\n{mean_setosa_sep_len}\n{mean_setosa_sep_wid}\n{mean_setosa_pet_len}\n{mean_setosa_pet_wid}")
#print(f"\n{mean_versicolor_sep_len}\n{mean_versicolor_sep_wid}\n{mean_versicolor_pet_len}\n{mean_versicolor_pet_wid}")
#print(f"\n{mean_virginica_sep_len}\n{mean_virginica_sep_wid}\n{mean_virginica_pet_len}\n{mean_virginica_pet_wid}")

#print (df)

#********************************************************************************************************************************************************************************************************************************
#SCATTER PLOT OF ORIGINAL DATASET
#********************************************************************************************************************************************************************************************************************************
sepallen=[]
sepalwid=[]
petallen=[]
petalwid=[]
sepallen_X_petallen=[]
sepalwid_X_petalwid=[]

for p in range(0, len(df.index), 1) :
  sepallen.append(df.iat[p,0])
  sepalwid.append(df.iat[p,1])
  petallen.append(df.iat[p,2])
  petalwid.append(df.iat[p,3])
  sepallen_X_petallen.append(((7*df.iat[p,0]) + (3*df.iat[p,2])))
  sepalwid_X_petalwid.append(((11*(df.iat[p,1])) + (df.iat[p,3])))

plt.scatter(sepallen,sepalwid, c='green')
plt.xlabel('sepal length in cm')
plt.ylabel('sepal width in cm')
plt.title('Raw-data')
plt.show()

plt.scatter(petallen,petalwid,c='magenta')
plt.xlabel('Petal length in cm')
plt.ylabel('Petal width in cm')
plt.title('Raw-data')
plt.show()

plt.scatter(sepallen,petallen,c='cyan')
plt.xlabel('Sepal length in cm')
plt.ylabel('Petal length in cm')
plt.title('Raw-data')
plt.show()

plt.scatter(sepallen,petalwid,c='yellow')
plt.xlabel('Sepal length in cm')
plt.ylabel('Petal width in cm')
plt.title('Raw-data')
plt.show()

plt.scatter(sepalwid,petalwid,c='blue')
plt.xlabel('Sepal width in cm')
plt.ylabel('Petal width in cm')
plt.title('Raw-data')
plt.show()

plt.scatter(sepalwid,petallen,c='black')
plt.xlabel('Sepal width in cm')
plt.ylabel('Petal length in cm')
plt.title('Raw-data')
plt.show()

plt.scatter(sepallen_X_petallen,sepalwid_X_petalwid,c='red')
plt.xlabel('Linear Sum of Sepal & Petal lengths in cm')
plt.ylabel('Linear Sum  of Sepal & Petal widths in cm')
plt.title('Raw-data')
plt.show()

#********************************************************************************************************************************************************************************************************************************
#Centroid Function, SSE calculation Function, K-Means Assignment function, K-Means-Iris Function
#********************************************************************************************************************************************************************************************************************************

#old_centroids_with_cluster=[[0,mean_setosa_sep_len,mean_setosa_sep_wid,mean_setosa_pet_len,mean_setosa_pet_wid], [1,mean_versicolor_sep_len,mean_versicolor_sep_wid,mean_versicolor_pet_len,mean_versicolor_pet_wid], [2,mean_virginica_sep_len,mean_virginica_sep_wid,mean_virginica_pet_len,mean_virginica_pet_wid]]

def centroid_calc_function (cluster) :
  R=len(cluster.index)
  C=len(cluster.columns)

  sum1=[]
  centroid_coordinates=[]

  for i in range (0,C-1,1) :
    sum1.append(0)
    centroid_coordinates.append(0)

  for j in range (0,R,1) :
    for k in range(0,C-1,1) :
      sum1[k] = sum1[k] + cluster.iat[j,k]

  for m in range (0,C-1,1) :
    if (R!=0) :
      centroid_coordinates[m]=sum1[m]/R
    else :
      break

  #print("\nEmpty Clusters do not have a defined centroid")

  #print (centroid_coordinates)

  return centroid_coordinates

#***********************************************************************************************************************************************************************************************************************************
#***********************************************************************************************************************************************************************************************************************************

def SSE(cluster) :

  rows_1 = len(cluster.index)

  if (rows_1 == 0) :
    print("Empty Clusters do not have a defined SSE")

  else :
    cen = centroid_calc_function(cluster)
    SSE_Cluster=0

    for i in range (0,rows_1,1) :
      SSE_Cluster = SSE_Cluster + (((cen[0]-cluster.iat[i,0])**2) + ((cen[1]-cluster.iat[i,1])**2) + ((cen[2]-cluster.iat[i,2])**2) + ((cen[3]-cluster.iat[i,3])**2))

  return SSE_Cluster

#***********************************************************************************************************************************************************************************************************************************
#***********************************************************************************************************************************************************************************************************************************

def assignment_function(centroids,dataset) :

  num_rows = len(dataset.index)
  num_cols = len(dataset.columns)

  k1=0
  k2=0
  k3=0

  dist1=[]
  dist2=[]
  dist3=[]

  for i in range(0,num_rows,1) :
    k1=math.sqrt(((centroids[0][0] - dataset.iat[i,0])**2) + ((centroids[0][1] - dataset.iat[i,1])**2) + ((centroids[0][2] - dataset.iat[i,2])**2) + ((centroids[0][3] - dataset.iat[i,3])**2))
    dist1.append(k1)

    k2=math.sqrt(((centroids[1][0] - dataset.iat[i,0])**2) + ((centroids[1][1] - dataset.iat[i,1])**2) + ((centroids[1][2] - dataset.iat[i,2])**2) + ((centroids[1][3] - dataset.iat[i,3])**2))
    dist2.append(k2)

    k3=math.sqrt(((centroids[2][0] - dataset.iat[i,0])**2) + ((centroids[2][1] - dataset.iat[i,1])**2) + ((centroids[2][2] - dataset.iat[i,2])**2) + ((centroids[2][3] - dataset.iat[i,3])**2))
    dist3.append(k3)

  list0=[]
  list1=[]
  list2=[]

  for j in range (0,num_rows,1) :
    if (min(dist1[j],dist2[j],dist3[j])==dist1[j]) :
      a0_0=dataset.iat[j,0]
      a0_1=dataset.iat[j,1]
      a0_2=dataset.iat[j,2]
      a0_3=dataset.iat[j,3]
      a0_4=dataset.iat[j,4]
      a0=[a0_0, a0_1, a0_2, a0_3, a0_4]
      list0.append(a0)

    elif (min(dist1[j],dist2[j],dist3[j])==dist2[j]) :
      a1_0=dataset.iat[j,0]
      a1_1=dataset.iat[j,1]
      a1_2=dataset.iat[j,2]
      a1_3=dataset.iat[j,3]
      a1_4=dataset.iat[j,4]
      a1=[a1_0, a1_1, a1_2, a1_3,a1_4]
      list1.append(a1)

    elif (min(dist1[j],dist2[j],dist3[j])==dist3[j]) :
      a2_0=dataset.iat[j,0]
      a2_1=dataset.iat[j,1]
      a2_2=dataset.iat[j,2]
      a2_3=dataset.iat[j,3]
      a2_4=dataset.iat[j,4]
      a2=[a2_0, a2_1, a2_2, a2_3, a2_4]
      list2.append(a2)

  cluster0 = pd.DataFrame (list(list0), columns=["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm","Species"])

  cluster1 = pd.DataFrame (list(list1), columns=["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm","Species"])

  cluster2 = pd.DataFrame (list(list2), columns=["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm","Species"])

  centroid_cluster0 = centroid_calc_function(cluster0)
  centroid_cluster1 = centroid_calc_function(cluster1)
  centroid_cluster2 = centroid_calc_function(cluster2)

  new_iteration_centroids = [centroid_cluster0,centroid_cluster1,centroid_cluster2]

  #print(new_iteration_centroids)
  #print (f"\nIris-Setosa cluster looks like :\n\n{cluster0}\n\n")
  #print (f"\nIris-Versicolor cluster looks like :\n\n{cluster1}\n\n")
  #print (f"\nIris-Virginica cluster looks like :\n\n{cluster2}\n\n")
  #cluster0, cluster1, cluster2, new_iteration_centroids

  return cluster0, cluster1, cluster2, new_iteration_centroids

#***********************************************************************************************************************************************************************************************************************************
#***********************************************************************************************************************************************************************************************************************************

def kmeans_iris(ini_centroids,dataset) :

  K=3
  Last_iteration_centroids = ini_centroids
  Iterations=0

  while 1:

    Iterations = Iterations+1
    print(f"\nIteration Number : {Iterations}\n")

    [C_0, C_1, C_2, New_iteration_centroids] = assignment_function(Last_iteration_centroids,dataset)
    len_C_0 = len(C_0.index)
    len_C_1 = len(C_1.index)
    len_C_2 = len(C_2.index)

    #print ()

    if(New_iteration_centroids==Last_iteration_centroids and len_C_0!=0 and len_C_1!=0 and len_C_2!=0) :
      print("\n\n**************************************************************************************************************************************************************************************************")
      print("\n**************************************************************************************************************************************************************************************************")
      print("\nCASE: 1 COMMON\n")

      print(f"\n\nConvergence Achieved in the K-Means Clustering Algorithm!!!\n\nTotal Number of Iterations : {Iterations}\n\nTotal Number of Clusters : {K}\n\nTotal Number of Points in First Cluster : {len(C_0.index)}\n\nSSE for the First Cluster : {SSE(C_0)} cm.Sq.\n\nTotal Number of Points in Second Cluster : {len(C_1.index)}\n\nSSE for the Second Cluster : {SSE(C_1)} cm.Sq.\n\nTotal Number of Points in Third Cluster : {len(C_2.index)}\n\nSSE for the Third Cluster : {SSE(C_2)} cm.Sq.\n\nTotal SSE for the finalized 3-Cluster-System : {SSE(C_0) + SSE(C_1) + SSE(C_2)} cm.Sq.\n\n")
      print (New_iteration_centroids)

      
      setosa_C0=0
      versicolor_C0=0
      virginica_C0=0

      for i1 in range (0,len_C_0,1) :
        if (C_0.iat[i1,4]=="Iris-setosa") :
          setosa_C0=setosa_C0+1
        elif (C_0.iat[i1,4]=="Iris-versicolor") :
          versicolor_C0=versicolor_C0+1
        elif (C_0.iat[i1,4]=="Iris-virginica") :
          virginica_C0=virginica_C0+1
        
      print(f"\n\nIn Cluster 0, the number of elements from :\na.)CLASS SETOSA : {setosa_C0}\nb.)CLASS VERSICOLOR : {versicolor_C0}\nc.)CLASS VIRGINICA : {virginica_C0}")
      C0_Entropy_Setosa=0
      C0_Entropy_Versicolor=0
      C0_Entropy_Virginica=0
      C0_Entropy=0

      if(setosa_C0>0) :
        C0_Entropy_Setosa=-1*(setosa_C0/n_setosa)*(math.log2(setosa_C0/n_setosa))
      elif(setosa_C0==0) :
        C0_Entropy_Setosa=0

      if(versicolor_C0>0) :
        C0_Entropy_Versicolor=-1*(versicolor_C0/n_versicolor)*(math.log2(versicolor_C0/n_versicolor))
      elif(versicolor_C0==0) :
        C0_Entropy_Versicolor=0
      
      if(virginica_C0>0) :
        C0_Entropy_Virginica=-1*(virginica_C0/n_virginica)*(math.log2(virginica_C0/n_virginica))
      elif(virginica_C0==0) :
        C0_Entropy_Virginica=0
      
      C0_Entropy = C0_Entropy_Setosa + C0_Entropy_Versicolor + C0_Entropy_Virginica
      print(f"Shannon's Entropy for Cluster 0 is : {C0_Entropy}\n\n")

      
      setosa_C1=0
      versicolor_C1=0
      virginica_C1=0

      for i2 in range (0,len_C_1,1) :
        if (C_1.iat[i2,4]=="Iris-setosa") :
          setosa_C1=setosa_C1+1
        elif (C_1.iat[i2,4]=="Iris-versicolor") :
          versicolor_C1=versicolor_C1+1
        elif (C_1.iat[i2,4]=="Iris-virginica") :
          virginica_C1=virginica_C1+1
        
      print(f"\n\nIn Cluster 1, the number of elements from :\na.)CLASS SETOSA : {setosa_C1}\nb.)CLASS VERSICOLOR : {versicolor_C1}\nc.)CLASS VIRGINICA : {virginica_C1}")
      C1_Entropy_Setosa=0
      C1_Entropy_Versicolor=0
      C1_Entropy_Virginica=0
      C1_Entropy=0

      if(setosa_C1>0) :
        C1_Entropy_Setosa=-1*(setosa_C1/n_setosa)*(math.log2(setosa_C1/n_setosa))
      elif(setosa_C1==0) :
        C1_Entropy_Setosa=0

      if(versicolor_C1>0) :
        C1_Entropy_Versicolor=-1*(versicolor_C1/n_versicolor)*(math.log2(versicolor_C1/n_versicolor))
      elif(versicolor_C1==0) :
        C1_Entropy_Versicolor=0
      
      if(virginica_C1>0) :
        C1_Entropy_Virginica=-1*(virginica_C1/n_virginica)*(math.log2(virginica_C1/n_virginica))
      elif(virginica_C1==0) :
        C1_Entropy_Virginica=0
      
      C1_Entropy = C1_Entropy_Setosa + C1_Entropy_Versicolor + C1_Entropy_Virginica
      print(f"Shannon's Entropy for Cluster 1 is : {C1_Entropy}\n\n")

      
      setosa_C2=0
      versicolor_C2=0
      virginica_C2=0

      for i3 in range (0,len_C_2,1) :
        if (C_2.iat[i3,4]=="Iris-setosa") :
          setosa_C2=setosa_C2+1
        elif (C_2.iat[i3,4]=="Iris-versicolor") :
          versicolor_C2=versicolor_C2+1
        elif (C_2.iat[i3,4]=="Iris-virginica") :
          virginica_C2=virginica_C2+1
        
      print(f"\n\nIn Cluster 2, the number of elements from :\na.)CLASS SETOSA : {setosa_C2}\nb.)CLASS VERSICOLOR : {versicolor_C2}\nc.)CLASS VIRGINICA : {virginica_C2}")
      
      C2_Entropy_Setosa=0
      C2_Entropy_Versicolor=0
      C2_Entropy_Virginica=0
      C2_Entropy=0

      if(setosa_C2>0) :
        C2_Entropy_Setosa=-1*(setosa_C2/n_setosa)*(math.log2(setosa_C2/n_setosa))
      elif(setosa_C2==0) :
        C2_Entropy_Setosa=0

      if(versicolor_C2>0) :
        C2_Entropy_Versicolor=-1*(versicolor_C2/n_versicolor)*(math.log2(versicolor_C2/n_versicolor))
      elif(versicolor_C2==0) :
        C2_Entropy_Versicolor=0
      
      if(virginica_C2>0) :
        C2_Entropy_Virginica=-1*(virginica_C2/n_virginica)*(math.log2(virginica_C2/n_virginica))
      elif(virginica_C2==0) :
        C2_Entropy_Virginica=0
      
      C2_Entropy = C2_Entropy_Setosa + C2_Entropy_Versicolor + C2_Entropy_Virginica
      print(f"Shannon's Entropy for Cluster 2 is : {C2_Entropy}\n\n")


      sepallen_C_0=[]
      sepallen_C_1=[]
      sepallen_C_2=[]

      sepalwid_C_0=[]
      sepalwid_C_1=[]
      sepalwid_C_2=[]

      petallen_C_0=[]
      petallen_C_1=[]
      petallen_C_2=[]

      petalwid_C_0=[]
      petalwid_C_1=[]
      petalwid_C_2=[]

      sepallen_X_petallen_C_0=[]
      sepallen_X_petallen_C_1=[]
      sepallen_X_petallen_C_2=[]

      sepalwid_X_petalwid_C_0=[]
      sepalwid_X_petalwid_C_1=[]
      sepalwid_X_petalwid_C_2=[]

      for z in range (0,len(C_0.index),1) :
        sepallen_C_0.append(C_0.iat[z,0])
        sepalwid_C_0.append(C_0.iat[z,1])
        petallen_C_0.append(C_0.iat[z,2])
        petalwid_C_0.append(C_0.iat[z,3])
        sepallen_X_petallen_C_0.append(((7*C_0.iat[z,0])) + (3*C_0.iat[z,2]))
        sepalwid_X_petalwid_C_0.append((11*C_0.iat[z,1]) + (C_0.iat[z,3]))

      for y in range (0,len(C_1.index),1) :
        sepallen_C_1.append(C_1.iat[y,0])
        sepalwid_C_1.append(C_1.iat[y,1])
        petallen_C_1.append(C_1.iat[y,2])
        petalwid_C_1.append(C_1.iat[y,3])
        sepallen_X_petallen_C_1.append(((7*C_1.iat[y,0])) + (3*C_1.iat[y,2]))
        sepalwid_X_petalwid_C_1.append((11*C_1.iat[y,1]) + (C_1.iat[y,3]))

      for x in range (0,len(C_2.index),1) :
        sepallen_C_2.append(C_2.iat[x,0])
        sepalwid_C_2.append(C_2.iat[x,1])
        petallen_C_2.append(C_2.iat[x,2])
        petalwid_C_2.append(C_2.iat[x,3])
        sepallen_X_petallen_C_2.append(((7*C_2.iat[x,0])) + (3*C_2.iat[x,2]))
        sepalwid_X_petalwid_C_2.append((11*C_2.iat[x,1]) + (C_2.iat[x,3]))

      plt.scatter(sepallen_C_0,sepalwid_C_0, c='green')
      plt.scatter(sepallen_C_1,sepalwid_C_1, c='blue')
      plt.scatter(sepallen_C_2,sepalwid_C_2, c='red')
      plt.xlabel('sepal length in cm')
      plt.ylabel('sepal width in cm')
      plt.title('Clusterings')
      plt.show()

      plt.scatter(petallen_C_0,petalwid_C_0, c='green')
      plt.scatter(petallen_C_1,petalwid_C_1, c='blue')
      plt.scatter(petallen_C_2,petalwid_C_2, c='red')
      plt.xlabel('petal length in cm')
      plt.ylabel('petal width in cm')
      plt.title('Clusterings')
      plt.show()

      plt.scatter(sepallen_C_0,petallen_C_0, c='green')
      plt.scatter(sepallen_C_1,petallen_C_1, c='blue')
      plt.scatter(sepallen_C_2,petallen_C_2, c='red')
      plt.xlabel('sepal length in cm')
      plt.ylabel('petal length in cm')
      plt.title('Clusterings')
      plt.show()

      plt.scatter(sepallen_C_0,petalwid_C_0, c='green')
      plt.scatter(sepallen_C_1,petalwid_C_1, c='blue')
      plt.scatter(sepallen_C_2,petalwid_C_2, c='red')
      plt.xlabel('sepal length in cm')
      plt.ylabel('petal width in cm')
      plt.title('Clusterings')
      plt.show()

      plt.scatter(sepalwid_C_0,petalwid_C_0, c='green')
      plt.scatter(sepalwid_C_1,petalwid_C_1, c='blue')
      plt.scatter(sepalwid_C_2,petalwid_C_2, c='red')
      plt.xlabel('sepal width in cm')
      plt.ylabel('petal width in cm')
      plt.title('Clusterings')
      plt.show()

      
      plt.scatter(sepalwid_C_0,petallen_C_0, c='green')
      plt.scatter(sepalwid_C_1,petallen_C_1, c='blue')
      plt.scatter(sepalwid_C_2,petallen_C_2, c='red')
      plt.xlabel('sepal width in cm')
      plt.ylabel('petal length in cm')
      plt.title('Clusterings')
      plt.show()

      plt.scatter(sepallen_X_petallen_C_0,sepalwid_X_petalwid_C_0, c='green')
      plt.scatter(sepallen_X_petallen_C_1,sepalwid_X_petalwid_C_1, c='blue')
      plt.scatter(sepallen_X_petallen_C_2,sepalwid_X_petalwid_C_2, c='red')
      plt.xlabel('Linear Sum  of Sepal & Petal lengths in cm')
      plt.ylabel('Linear Sum  of Sepal & Petal widths in cm')
      plt.title('Clusterings')
      plt.show()

      break

    elif (New_iteration_centroids!=Last_iteration_centroids and len_C_0!=0 and len_C_1!=0 and len_C_2!=0) :
      print("\nCASE: 2 COMMON\n")
      Last_iteration_centroids = New_iteration_centroids

    elif (len_C_0==0 and len_C_1==0) :
      print("\nCASE: 3 VERY RARE\n")
      Last_iteration_centroids[2]=New_iteration_centroids[2]

      Last_iteration_centroids[0][0]=0.5*New_iteration_centroids[2][0]
      Last_iteration_centroids[0][1]=0.5*New_iteration_centroids[2][1]
      Last_iteration_centroids[0][2]=0.5*New_iteration_centroids[2][2]
      Last_iteration_centroids[0][3]=0.5*New_iteration_centroids[2][3]

      Last_iteration_centroids[1][0]=0.75*New_iteration_centroids[2][0]
      Last_iteration_centroids[1][1]=0.75*New_iteration_centroids[2][1]
      Last_iteration_centroids[1][2]=0.75*New_iteration_centroids[2][2]
      Last_iteration_centroids[1][3]=0.75*New_iteration_centroids[2][3]

    elif (len_C_0==0 and len_C_2==0) :
      print("\nCASE: 4 VERY RARE\n")
      Last_iteration_centroids[1]=New_iteration_centroids[1]

      Last_iteration_centroids[0][0]=0.5*New_iteration_centroids[1][0]
      Last_iteration_centroids[0][1]=0.5*New_iteration_centroids[1][1]
      Last_iteration_centroids[0][2]=0.5*New_iteration_centroids[1][2]
      Last_iteration_centroids[0][3]=0.5*New_iteration_centroids[1][3]

      Last_iteration_centroids[2][0]=0.75*New_iteration_centroids[1][0]
      Last_iteration_centroids[2][1]=0.75*New_iteration_centroids[1][1]
      Last_iteration_centroids[2][2]=0.75*New_iteration_centroids[1][2]
      Last_iteration_centroids[2][3]=0.75*New_iteration_centroids[1][3]

    elif (len_C_1==0 and len_C_2==0) :
      print("\nCASE: 5 VERY RARE\n")
      Last_iteration_centroids[0]=New_iteration_centroids[0]

      Last_iteration_centroids[1][0]=0.5*New_iteration_centroids[0][0]
      Last_iteration_centroids[1][1]=0.5*New_iteration_centroids[0][1]
      Last_iteration_centroids[1][2]=0.5*New_iteration_centroids[0][2]
      Last_iteration_centroids[1][3]=0.5*New_iteration_centroids[0][3]

      Last_iteration_centroids[2][0]=0.75*New_iteration_centroids[0][0]
      Last_iteration_centroids[2][1]=0.75*New_iteration_centroids[0][1]
      Last_iteration_centroids[2][2]=0.75*New_iteration_centroids[0][2]
      Last_iteration_centroids[2][3]=0.75*New_iteration_centroids[0][3]


    elif (len_C_0==0) :
      print("\nCASE: 6 RARE\n")
      Last_iteration_centroids[1]=New_iteration_centroids[1]
      Last_iteration_centroids[2]=New_iteration_centroids[2]

      Last_iteration_centroids[0][0]=0.5*(New_iteration_centroids[1][0] + New_iteration_centroids[2][0])
      Last_iteration_centroids[0][1]=0.5*(New_iteration_centroids[1][1] + New_iteration_centroids[2][1])
      Last_iteration_centroids[0][2]=0.5*(New_iteration_centroids[1][2] + New_iteration_centroids[2][2])
      Last_iteration_centroids[0][3]=0.5*(New_iteration_centroids[1][3] + New_iteration_centroids[2][3])


    elif (len_C_1==0) :
      print("\nCASE: 7 RARE\n")
      Last_iteration_centroids[0]=New_iteration_centroids[0]
      Last_iteration_centroids[2]=New_iteration_centroids[2]

      Last_iteration_centroids[1][0]=0.5*(New_iteration_centroids[0][0] + New_iteration_centroids[2][0])
      Last_iteration_centroids[1][1]=0.5*(New_iteration_centroids[0][1] + New_iteration_centroids[2][1])
      Last_iteration_centroids[1][2]=0.5*(New_iteration_centroids[0][2] + New_iteration_centroids[2][2])
      Last_iteration_centroids[1][3]=0.5*(New_iteration_centroids[0][3] + New_iteration_centroids[2][3])


    elif (len_C_2==0) :
      print("\nCASE: 8 RARE\n")
      Last_iteration_centroids[0]=New_iteration_centroids[0]
      Last_iteration_centroids[1]=New_iteration_centroids[1]

      Last_iteration_centroids[2][0]=0.5*(New_iteration_centroids[0][0] + New_iteration_centroids[1][0])
      Last_iteration_centroids[2][1]=0.5*(New_iteration_centroids[0][1] + New_iteration_centroids[1][1])
      Last_iteration_centroids[2][2]=0.5*(New_iteration_centroids[0][2] + New_iteration_centroids[1][2])
      Last_iteration_centroids[2][3]=0.5*(New_iteration_centroids[0][3] + New_iteration_centroids[1][3])

    print(f"\nChecking for Convergence in K-Means Algorithm in Iteration number : {Iterations}")


#********************************************************************************************************************************************************************************************************************************
#Inputs for k-means algorithm with k=3
#********************************************************************************************************************************************************************************************************************************

url="https://raw.githubusercontent.com/SaumyenMishraIITP/iris/main/Iris.csv" # raw-github-link
df=pd.read_csv(url)                                                          # converting csv to dataframe
df=df.drop(['Id'], axis=1)                                                   # removing the column 'Id'


initial_centroids_set_1=[[mean_setosa_sep_len,mean_setosa_sep_wid,mean_setosa_pet_len,mean_setosa_pet_wid], [mean_versicolor_sep_len,mean_versicolor_sep_wid,mean_versicolor_pet_len,mean_versicolor_pet_wid], [mean_virginica_sep_len,mean_virginica_sep_wid,mean_virginica_pet_len,mean_virginica_pet_wid]]
#[50,61,39], SSE : 78.945, Entropy : [0, 0.59, 0.58]

initial_centroids_set_2=[[5,3.5,1.5,0],[6,3,4.5,1.5],[6.5,3,5.5,2]]
#[50,62,38], SSE : 78.940, Entropy : [0, 0.57, 0.52]

initial_centroids_set_3=[[5.25,3.25,1.75,0.5],[4.75,2.75,1.25,0],[6.5,3,5.5,2]]
#[31,22,97], SSE : 145.279, Entropy : [0.71, 0.52, 0.083]

initial_centroids_set_4=[[5,3.5,1.5,0],[6.25,3,5,1.75],[7,4,6,3]]
#[50,62,38], SSE : 78.940, Entropy : [0, 0.57, 0.52]

initial_centroids_set_5=[[5,2,2,1],[4,3,3,1],[5,3,4,2]]
#[50,61,39], SSE : 78.945, Entropy : [0, 0.59, 0.58]

initial_centroids_set_6=[[2,1,1,0],[3,2,2,1],[4,2,2,1]]
#[61,50,39], SSE : 78.945, Entropy : [0.59, 0, 0.58]

print(f"\nGiven Dataset : \n\n{df}")

print("\n\n**************************************************************************************************************************************************************************************************")
print("\n**************************************************************************************************************************************************************************************************")

print(f"\nRandom Centroid List : \n\n{initial_centroids_set_1}")

print("\n\n**************************************************************************************************************************************************************************************************")
print("\n**************************************************************************************************************************************************************************************************")

kmeans_iris(initial_centroids_set_1,df)