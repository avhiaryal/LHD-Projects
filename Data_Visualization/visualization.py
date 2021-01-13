#COVID-19 Data Visualization using matplotlib in Python
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('D:\GitHub Repositories\LHD-Projects\Data_Visualization\case_time_series.csv')

Y = data.iloc[61:,1].values #stores daily confirmed
R = data.iloc[61:,3].values #stores daily recovered
D = data.iloc[61:,5].values #stores daily recoverd
X = data.iloc[61:,0].values #stores dates

#creating canvas for the graph
plt.figure(figsize=(30,10)) #30=width and 10=height arguments position of graph

#creating object of the axes of the graph as ax to make it easir to implement functions
ax = plt.axes()

ax.grid(linewidth=0.4,color='black') #grid function crete grid lines in graph
ax.set_facecolor("teal") #set_facecolor function sets the backgrounf colorof the graph
ax.set_xlabel('\nDate', size=7, color='red') #set label for x axes
ax.set_ylabel("Number of Confirmed Cases \n", size=10,color='red') #set label for y axes


plt.xticks(rotation='vertical',size='7',color='black') 
plt.yticks(size=7,color='black') 
plt.tick_params(size=7,color='black')

for i,j in zip(X,Y): 
    ax.annotate(str(j),xy=(i,j+100),color='white',size='7')   

plt.title("COVID-19: Daily Confrimed\n", size=10,color='skyblue') 
ax.plot(X,Y,
        color='red',
        marker='o',
        linewidth=4,
        markersize=15,
        markeredgecolor='red'
        )

plt.show()