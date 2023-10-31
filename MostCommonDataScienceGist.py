# 10 common Python code snippets used in data science
# These code snippets cover various aspects of data science, including data loading, exploration, visualization, cleaning, machine learning modeling, evaluation, and feature selection. You can adapt and expand upon these snippets to suit your specific data science projects.
# 1. Importing Libraries:

# Import commonly used data science libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Description: Import essential data science libraries like NumPy, Pandas, Matplotlib, and Seaborn.
# -------------------------------------------------------------------------------------------------------------------------
# 2. Loading Data:

# Load a CSV file into a Pandas DataFrame
data = pd.read_csv('data.csv')

# Description: Load data from a CSV file into a Pandas DataFrame for analysis.
# -------------------------------------------------------------------------------------------------------------------------
#3. Data Exploration:

# Display basic statistics of the DataFrame
print(data.describe())

# Description: Get a summary of the data, including mean, standard deviation, and other statistical measures.
# -------------------------------------------------------------------------------------------------------------------------
# 4. Data Visualization:

# Create a histogram to visualize a numeric variable
plt.hist(data['column_name'], bins=20)
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Histogram of Column')
plt.show()

# Description: Create a histogram to visualize the distribution of a numeric variable.
# -------------------------------------------------------------------------------------------------------------------------
# 5. Data Cleaning:

# Check for and handle missing values
data.isnull().sum()
data.fillna(value, inplace=True)

# Description: Identify and handle missing values in the dataset.
# -------------------------------------------------------------------------------------------------------------------------
# 6. Data Preprocessing:

# Encode categorical variables using one-hot encoding
data = pd.get_dummies(data, columns=['categorical_column'])

# Description: Convert categorical variables into numerical format using one-hot encoding.
# -------------------------------------------------------------------------------------------------------------------------
# 7. Machine Learning Model:

# Train a machine learning model (e.g., Linear Regression)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

# Description: Train a machine learning model, such as linear regression, on a training dataset.
# -------------------------------------------------------------------------------------------------------------------------
# 8. Model Evaluation:

# Evaluate the model's performance using metrics like RMSE
from sklearn.metrics import mean_squared_error
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', rmse)

# Description: Assess the model's performance using evaluation metrics like RMSE.
# -------------------------------------------------------------------------------------------------------------------------
# 9. Data Splitting:

# Split the dataset into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Description: Divide the data into training and testing subsets for model validation.
# -------------------------------------------------------------------------------------------------------------------------
# 10. Feature Selection:

# Select important features using feature importance
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X, y)
feature_importance = model.feature_importances_

# Description: Determine important features in a dataset using techniques like feature importance.
# -------------------------------------------------------------------------------------------------------------------------