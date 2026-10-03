import pandas as pd

# Load the dataset
df = pd.read_csv("all_stock_5yr.csv")

# Display first 5 rows
print(df.head())

# Display column names
print("\nColumns:")
print(df.columns)

# Display dataset information
print("\nDataset Information:")
print(df.info())
import pandas as pd

# Load the dataset
df = pd.read_csv("all_stock_5yr.csv")

# Display first 5 rows
print(df.head())

# Display column names
print("\nColumns:")
print(df.columns)

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Select Apple stock
df = df[df["Name"] == "AAPL"]

# Display Apple stock data
print("\nApple Stock Data:")
print(df.head())

print("\nNumber of Apple records:")
print(len(df))
# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())
# Sort data by date
df = df.sort_values("date")

print("\nData after sorting by date:")
print(df.head())
# Create previous day's closing price
df["previous_close"] = df["close"].shift(1)

# Remove the first row because it has no previous day's value
df = df.dropna()

print("\nData with Previous Close:")
print(df.head())
# Define input and target
X = df[["previous_close"]]
y = df["close"]

print("\nInput (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())
# Split data into training and testing sets
split = int(len(df) * 0.8)

X_train = X[:split]
X_test = X[split:]

y_train = y[:split]
y_test = y[split:]

print("\nTraining data size:", len(X_train))
print("Testing data size:", len(X_test))
from sklearn.linear_model import LinearRegression

# Create the Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

print("\nModel training completed successfully!")
# Make predictions on test data
y_pred = model.predict(X_test)

print("\nPredicted Stock Prices:")
print(y_pred[:5])
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Calculate evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("Mean Absolute Error (MAE):", mae)
print("Root Mean Squared Error (RMSE):", rmse)
print("R2 Score:", r2)
import matplotlib.pyplot as plt

# Plot actual vs predicted prices
plt.figure(figsize=(10, 5))

plt.plot(y_test.values, label="Actual Price")
plt.plot(y_pred, label="Predicted Price")

plt.title("Actual vs Predicted Stock Prices")
plt.xlabel("Test Data")
plt.ylabel("Closing Price")
plt.legend()

plt.show()
# Display actual vs predicted values
results = pd.DataFrame({
    "Actual Price": y_test.values,
    "Predicted Price": y_pred
})

print("\nActual vs Predicted Prices:")
print(results.head(10))