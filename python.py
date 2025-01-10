import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Correct URL to the raw CSV file
url = "https://raw.githubusercontent.com/shahrzadhsh/Analysis-with-python/main/auto.csv"
# Reading the CSV from the URL
df = pd.read_csv(url)
# Displaying the first 5 rows
print(df.head(5))
