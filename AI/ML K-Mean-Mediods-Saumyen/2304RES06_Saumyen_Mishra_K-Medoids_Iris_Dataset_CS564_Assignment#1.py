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
#Exploratory data analysis & initialization of Medoids
#********************************************************************************************************************************************************************************************************************************

n_setosa=0
n_versicolor=0
n_virginica=0

kmeans = [[5.005999999999999, 3.4180000000000006, 1.464, 0.2439999999999999], [5.88360655737705, 2.740983606557377, 4.388524590163935, 1.4344262295081966], [6.853846153846153, 3.0769230769230766, 5.715384615384615, 2.053846153846153]]

k11=0
k21=0
k31=0

dist11=[]
dist21=[]
dist31=[]

for i1 in range(0,tot_rows,1) :
    k11=math.sqrt(((kmeans[0][0] - df.iat[i1,0])**2) + ((kmeans[0][1] - df.iat[i1,1])**2) + ((kmeans[0][2] - df.iat[i1,2])**2) + ((kmeans[0][3] - df.iat[i1,3])**2))
    dist11.append(k11)

    k21=math.sqrt(((kmeans[1][0] - df.iat[i1,0])**2) + ((kmeans[1][1] - df.iat[i1,1])**2) + ((kmeans[1][2] - df.iat[i1,2])**2) + ((kmeans[1][3] - df.iat[i1,3])**2))
    dist21.append(k21)

    k31=math.sqrt(((kmeans[2][0] - df.iat[i1,0])**2) + ((kmeans[2][1] - df.iat[i1,1])**2) + ((kmeans[2][2] - df.iat[i1,2])**2) + ((kmeans[2][3] - df.iat[i1,3])**2))
    dist31.append(k31)

MIN_D1=min(dist11)
MIN_D2=min(dist21)
MIN_D3=min(dist31)


IND_D1=dist11.index(MIN_D1)
IND_D2=dist21.index(MIN_D2)
IND_D3=dist31.index(MIN_D3)



for i in range(0,tot_rows,1) :
  if  (df.iat[i,4]=="Iris-setosa") :
    df.iat[i,4] = 0
    n_setosa = n_setosa+1

  elif  (df.iat[i,4]=="Iris-versicolor") :
    df.iat[i,4] = 1
    n_versicolor = n_versicolor+1

  elif (df.iat[i,4]=="Iris-virginica") :
      df.iat[i,4] = 2
      n_virginica = n_virginica+1
print(n_setosa)
print(n_versicolor)
print(n_virginica)
kmedoids=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
kmedoids[0] = [df.iat[IND_D1,0], df.iat[IND_D1,1], df.iat[IND_D1,2], df.iat[IND_D1,3], df.iat[IND_D1,4]]
kmedoids[1] = [df.iat[IND_D2,0], df.iat[IND_D2,1], df.iat[IND_D2,2], df.iat[IND_D2,3], df.iat[IND_D2,4]]
kmedoids[2] = [df.iat[IND_D3,0], df.iat[IND_D3,1], df.iat[IND_D3,2], df.iat[IND_D3,3], df.iat[IND_D3,4]]
#print(kmedoids)
print (df)

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
#Medoid Function, SSE calculation Function, K-Medoids Assignment function, K-Medoids-Iris Function
#********************************************************************************************************************************************************************************************************************************

