# FIFA-World-Cup-Dashboard
World Cup Winners Dashboard
📊 Project Overview
This project presents an interactive dashboard that allows users to explore the history of FIFA World Cup winners. The dashboard allows users to:

View countries that have won the World Cup and the number of wins.

Select a specific year and see the winner and runner-up for that year.

Visualize the World Cup winners using a choropleth map, color-coded based on the number of wins.

The project uses Dash and Plotly to create an interactive web application with features such as dropdown selection and dynamic data updates.

Dataset:
The dataset includes the following columns:

Year: The year the World Cup was held.

Winners: The country that won the World Cup in that year.

Runners-up: The country that finished as the runner-up in that year.

Host: The country that hosted the World Cup.

💻 Technologies Used
Python: The primary language used to develop the dashboard.

Dash: A Python framework for building web applications.

Plotly: Used for creating interactive visualizations like the choropleth map.

Pandas: For data manipulation and processing.

HTML/CSS: For styling the layout and design of the dashboard.

📂 Getting Started
Prerequisites:
Before running the code, make sure you have Python and the necessary libraries installed.

Install Python: Download Python from python.org.

Install required libraries: Run the following command to install the necessary libraries:

bash
Copy
Edit
pip install dash pandas plotly
Download or clone the project: Clone the repository or download the files to your local machine.

Run the application: To start the dashboard, run the following command in the terminal:

bash
Copy
Edit
python app.py
This will launch a local server and you can view the dashboard by visiting http://127.0.0.1:8050/ in your browser.

Data File:
The dataset used in this project is embedded within the code, but if you want to load your own data, update the DataFrame initialization with the path to your custom CSV file.

Editing the Dashboard:
The dashboard is built using Dash. You can edit the layout and functionality by modifying the app.layout section and adding more callbacks as needed.

To run and edit the project in a more interactive environment, it's recommended to use Jupyter Lab:

bash
Copy
Edit
pip install jupyterlab
jupyter lab
