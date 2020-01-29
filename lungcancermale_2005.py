## Importing packages 
import plotly.express as px
import pandas as pd

## Importing CSV file from desktop
df = pd.read_csv("~/Desktop/rstat/lungcancer_2005.csv")

figure = px.scatter(df, x="Percentage_of_smokers", y="Death", color="Continent", hover_data=['Continent'])

figure.update_layout(title='Graph of Percentage of male smokers vs Number of death in males with lung cancer in 2005')

figure.show()







