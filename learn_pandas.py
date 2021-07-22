import pandas as pd
import matplotlib.pyplot as plt
test_data = pd.read_csv('statsnz_test.csv')
#print(test_data.head())
counts = test_data.groupby("Year").Value.sum()
counts.plot.bar
plt.show()
