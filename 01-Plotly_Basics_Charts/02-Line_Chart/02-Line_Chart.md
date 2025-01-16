

## **Example 1: Stock Prices Over Time**

### **Purpose:**
Visualize the daily closing prices of multiple companies over a year to compare their stock performance.

### **Key Features Demonstrated:**
- Handling real-world financial data.
- Plotting multiple time series on the same chart.
- Adding interactive features like hover information.

### **Dataset:**
Simulated daily closing prices for three tech companies over one year.

### **Code Snippet:**
```python
# 1. IMPORT LIBRARIES
import plotly.express as px
import pandas as pd
import numpy as np

# 2. CREATE A SAMPLE DATASET
# Simulate daily closing prices for three tech companies over one year.
np.random.seed(100)  # For reproducibility
dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq='B')  # Business days
companies = ["TechCorp", "InnovateX", "FutureSoft"]

# Generate random walk data for stock prices
def generate_stock_prices(start_price=100):
    return start_price + np.cumsum(np.random.normal(0, 1, len(dates)))

data = {
    "Date": np.tile(dates, len(companies)),
    "Company": np.repeat(companies, len(dates)),
    "Closing Price": np.concatenate([generate_stock_prices() for _ in companies])
}
df_stock = pd.DataFrame(data)

# 3. STOCK PRICES LINE CHART
fig_stock = px.line(
    df_stock,
    x="Date",
    y="Closing Price",
    color="Company",
    title="Daily Closing Prices of Tech Companies in 2024",
    labels={
        "Date": "Date",
        "Closing Price": "Price (USD)"
    }
)

fig_stock.update_layout(
    hovermode="x unified"
)

fig_stock.show()
```

### **Explanation:**
1. **Data Generation:**
   - **Dates:** Generated business days for the year 2024.
   - **Companies:** Three fictional tech companies.
   - **Closing Prices:** Simulated using a random walk to mimic real stock price movements.

2. **Plotting:**
   - **Plotly Express (`px.line`):** Creates an interactive line chart.
   - **Color Coding:** Differentiates each company with distinct colors.
   - **Hovermode:** Set to "x unified" to display all companies' data when hovering over a specific date.

### **Why Include This Example?**
Stock price visualization is a common requirement in financial analysis. This example demonstrates how to handle time series data, compare multiple entities, and utilize interactive features that are crucial for financial dashboards.

---

## **Example 2: Average Monthly Temperatures Across Cities**

### **Purpose:**
Compare the average monthly temperatures of different cities to analyze climate patterns.

### **Key Features Demonstrated:**
- Using categorical x-axis with months.
- Differentiating lines by categories (cities).
- Customizing line styles for better distinction.

### **Dataset:**
Average monthly temperatures for four major cities.

### **Code Snippet:**
```python
# 1. IMPORT LIBRARIES
import plotly.express as px
import pandas as pd

# 2. CREATE A SAMPLE DATASET
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
cities = ["New York", "Los Angeles", "Chicago", "Houston"]

# Average temperatures in Celsius (simulated data)
temperature_data = {
    "Month": months * len(cities),
    "City": sorted(cities * len(months)),
    "Avg Temperature": [
        # New York
        0.6, 1.1, 5.5, 11.3, 17.0, 22.2, 24.7, 24.5, 20.3, 14.4, 8.9, 3.3,
        # Los Angeles
        13.9, 14.4, 15.6, 17.2, 18.9, 20.0, 22.2, 22.2, 21.1, 18.9, 15.6, 13.9,
        # Chicago
        -5.0, -3.3, 2.8, 9.4, 16.1, 21.7, 24.4, 23.9, 19.4, 12.2, 5.6, -1.1,
        # Houston
        11.1, 13.3, 16.1, 19.4, 23.3, 26.7, 28.3, 28.3, 26.7, 23.3, 17.8, 13.3
    ]
}

df_temp = pd.DataFrame(temperature_data)

# 3. TEMPERATURE LINE CHART
fig_temp = px.line(
    df_temp,
    x="Month",
    y="Avg Temperature",
    color="City",
    title="Average Monthly Temperatures in 2024",
    markers=True,
    line_dash="City",  # Differentiates lines by dash style
    labels={
        "Avg Temperature": "Temperature (°C)"
    }
)

fig_temp.update_layout(
    xaxis=dict(tickmode='linear'),
    hovermode="x unified"
)

fig_temp.show()
```

