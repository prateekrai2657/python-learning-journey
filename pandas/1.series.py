# series is basically one dimesional array that can hold any data type||think like a column in a spread sheet
# import pandas as pd

# data = [100,102,104,106]

# # series = pd.Series(data)
# series = pd.Series(data,index=["a","b","c","d"])
# # series.loc["c"]=69

# # print(series)
# # print(series.loc["a"])
# print(series[series>102])

import pandas as pd

calories = {"Day 1": 1760,"Day 2" :2211,"Day 3":2300}

series = pd.Series(calories)
# print(series)

series.loc["Day 1"] += 600

print(series.loc["Day 1"])

print(series)
print(series[series>2300])


 