def assignment_function(medoids,dataset) :

  num_rows = len(dataset.index)
  num_cols = len(dataset.columns)

  k1=0
  k2=0
  k3=0

  dist1=[]
  dist2=[]
  dist3=[]


  C0_m=0
  C1_m=0
  C2_m=0


  for t in range (0, num_rows, 1) :
    if (dataset.iat[t,0]==medoids[0][0] and dataset.iat[t,1]==medoids[0][1] and dataset.iat[t,2]==medoids[0][2] and dataset.iat[t,3]==medoids[0][3] and dataset.iat[t,4]==medoids[0][4]) :
      C0_m=t
      #print(C0_m)
    elif (dataset.iat[t,0]==medoids[1][0] and dataset.iat[t,1]==medoids[1][1] and dataset.iat[t,2]==medoids[1][2] and dataset.iat[t,3]==medoids[1][3] and dataset.iat[t,4]==medoids[1][4]) :
      C1_m=t
      #print(C1_m)
    elif (dataset.iat[t,0]==medoids[2][0] and dataset.iat[t,1]==medoids[2][1] and dataset.iat[t,2]==medoids[2][2] and dataset.iat[t,3]==medoids[2][3] and dataset.iat[t,4]==medoids[2][4]) :
      C2_m=t
      #print(C2_m)


  for i in range(0,num_rows,1) :
    if (i!=C0_m and i!=C1_m and i!=C2_m) :
        k1=math.sqrt(((medoids[0][0] - dataset.iat[i,0])**2) + ((medoids[0][1] - dataset.iat[i,1])**2) + ((medoids[0][2] - dataset.iat[i,2])**2) + ((medoids[0][3] - dataset.iat[i,3])**2))
        dist1.append(k1)

        k2=math.sqrt(((medoids[1][0] - dataset.iat[i,0])**2) + ((medoids[1][1] - dataset.iat[i,1])**2) + ((medoids[1][2] - dataset.iat[i,2])**2) + ((medoids[1][3] - dataset.iat[i,3])**2))
        dist2.append(k2)

        k3=math.sqrt(((medoids[2][0] - dataset.iat[i,0])**2) + ((medoids[2][1] - dataset.iat[i,1])**2) + ((medoids[2][2] - dataset.iat[i,2])**2) + ((medoids[2][3] - dataset.iat[i,3])**2))
        dist3.append(k3)

  list0=[]
  list1=[]
  list2=[]

  for j in range (0,num_rows-3,1) :
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

  if (medoids[0][4]==0) :
    list0.append(medoids[0])
  elif(medoids[1][4]==0) :
    list0.append(medoids[1])
  elif(medoids[2][4]==0) :
    list0.append(medoids[2])

  if (medoids[0][4]==1) :
    list1.append(medoids[0])
  elif(medoids[1][4]==1) :
    list1.append(medoids[1])
  elif(medoids[2][4]==1) :
    list1.append(medoids[2])

    
  if (medoids[0][4]==2) :
    list2.append(medoids[0])
  elif(medoids[1][4]==2) :
    list2.append(medoids[1])
  elif(medoids[2][4]==2) :
    list2.append(medoids[2])

  print(list2)
  cluster0 = pd.DataFrame (list(list0), columns=["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm","Species"])
  print ("In assignment function, Cluster 0 is calculated")

  cluster1 = pd.DataFrame (list(list1), columns=["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm","Species"])
  print ("In assignment function, Cluster 1 is calculated")

  cluster2 = pd.DataFrame (list(list2), columns=["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm","Species"])
  print ("In assignment function, Cluster 2 is calculated")

  len_C0=len(cluster0.index)
  len_C1=len(cluster1.index)
  len_C2=len(cluster2.index)

  SSE_C0=0
  SSE_C1=0
  SSE_C2=0

  SSE_Clusterings=0

  for i in range (0,len_C0,1) :
      SSE_C0 = SSE_C0 + (((medoids[0][0]-cluster0.iat[i,0])**2) + ((medoids[0][1]-cluster0.iat[i,1])**2) + ((medoids[0][2]-cluster0.iat[i,2])**2) + ((medoids[0][3]-cluster0.iat[i,3])**2))

  for i in range (0,len_C1,1) :
      SSE_C1 = SSE_C1 + (((medoids[1][0]-cluster1.iat[i,0])**2) + ((medoids[1][1]-cluster1.iat[i,1])**2) + ((medoids[1][2]-cluster1.iat[i,2])**2) + ((medoids[1][3]-cluster1.iat[i,3])**2))

  for i in range (0,len_C2,1) :
      SSE_C2 = SSE_C2 + (((medoids[2][0]-cluster2.iat[i,0])**2) + ((medoids[2][1]-cluster2.iat[i,1])**2) + ((medoids[2][2]-cluster2.iat[i,2])**2) + ((medoids[2][3]-cluster2.iat[i,3])**2))

  SSE_Clusterings = SSE_C0 + SSE_C1 + SSE_C2
  #print(f"\n\nSSE_C0 : {SSE_C0}\n\nSSE_C1 : {SSE_C1}\n\nSSE_C2 : {SSE_C2}\n\nSSE_Clusterings : {SSE_Clusterings}\n\n")

  #print(cluster0)
  #print(cluster1)
  #print(cluster2)

  return cluster0, cluster1, cluster2, SSE_C0, SSE_C1, SSE_C2, SSE_Clusterings, medoids

#***********************************************************************************************************************************************************************************************************************************
#***********************************************************************************************************************************************************************************************************************************