### **Explanation:**
1. **Data Preparation:**
   - **Months:** List of all months.
   - **Cities:** Four major U.S. cities.
   - **Avg Temperature:** Simulated average temperatures for each city across all months.

2. **Plotting:**
   - **Markers:** Added to show individual data points.
   - **Line Dash (`line_dash`):** Differentiates each city’s line style (solid, dash, dot, etc.).
   - **Hovermode:** "x unified" allows viewing all cities' temperatures for a specific month simultaneously.

### **Why Include This Example?**
Climate data is highly relatable and showcases how to handle categorical axes and multiple line styles for better visual distinction. This example also emphasizes the importance of customizing line appearances to improve chart readability.

---

## **Example 3: Website Traffic Sources Over a Quarter**

### **Purpose:**
Analyze the distribution of website traffic sources (Direct, Organic Search, Referral, Social) over three months to understand user acquisition channels.

### **Key Features Demonstrated:**
- Stacked line charts to show cumulative trends.
- Highlighting different traffic sources.
- Emphasizing growth trends over time.

### **Dataset:**
Weekly website traffic data segmented by source for a quarter (January - March).

### **Code Snippet:**
```python
# 1. IMPORT LIBRARIES
import plotly.express as px
import pandas as pd

# 2. CREATE A SAMPLE DATASET
weeks = [f"Week {i}" for i in range(1, 14)]  # 13 weeks in a quarter
sources = ["Direct", "Organic Search", "Referral", "Social"]

# Simulated traffic numbers
traffic_data = {
    "Week": np.tile(weeks, len(sources)),
    "Source": np.repeat(sources, len(weeks)),
    "Visitors": [
        # Direct
        500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720, 740,
        # Organic Search
        300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420,
        # Referral
        150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210,
        # Social
        80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140
    ]
}

df_traffic = pd.DataFrame(traffic_data)

# 3. WEBSITE TRAFFIC LINE CHART
fig_traffic = px.line(
    df_traffic,
    x="Week",
    y="Visitors",
    color="Source",
    title="Weekly Website Traffic Sources (Q1 2024)",
    markers=True,
    line_shape="linear",
    labels={
        "Visitors": "Number of Visitors"
    }
)

fig_traffic.update_layout(
    hovermode="x unified",
    legend_title="Traffic Source"
)

fig_traffic.show()
```

### **Explanation:**
1. **Data Generation:**
   - **Weeks:** 13 weeks representing a quarter.
   - **Sources:** Four primary traffic acquisition channels.
   - **Visitors:** Simulated visitor counts for each source per week.

2. **Plotting:**
   - **Markers:** Enhance visibility of weekly data points.
   - **Line Shape:** Set to "linear" for straightforward trend lines.
   - **Legend:** Clearly labels each traffic source.

### **Why Include This Example?**
Understanding website traffic sources is crucial for digital marketing strategies. This example illustrates how to track and compare multiple metrics over time, emphasizing the ability to discern trends and make data-driven decisions based on visualization.

---

## **Bonus Example: Sensor Data Monitoring**

### **Purpose:**
Monitor real-time sensor data (e.g., temperature, humidity, pressure) from an IoT device to detect anomalies and trends.

### **Key Features Demonstrated:**
- Real-time data simulation.
- Multiple y-axes for different measurement units.
- Highlighting anomalies or thresholds.

### **Dataset:**
Simulated minute-by-minute sensor readings over one hour.

