# Step 01:-Imported the required packages.*


#importing the required packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error


# Step 02:- Pre-processing of data:
# 1. Read the data and select dependent and independent columns.
# 2. Convert them to array format by to_numpy()
# 3. To make the dependent and independent variable on same scale Divide
# them with their max value. So, all values will be between 0 and 1


data = pd.read_csv("Ecommerce Customers.csv")
#Select dependent and independent columns and convert them to array.
dependent = data['Yearly Amount Spent'].to_numpy()
indpd_avg_sessn = data['Avg. Session Length'].to_numpy()
indpd_tm_app = data['Time on App'].to_numpy()
indpd_tm_web = data['Time on Website'].to_numpy()
indpd_mbrshp = data['Length of Membership'].to_numpy()

#Divide the values with their max Value so all scale will between 0 and 1
dependent = dependent/max(dependent)
indpd_avg_sessn = indpd_avg_sessn/max(indpd_avg_sessn)
indpd_tm_app = indpd_tm_app/max(indpd_tm_app)
indpd_tm_web = indpd_tm_web/max(indpd_tm_web)
indpd_mbrshp = indpd_mbrshp/max(indpd_mbrshp)

# **Step 03:-**
# **Define the learn func6on considering X as independent and Y as a dependent variable. which will do the following: **

# 1. Calculate the Slope/Coefficient (m) and Constant/Intercept (c).
# i. Error = sum( y -(m * x + c)) / len(x)
# ii. Error(x) = sum( y -(m * x + c) * x) / len(x)
# iii. m = m + (Learning_rate * Error(x))
# iv. c = c + (Learning_rate * Error)
# v. Here the ini6al value of m and c will be any random value.
# vi. Program will stop when m and c are unchanged.
# 2. Once we calculate the m and c value calculate the predicated values for y (dependent)
# i. y_pred = m * x + c
# 3. Calculate the Mean square error between actual y and predicted y
# i. will use sklearn mean_squared_error(y, y_pred)
# 4. Will plot the graph
# i. Plot scaIered graph for x and y
# ii. Plot line y_pred

def learn(x,y,m,c):
 iteration = 0
 while True:
  iteration += 1
  m_old = m
  c_old = c
  error = y - (m * x + c)

  #Y is actual value and (m * x + c) is calculated value. So error will be actual value minus calculated value.

  x_error = (y - (m * x + c)) * x
  error = np.sum(error)/len(x)
  x_error = np.sum(x_error)/len(x)
  learning_rate = 0.01

  # Learning rate any random value
  delta_m = learning_rate * x_error
  delta_c = learning_rate * error
  m += delta_m
  c += delta_c
  if round(m,8) == round(m_old,8) and round(c,8) == round(c_old,8):
    break
  return m,c,iteration

#Plot the graph by calculating the predicated line
def plot_graph(x,y,m,c,x_label,y_label):
 y_pred_line = m * x + c # Calculate the Line
 sum_of_square = mean_squared_error(y,y_pred_line)
 plt.figure(figsize=(18, 4), dpi=80)
 plt.xlabel(x_label)
 plt.ylabel(y_label)
 print(f"Slope Theta1 (m):{m}\nIntercept Theta0 (c):{c}\nSum of Square:{sum_of_square}")
 plt.scatter(x, y)
 plt.plot(x,y_pred_line,color='red')
 plt.show()

# Step 04:-
# It is a Main program to call learn function to calculate m and c for each feature.
# 1. Define any random value for m and c
# 2. Calculate m and c till it unchanged.
# 3. Then calculate the y_predict value where y = mx + c
# 4. And plot the scaIer graph for x and y.
# 5. Plot the line for y and y_predict.


initial_m = np.random.random()
initial_c = np.random.random()
print("Initial Random Value of m:",initial_m,"& c:",initial_c)
print("Avg. Session Length X Yearly Amount Spent")
m,c,iteration = learn(indpd_avg_sessn,dependent,initial_m,initial_c)
print("Achieved in iteration:",iteration)
plot_graph(indpd_avg_sessn,dependent,m,c,"Avg. Session Length","Yearly Amount Spent")
print("Time on App X Yearly Amount Spent")
m,c,iteration = learn(indpd_tm_app,dependent,initial_m,initial_c)
print("Achieved in iteration:",iteration)
plot_graph(indpd_tm_app,dependent,m,c,"Time on App","Yearly Amount Spent")
print("Time on Website X Yearly Amount Spent")
m,c,iteration = learn(indpd_tm_web,dependent,initial_m,initial_c)
print("Achieved in iteration:",iteration)
plot_graph(indpd_tm_web,dependent,m,c,"Time on Website","Yearly Amount Spent")
print("Length of Membership X Yearly Amount Spent")
m,c,iteration = learn(indpd_mbrshp,dependent,initial_m,initial_c)
print("Achieved in iteration:",iteration)
plot_graph(indpd_mbrshp,dependent,m,c,"Length of Membership","Yearly Amount Spent")
