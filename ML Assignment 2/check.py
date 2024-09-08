import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Data Loading and Preprocessing
student_db = pd.read_csv("students.csv")
student_db = student_db.drop_duplicates()

# Feature Selection based on Variance
list_var = []
for a1 in range(0, len(student_db.columns), 1):
    Y1 = student_db.iloc[:, [a1]].values.ravel()
    Y1_numeric = pd.to_numeric(Y1, errors='coerce')  # Convert to numeric
    v1 = np.var(Y1_numeric)
    list_var.append(v1)
list_var.remove(list_var[0])
list_var.remove(list_var[0])

# Plotting Feature Variance
feat = list(range(2, len(student_db.columns), 1))
plt.plot(feat, list_var, color='blue', linestyle='dashed', linewidth=2,marker='o', markerfacecolor='red', markersize=8)
plt.xlabel('Feature IDs')
plt.ylabel('Feature Variance')
plt.title('Feature Selection based on Variance')
plt.show()

# Pair Grid Visualization
g = sns.PairGrid(student_db.loc[:, ["gradyear", "NumberOffriends", "basketball", "football", "soccer", "softball", "volleyball", "baseball", "tennis"]])
g.map_diag(plt.hist, histtype="step", linewidth=3)
g.map_offdiag(plt.scatter)
plt.show()