### **Code Snippet:**
```python
# 1. IMPORT LIBRARIES
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# 2. CREATE A SAMPLE DATASET
# Simulate sensor data every minute for one hour
timestamps = pd.date_range(start="2024-04-01 12:00", periods=60, freq='T')
sensor_types = ["Temperature", "Humidity", "Pressure"]

# Generate random sensor data
np.random.seed(200)
temperature = 20 + np.random.normal(0, 0.5, len(timestamps)).cumsum()
humidity = 50 + np.random.normal(0, 1, len(timestamps)).cumsum()
pressure = 1013 + np.random.normal(0, 0.2, len(timestamps)).cumsum()

df_sensor = pd.DataFrame({
    "Timestamp": timestamps,
    "Temperature": temperature,
    "Humidity": humidity,
    "Pressure": pressure
})

# 3. SENSOR DATA MONITORING LINE CHART
fig_sensor = go.Figure()

# Temperature Trace
fig_sensor.add_trace(
    go.Scatter(
        x=df_sensor["Timestamp"],
        y=df_sensor["Temperature"],
        mode='lines+markers',
        name='Temperature (°C)',
        line=dict(color='red')
    )
)

# Humidity Trace
fig_sensor.add_trace(
    go.Scatter(
        x=df_sensor["Timestamp"],
        y=df_sensor["Humidity"],
        mode='lines+markers',
        name='Humidity (%)',
        line=dict(color='blue')
    )
)

# Pressure Trace
fig_sensor.add_trace(
    go.Scatter(
        x=df_sensor["Timestamp"],
        y=df_sensor["Pressure"],
        mode='lines+markers',
        name='Pressure (hPa)',
        line=dict(color='green')
    )
)

# Add threshold lines
fig_sensor.add_hline(y=21, line_dash="dash", line_color="red", annotation_text="Temp Threshold", annotation_position="top left")
fig_sensor.add_hline(y=55, line_dash="dash", line_color="blue", annotation_text="Humidity Threshold", annotation_position="bottom left")

fig_sensor.update_layout(
    title="Real-Time Sensor Data Monitoring",
    xaxis_title="Time",
    yaxis_title="Sensor Readings",
    legend_title="Sensors",
    hovermode="x unified"
)

fig_sensor.show()
```

### **Explanation:**
1. **Data Simulation:**
   - **Timestamps:** Every minute for one hour.
   - **Sensors:** Temperature, Humidity, and Pressure with simulated readings.

2. **Plotting:**
   - **Plotly Graph Objects (`go.Figure`):** Allows for more advanced customization.
   - **Multiple Traces:** Each sensor type is plotted as a separate trace with distinct colors.
   - **Threshold Lines:** Dashed lines indicate predefined thresholds for Temperature and Humidity to quickly identify anomalies.

### **Why Include This Example?**
IoT and sensor data monitoring are increasingly important in various industries. This example showcases how to handle real-time data, use multiple y-axes if needed, and highlight critical thresholds, which are essential for alert systems and real-time dashboards.

---

## **Tips for Your Tutorial Video:**

1. **Diverse Data Contexts:**
   - Presenting examples from different domains (finance, climate, web analytics, IoT) demonstrates Plotly's flexibility and wide applicability.

2. **Interactive Features:**
   - Emphasize Plotly's interactivity, such as hover information, zooming, and panning, to engage viewers and enhance data exploration.

3. **Customization Techniques:**
   - Showcase how to customize colors, line styles, markers, and layouts to make charts more informative and visually appealing.

4. **Data Preparation:**
   - Highlight the importance of preparing and structuring data appropriately before visualization. This includes data cleaning, aggregation, and transformation using libraries like Pandas.

5. **Real-World Applications:**
   - Relate each example to real-world scenarios to help viewers understand the practical applications of the visualizations.

6. **Code Walkthrough:**
   - Go through the code step-by-step, explaining each part to ensure viewers grasp both the how and the why behind each action.

7. **Encourage Experimentation:**
   - Prompt viewers to modify the examples, such as changing colors, adding more data series, or adjusting layouts, to reinforce learning through practice.

---

By incorporating these diverse examples and following the tips provided, your YouTube tutorial will offer a comprehensive guide to creating effective and interactive line charts using Plotly. This approach will cater to a wide audience, from beginners to more advanced users looking to enhance their data visualization skills.

Good luck with your tutorial!