# Predict house prices using a simple linear regression model
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
# Generate synthetic data for house sizes (in square feet) and prices (in dollars)
np.random.seed(0)
house_sizes = 2.5 * np.random.randn(1000) + 1500  # Average size around 1500 sqft
house_prices = house_sizes * 200 + (10000 * np.random.randn(1000))  # Price with some noise
# Reshape data for sklearn
house_sizes = house_sizes.reshape(-1, 1)
house_prices = house_prices.reshape(-1, 1)
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(house_sizes, house_prices, test_size=0.2, random_state=42)
# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)
# Make predictions on the test set
y_pred = model.predict(X_test)
# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Plotting the results
plt.scatter(X_test, y_test, color='blue', label='Actual Prices')
plt.scatter(X_test, y_pred, color='red', label='Predicted Prices')
plt.xlabel('House Size (sqft)')
plt.ylabel('Price ($)')
plt.title('Actual vs Predicted House Prices')
plt.legend()
plt.show()
# Example usage
new_house_size = np.array([[2000]])  # Predict price for a 2000 sqft house
predicted_price = model.predict(new_house_size)
print(f"Predicted price for a 2000 sqft house: ${predicted_price[0][0]:.2f}")
# Note: To run this code, you need to have the required libraries installed.
# You can install the required libraries using:
# pip install numpy scikit-learn matplotlib