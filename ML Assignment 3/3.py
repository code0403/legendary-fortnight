#importing the required packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error


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


def learn(x,y,m,c):
  iteration = 0
  while True:
    iteration += 1
    m_old = m
    c_old = c
    error = y - (m * x + c)
    x_error = (y - (m * x + c)) * x
    error = np.sum(error)/len(x)
    x_error = np.sum(x_error)/len(x)
    learning_rate = 0.01
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



# Calculate the intercept and slope for each feature
intercepts = []
slopes = []

print("Intercepts and Slopes:")
for x, label in zip([indpd_avg_sessn, indpd_tm_app, indpd_tm_web, indpd_mbrshp], 
                    ['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']):
    m, c, _ = learn(x, dependent, initial_m, initial_c)
    intercepts.append(c)
    slopes.append(m)
    print(f"{label}: Intercept = {c}, Slope = {m}")


# Calculate the coefficients
coefficients = pd.DataFrame({'Feature': ['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership'],
                             'Intercept': intercepts,
                             'Slope': slopes})
print("\nCoefficients:")
print(coefficients)


# Determine which feature the company should invest more in
max_coefficient_feature = coefficients['Slope'].idxmax()
print("\nCompany should invest more in:", coefficients.loc[max_coefficient_feature, 'Feature'])


# Plot the test prediction for the feature with the highest coefficient
plt.scatter(indpd_mbrshp, dependent)
plt.xlabel('Length of Membership')
plt.ylabel('Yearly Amount Spent')
plt.title('Test Prediction')
plt.plot(indpd_mbrshp, slopes[-1] * indpd_mbrshp + intercepts[-1], color='red')
plt.show()
