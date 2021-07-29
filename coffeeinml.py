import plotly.express as px
import csv

with open("week,Coffee in ml,sleep in hours.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x = "Coffee in ml", y = "Sleep in hours")
    fig.show()