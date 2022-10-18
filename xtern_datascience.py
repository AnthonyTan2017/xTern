# -*- coding: utf-8 -*-
"""Xtern dataScience.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dW1qpI8bOjnibuOi3uZADRBsZAibY5uk
"""

pip install -U googlemaps

AIzaSyCoUqQYV41COJSFft6SDChlbDZZ84SJcbc

AIzaSyDyycuzhKtyHuHEOQjrVzbvjlomP65cbGk atta

import pandas as pd
df = pd.read_csv("xternDataScience.csv")
df2=df.groupby('Type')
df2.groups
for name, group in df2:
    print(name)
    # print(group)
    print()
df2.get_group("park")
# df2.get_group("premise")
# df2.get_group("point_of_interest")
# df2.get_group("tourist_attraction")
# df.sort_values("rating",ascending = 0)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("xternDataScience.csv")
df2=df.groupby('Type')
df2.groups
for name, group in df2:
    print(name)
    print()
gp2 =df2.get_group("tourist_attraction").sort_values(by='rating', ascending=False)
gp=gp2.drop_duplicates()
# https://datatofish.com/remove-duplicates-pandas-dataframe/

sns.set_style('whitegrid')
# Construct plot
a =sns.barplot(x = gp.index, y = "rating", data = gp,order=gp.sort_values('rating',ascending = True).index)
ticks = [4, 4.1, 4.2, 4.3,4.4,4.5,4.6,4.7,4.8,4.9,5]
a.set_yticks(ticks)
a.set_yticklabels(ticks)
plt.ylim(4, 5)
plt.xlabel('Index')
# https://aihints.com/how-to-change-y-axis-scale-in-seaborn/
plt.show()

# df.sort_values("rating",ascending = 0)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("xternDataScience.csv")
df2=df.groupby('Type')
df2.groups
# for name, group in df2:
#     print(name)
#     print()
gp2 =df2.get_group("restaurant").sort_values(by='rating', ascending=False)
gp=gp2.drop_duplicates()
# https://datatofish.com/remove-duplicates-pandas-dataframe/

sns.set_style('whitegrid')
# Construct plot
a =sns.barplot(x = gp.index, y = "rating", data = gp,order=gp.sort_values('rating',ascending = True).index)
ticks = [4, 4.1, 4.2, 4.3,4.4,4.5,4.6,4.7,4.8,4.9,5]
a.set_yticks(ticks)
a.set_yticklabels(ticks)
plt.ylim(4, 5)
plt.xlabel('Index')
# https://aihints.com/how-to-change-y-axis-scale-in-seaborn/
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("xternDataScience.csv")
df2=df.groupby('Type')
df2.groups
# for name, group in df2:
#     print(name)
#     print()
gp2 =df2.get_group("restaurant").sort_values(by='rating', ascending=False)
gp=gp2.drop_duplicates()
# https://datatofish.com/remove-duplicates-pandas-dataframe/

sns.set_style('whitegrid')
# Construct plot
a =sns.barplot(x = gp.index, y = "rating", data = gp,order=gp.sort_values('rating',ascending = True).index)
ticks = [4, 4.1, 4.2, 4.3,4.4,4.5,4.6,4.7,4.8,4.9,5]
a.set_yticks(ticks)
a.set_yticklabels(ticks)
plt.ylim(4, 5)
plt.xlabel('Index')
# https://aihints.com/how-to-change-y-axis-scale-in-seaborn/
plt.show()