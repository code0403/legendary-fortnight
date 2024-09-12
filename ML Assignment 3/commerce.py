import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the dataset (replace 'data.csv' with the actual filename)
data = pd.read_csv('Ecommerce Customers.csv')

# Split the dataset into features (X) and target variable (y)
X = data[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
y = data['Yearly Amount Spent']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Plot each feature separately against the target variable
features = X.columns

for feature in features:
    plt.scatter(X[feature], y, label=feature)
    plt.xlabel(feature)
    plt.ylabel('Yearly Amount Spent')
    plt.title(f'{feature} vs. Yearly Amount Spent')
    # Plot the regression line
    plt.plot(X[feature], model.predict(X), color='none', linewidth=2)
    plt.legend()
    plt.show()

# 1. Find out the intercept
intercept = model.intercept_
print("Intercept:", intercept)

# 2. Find out the slope
slope = model.coef_
print("Slope:", slope)

# 3. Find out the coefficient for each feature
coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
print("Coefficients:")
print(coefficients)

# 4. Determine which feature the company should invest more in
# We can compare the absolute values of coefficients to determine which feature has more impact
max_coefficient_feature = coefficients.abs().idxmax().iloc[0]
print("Company should invest more in:", max_coefficient_feature)

# 5. Plot the test prediction
y_pred = model.predict(X_test)
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Yearly Amount Spent")
plt.ylabel("Predicted Yearly Amount Spent")
plt.title("Actual vs. Predicted Yearly Amount Spent")
plt.show()
