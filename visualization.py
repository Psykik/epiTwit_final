#small script to visualize latest count of query result
    #while the query script to create the file we read no longer works, the most recent iteration of count.yaml was kept for demonstration purposes
import yaml
import matplotlib.pyplot as plt

#load in .yaml file
with open('count.yaml') as f:
    data = yaml.safe_load(f)

queries = list(data.keys())
counts = list(data.values())

figure = plt.figure(figsize=(10,5))
plt.bar(queries, counts, color ='teal', width = 0.8)
 
plt.xlabel("Queries used")
plt.ylabel("No. of tweets returned")
plt.title("Number of tweets returned for each query (250 tweet limit)")
plt.xticks(range(len(queries)), queries, rotation=70,fontsize = 16) #rotates bar labels so that they don't overlap as easily
plt.show()