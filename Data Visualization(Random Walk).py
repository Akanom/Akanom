#!/usr/bin/env python
# coding: utf-8

# <h1>Data Visualization Using Matplotlib</h1>
# <h2>Description</h2>
# <p>In this project, I will be exploring data through data visualisation. Codes will be used to explore the patterns and connections in a dataset. Matplotlib will be imported and used to make simple plots. Plotly will be used to make visualization that work well on digital devices. </p>

# In[1]:


import matplotlib
import matplotlib.pyplot as plt


# <h2>Plotting a simple Line Graph</h2>

# In[2]:


x_input=[1,2,3,4,5]
squares= [1,4,9,16,25]
plt.style.use("seaborn")#change the style used for plotting the graph
fig,ax=plt.subplots(figsize=(18,12), dpi=130)
ax.plot(x_input,squares, linewidth=5, c="red")
ax.set_title("Square numbers", fontsize=20)#set the title of the graph
ax.set_xlabel("Values",fontsize=10)#set the x_axis
ax.set_ylabel("Squares")#set the y_axis
ax.tick_params(axis="both",labelsize=10)#set the thick
plt.show()


# <h2>Calculating Data Automatically</h2>

# <p>A loop will be used to generate data points automatically</p>

# In[3]:


x_data=range(1,100)#range of value 1 to 100
y_data=[x**2 for x in x_data]#looping through x_axis to generate its sqaures
plt.style.use("seaborn")
fig,ax=plt.subplots(figsize=(18,12), dpi=130)
ax.scatter(x_data,y_data,s=10, linewidth=5, c=y_data, cmap=plt.cm.Reds)#using color map
ax.set_title("Square numbers", fontsize=20)#set the title of the graph
ax.set_xlabel("Values",fontsize=10)#set the x_axis
ax.set_ylabel("Squares")#set the y_axis
ax.tick_params(axis="both",labelsize=10)#set the thick
ax.axis([0,103,0,10000])
plt.show()


# <h2>Random Walk</h2>
# <p>This section will use python to generate a random walk data, and the visualize it using matplotlib. The random walk data creates a path that is not clear by a series of random decisions, theses decisions are left to chance.</p>

# In[4]:


from random import choice
class RandomWalk:
    """Make a random decision on the decision to take"""
    def __init__(self, random_points=10_000): # default number of random walk
        """The attribute of the walk is initialized"""
        self.random_points=random_points
        #All the walk must start from zero (0,0)
        self.x_data=[0] #list to hold x data
        self.y_data=[0] #list to hold y data
    
    def fill_walk(self):
        """Used to calculate all the walk and determine the direction"""
        while len(self.x_data)<self.random_points:#continue taking step until you reach the desired lenght
            x_direction=choice([1,-1])#decide on the direction to go, and how to go in this direction
            x_distance=choice([0,1,2,3,4,5,6,7,8,9,10])
            x_step=x_direction*x_distance
        
            y_direction=choice([1,-1])
            y_distance=choice([0,1,2,3,4,5,6,7,8,9,10])
            y_step=y_direction*y_distance
        
            if x_step==0 and y_step==0:#reject steps that go nowhere
                continue
        
            x=self.x_data[-1]+x_step
            y=self.y_data[-1]+y_step
        
            self.x_data.append(x)
            self.y_data.append(y)
        


# <h3>Plot the generated data</h3>

# In[ ]:


while True:#keep making new walk as long as the program is active
    random_walk=RandomWalk(50000)
    random_walk.fill_walk()
    plt.style.use("classic")
    fig,ax=plt.subplots(figsize=(18,12), dpi=130)
    numbers=range(random_walk.random_points)
    ax.scatter(random_walk.x_data, random_walk.y_data, s=10, c=numbers, cmap=plt.cm.Reds,
              edgecolors="none")
    ax.scatter(0,0,c="blue", edgecolors="none", s=80)#emphasis the first and last point
    ax.scatter(random_walk.x_data[-1], random_walk.y_data[-1],
               c="green",edgecolors="none",s=80)#end point
    ax.get_xaxis().set_visible(False)#remove the thick of the axis
    ax.get_yaxis().set_visible(False)
    plt.show()
    
    keep_running=input("Make another walk? (y/n):")
    if keep_running=="n":
        break


# <h2>About the Author:</h2>
# <p><a href="https://www.linkedin.com/in/oluwajuwon-mayomi-akanbi"><b>Akanbi Oluwajuwon Mayomi<b></a> has a Master's degree in Economics, his interest are data science, web development, and researchs on international economics </p>

# <h2>Reference</h2>
# <p>Matthes, Eric (2015). Python crash course: A hands-on, project-based introduction to programming. no starch press. page 305-322</p>
