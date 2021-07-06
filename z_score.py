import statistics
import random
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv('Graph Visualization 2/School1.csv')
data = df["Math_score"].tolist()
mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print(std_deviation, mean)

def random_setof_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range (0,1000):
    set_ofmeans = random_setof_mean(100)
    mean_list.append(set_ofmeans)

standard_deviation = statistics.stdev(mean_list)
first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start, second_std_deviation_end = mean - 2 * std_deviation, mean + 2 * std_deviation
third_std_deviation_start, third_std_deviation_end = mean - 3 * std_deviation, mean + 4 * std_deviation



df = pd.read_csv("Graph Visualization 2/School_1_Sample.csv")
data = df["Math_score"].tolist()
mean_ofsample1 = statistics.mean(data)

fig = ff.create_distplot([mean_list], ['Math_score'], show_hist = False)
print("Standard Deviation 1: ", first_std_deviation_start, first_std_deviation_end)
print("Standard Deviation 2: ", second_std_deviation_start, second_std_deviation_end)
print("Standard Deviation 3: ", third_std_deviation_start, third_std_deviation_end)

fig = ff.create_distplot([mean_list], ['Math_score'], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [first_std_deviation_start, first_std_deviation_start], y = [0,0.17],  mode = "lines", name = "Standard deviation 1 start"))
fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0,0.17],  mode = "lines", name = "Standard deviation 1 end"))
fig.add_trace(go.Scatter(x = [second_std_deviation_start, second_std_deviation_start], y = [0,0.17],  mode = "lines", name = "Standard deviation 2 start"))
fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0,0.17],  mode = "lines", name = "Standard deviation 2 end"))
fig.add_trace(go.Scatter(x = [third_std_deviation_start, third_std_deviation_start], y = [0,0.17],  mode = "lines", name = "Standard deviation 3 start"))
fig.add_trace(go.Scatter(x = [third_std_deviation_end, third_std_deviation_end], y = [0,0.17],  mode = "lines", name = "Standard deviation 3 end"))



df = pd.read_csv("Graph Visualization 2/School_2_Sample.csv")
data = df["Math_score"].tolist()
mean_ofsample2 = statistics.mean(data)

fig = ff.create_distplot([mean_list], ['Math_score'], show_hist = False)
print("Standard Deviation 1: ", first_std_deviation_start, first_std_deviation_end)
print("Standard Deviation 2: ", second_std_deviation_start, second_std_deviation_end)
print("Standard Deviation 3: ", third_std_deviation_start, third_std_deviation_end)

fig = ff.create_distplot([mean_list], ['Math_score'], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [first_std_deviation_start, first_std_deviation_start], y = [0,0.17],  mode = "lines", name = "Standard deviation 1 start"))
fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0,0.17],  mode = "lines", name = "Standard deviation 1 end"))
fig.add_trace(go.Scatter(x = [second_std_deviation_start, second_std_deviation_start], y = [0,0.17],  mode = "lines", name = "Standard deviation 2 start"))
fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0,0.17],  mode = "lines", name = "Standard deviation 2 end"))
fig.add_trace(go.Scatter(x = [third_std_deviation_start, third_std_deviation_start], y = [0,0.17],  mode = "lines", name = "Standard deviation 3 start"))
fig.add_trace(go.Scatter(x = [third_std_deviation_end, third_std_deviation_end], y = [0,0.17],  mode = "lines", name = "Standard deviation 3 end"))



df = pd.read_csv("Graph Visualization 2/School_3_Sample.csv")
data = df["Math_score"].tolist()
mean_ofsample3 = statistics.mean(data)

fig = ff.create_distplot([mean_list], ['Math_score'], show_hist = False)
print("Standard Deviation 1: ", first_std_deviation_start, first_std_deviation_end)
print("Standard Deviation 2: ", second_std_deviation_start, second_std_deviation_end)
print("Standard Deviation 3: ", third_std_deviation_start, third_std_deviation_end)

fig = ff.create_distplot([mean_list], ['Math_score'], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [first_std_deviation_start, first_std_deviation_start], y = [0,0.17],  mode = "lines", name = "Standard deviation 1 start"))
fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0,0.17],  mode = "lines", name = "Standard deviation 1 end"))
fig.add_trace(go.Scatter(x = [second_std_deviation_start, second_std_deviation_start], y = [0,0.17],  mode = "lines", name = "Standard deviation 2 start"))
fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0,0.17],  mode = "lines", name = "Standard deviation 2 end"))
fig.add_trace(go.Scatter(x = [third_std_deviation_start, third_std_deviation_start], y = [0,0.17],  mode = "lines", name = "Standard deviation 3 start"))
fig.add_trace(go.Scatter(x = [third_std_deviation_end, third_std_deviation_end], y = [0,0.17],  mode = "lines", name = "Standard deviation 3 end"))


z_score = (mean - mean_ofsample2)/ std_deviation
print("the Z score is: ", z_score)