def updation_function (C0,C1,C2,SSE0,SSE1,SSE2,SSE_tot,Parent_Medoids) :

  len_C0=len(C0.index)
  len_C1=len(C1.index)
  len_C2=len(C2.index)

  print(f"No. of points in Cluster 0 right now : {len_C0}\nNo. of points in Cluster 1 right now : {len_C1}\nNo. of  points in Cluster 2 right now : {len_C2}\n")

  new_iteration_medoids=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

  random_medoids=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

  Conv=0

  list_int_1=[]
  X_1=[]

  for i in range (0, tot_rows, 1) :
    random_medoids=[Parent_Medoids[0],Parent_Medoids[1], [df.iat[i,0], df.iat[i,1], df.iat[i,2], df.iat[i,3], df.iat[i,4]]]
    list_int_1.append(assignment_function(random_medoids,df))
    print(f"\nDone with Medoid[2] movement check to Row no. {i} if the dataset\n")

  for j in range (0, tot_rows, 1) :
    X_1.append(list_int_1[j][6])
  
  list_int_2=[]
  X_2=[]

  for i1 in range (0, tot_rows, 1) :
    random_medoids=[Parent_Medoids[0],[df.iat[i1,0], df.iat[i1,1], df.iat[i1,2], df.iat[i1,3], df.iat[i1,4]] ,Parent_Medoids[2]]
    list_int_2.append(assignment_function(random_medoids,df))
    print(f"\nDone with Medoid[1] movement check to Row no. {i1} if the dataset\n")

  for j1 in range (0, tot_rows, 1) :
    X_2.append(list_int_2[j1][6])
  
  list_int_3=[]
  X_3=[]

  for i2 in range (0, tot_rows, 1) :
    random_medoids=[[df.iat[i2,0], df.iat[i2,1], df.iat[i2,2], df.iat[i2,3], df.iat[i2,4]], Parent_Medoids[1] ,Parent_Medoids[2]]
    list_int_3.append(assignment_function(random_medoids,df))
    print(f"\nDone with Medoid[0] movement check to Row no. {i2} if the dataset\n")

  for j2 in range (0, tot_rows, 1) :
    X_3.append(list_int_3[j2][6])


  min_SSE= min(X_1)
  min_SSE1= min(X_2)
  min_SSE2= min(X_3)

  min_SSE_ind=X_1.index(min_SSE)
  min_SSE_ind1=X_2.index(min_SSE1)
  min_SSE_ind2=X_3.index(min_SSE2)

  Ovr_min_SSE= min(min_SSE,min_SSE1,min_SSE2)

  if (Ovr_min_SSE == min_SSE) :
    if (min_SSE<SSE_tot) :
      cluster0=list_int_1[min_SSE_ind][0]
      cluster1=list_int_1[min_SSE_ind][1]
      cluster2=list_int_1[min_SSE_ind][2]
      SSE_C0=list_int_1[min_SSE_ind][3]
      SSE_C1=list_int_1[min_SSE_ind][4]
      SSE_C2=list_int_1[min_SSE_ind][5]
      SSE_Clusterings=list_int_1[min_SSE_ind][6]
      new_iteration_medoids = [Parent_Medoids[0],Parent_Medoids[1], [df.iat[min_SSE_ind,0], df.iat[min_SSE_ind,1], df.iat[min_SSE_ind,2], df.iat[min_SSE_ind,3], df.iat[min_SSE_ind,4]]]
      Conv=0

    else :
      cluster0=C0
      cluster1=C1
      cluster2=C2
      SSE_C0=SSE0
      SSE_C1=SSE1
      SSE_C2=SSE2
      SSE_Clusterings=SSE_tot
      new_iteration_medoids = Parent_Medoids
      Conv=1
      print("\nConvergence Reached as no better medoid combination exists!\n")
  
  elif (Ovr_min_SSE == min_SSE1) :
    if (min_SSE1<SSE_tot) :
      cluster0=list_int_2[min_SSE_ind1][0]
      cluster1=list_int_2[min_SSE_ind1][1]
      cluster2=list_int_2[min_SSE_ind1][2]
      SSE_C0=list_int_2[min_SSE_ind1][3]
      SSE_C1=list_int_2[min_SSE_ind1][4]
      SSE_C2=list_int_2[min_SSE_ind1][5]
      SSE_Clusterings=list_int_2[min_SSE_ind1][6]
      new_iteration_medoids = [Parent_Medoids[0],[df.iat[min_SSE_ind1,0], df.iat[min_SSE_ind1,1], df.iat[min_SSE_ind1,2], df.iat[min_SSE_ind1,3], df.iat[min_SSE_ind1,4]], Parent_Medoids[2]]
      Conv=0

    else :
      cluster0=C0
      cluster1=C1
      cluster2=C2
      SSE_C0=SSE0
      SSE_C1=SSE1
      SSE_C2=SSE2
      SSE_Clusterings=SSE_tot
      new_iteration_medoids = Parent_Medoids
      Conv=1
      print("\nConvergence Reached as no better medoid combination exists!\n")

  elif (Ovr_min_SSE == min_SSE2) :
    if (min_SSE2<SSE_tot) :
      cluster0=list_int_3[min_SSE_ind2][0]
      cluster1=list_int_3[min_SSE_ind2][1]
      cluster2=list_int_3[min_SSE_ind2][2]
      SSE_C0=list_int_3[min_SSE_ind2][3]
      SSE_C1=list_int_3[min_SSE_ind2][4]
      SSE_C2=list_int_3[min_SSE_ind2][5]
      SSE_Clusterings=list_int_3[min_SSE_ind2][6]
      new_iteration_medoids = [[df.iat[min_SSE_ind2,0], df.iat[min_SSE_ind2,1], df.iat[min_SSE_ind2,2], df.iat[min_SSE_ind2,3], df.iat[min_SSE_ind2,4]],Parent_Medoids[1], Parent_Medoids[2]]
      Conv=0

    else :
      cluster0=C0
      cluster1=C1
      cluster2=C2
      SSE_C0=SSE0
      SSE_C1=SSE1
      SSE_C2=SSE2
      SSE_Clusterings=SSE_tot
      new_iteration_medoids = Parent_Medoids
      Conv=1
      print("\nConvergence Reached as no better medoid combination exists!\n")


     
                    
  return  new_iteration_medoids, cluster0, cluster1, cluster2, SSE_C0, SSE_C1, SSE_C2, SSE_Clusterings, Conv


#***********************************************************************************************************************************************************************************************************************************
#***********************************************************************************************************************************************************************************************************************************

def kmedoids_iris(ini_medoids,dataset) :
  K=3
  Last_iteration_medoids = ini_medoids
  Iterations=0
  New_iteration_medoids=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

  while 1:

    Iterations = Iterations+1
    print(f"\n\nIteration Number : {Iterations}\n\n")
    A1 = assignment_function(Last_iteration_medoids,dataset)
    A = A1[0]
    B = A1[1]
    C = A1[2]
    D = A1[3]
    E = A1[4]
    F = A1[5]
    G = A1[6]
    H = A1[7]
    print("Assignment is Done")

    B1=updation_function(A,B,C,D,E,F,G,H)
    New_iteration_medoids = B1[0]

    print(New_iteration_medoids)

    print("Updation is Done")
    C_0 = B1[1]
    C_1 = B1[2]
    C_2 = B1[3]
    len_C_0 = len(C_0.index)
    len_C_1 = len(C_1.index)
    len_C_2 = len(C_2.index)
    SSE_C_0 = B1[4]
    SSE_C_1 = B1[5]
    SSE_C_2 = B1[6]
    SSE_Total = SSE_C_0 + SSE_C_1 + SSE_C_2
    Convergence = B1[8]

    if (New_iteration_medoids==Last_iteration_medoids or Convergence==1) :

      print("\n\n****************************************************************************************************************************************************************************************************************************")
      print("\n****************************************************************************************************************************************************************************************************************************")
      print("\n\n")
      print(f"Iteration No. : {Iterations}\n\n")
      print(f"Total Number of Clusters : {K}")
      print("\n\n")
      print(f"Final Medoids : {New_iteration_medoids}")
      print("\n\n")
      print(f"Points in Cluster 0 : {len_C_0}")
      print("\n\n")
      print(f"SSE of Cluster 0 : {SSE_C_0}")
      print("\n\n")
      print(f"Points in Cluster 1 : {len_C_1}")
      print("\n\n")
      print(f"SSE of Cluster 1 : {SSE_C_1}")
      print("\n\n")
      print(f"Points in Cluster 2 : {len_C_2}")
      print("\n\n")
      print(f"SSE of Cluster 2 : {SSE_C_2}")
      print("\n\n")
      print(f"Total SSE : {SSE_Total}")

      
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

    elif (New_iteration_medoids!=Last_iteration_medoids) :
      print("\n\n****************************************************************************************************************************************************************************************************************************")
      Last_iteration_medoids = New_iteration_medoids
      print(f"\n\nChecking for Convergence in K-Medoids Algorithm in Iteration number : {Iterations}\n\n")


#***********************************************************************************************************************************************************************************************************************************
#***********************************************************************************************************************************************************************************************************************************
medoid_1 = [[5.1,3.3,1.7,0.5,0], [6.1,2.8,4.7,1.2,1], [6.3,2.7,4.9,1.8,2]]
#2h56mins, [50,47,53], SSE : 128.13

kmedoids_iris(medoid_1,df)


#***********************************************************************************************************************************************************************************************************************************
#***********************************************************************************************************************************************************************************************************************************
