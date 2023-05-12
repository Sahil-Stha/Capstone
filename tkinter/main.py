import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('SuicideChina.csv')
df.dropna()
# Get general information about the dataset
df.info()

# Descriptive statistics of numerical columns
df.describe()

# Convert Dead to 0 1 format
df['Died'] = df['Died'].map({'no': 0, 'yes': 1})

# Define a function to create the Histogram of Ages by No of Deaths
def show_age_death_counts():
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Age'], kde=False, bins=20)
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.title('Distribution of Ages in Suicide Dataset')
    plt.show()  

# Define a function to create the bar chart of the UFO Suicide Rate by Gender
def show_suiciderate_gender_counts():
    plt.figure(figsize=(10, 15))
    sns.countplot(x='Sex', data=df,hue= 'Died')
    plt.xlabel('Gender')
    plt.ylabel('Number of Deaths')
    plt.title('Suicide Rates by Gender')
    plt.show()

# Define a function to create the SctterPlot of Age by Education Level
def show_age_education_distribution():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Age', y='Education', data=df)
    plt.xlabel('Age')
    plt.ylabel('Education Level')
    plt.title('Age versus Education Level')
    plt.show()

# Define a function to create the line chart of the number of UFO sightings by year
def show_suicide_occupation_counts():
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Occupation', y='Died', data=df)
    plt.xlabel('Occupation')
    plt.ylabel('Number of Deaths')
    plt.title('Suicide Rates by Occupation')
    plt.xticks(rotation=90)
    plt.show()

# Define a function to create the boxplot of UFO sighting durations
def show_suicide_rate():
    suicide_rates = df.groupby('Year')['Died'].sum().reset_index()
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Year', y='Died', data=suicide_rates)
    plt.xlabel('Year')
    plt.ylabel('Number of Deaths')
    plt.title('Suicide Rates Over Time')
    plt.xticks(rotation=90)
    plt.show()

# Create the tkinter GUI
root = tk.Tk()
root.title('Suicide Rate in China Data Exploration')

# Create the notebook
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Create the tabs
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Most Suicide According to Age')

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Suicide Rate by Gender')

tab3 = ttk.Frame(notebook)
notebook.add(tab3, text='Suicide as per Education')

tab4 = ttk.Frame(notebook)
notebook.add(tab4, text='Suicide Rates by Occupation')

tab5 = ttk.Frame(notebook)
notebook.add(tab5, text='Suicide Rate over Time')

# Add the widgets to the tabs
# Tab 1
#Add the widgets to Tab 1
label1 = ttk.Label(tab1, text='Most Suicide According to Age', font=('TkDefaultFont', 16))
label1.pack(padx=10, pady=10)

button1 = ttk.Button(tab1, text='Show Chart', command=show_age_death_counts)
button1.pack(padx=10, pady=10)

#Tab 2
#Add the widgets to Tab 2
label2 = ttk.Label(tab2, text='Most Suicide with Death as per Gender', font=('TkDefaultFont', 16))
label2.pack(padx=10, pady=10)

button2 = ttk.Button(tab2, text='Show Chart', command=show_suiciderate_gender_counts)
button2.pack(padx=10, pady=10)

#Tab 3
#Add the widgets to Tab 3
label3 = ttk.Label(tab3, text='Distribution of Age by Education Level', font=('TkDefaultFont', 16))
label3.pack(padx=10, pady=10)

button3 = ttk.Button(tab3, text='Show Chart', command=show_age_education_distribution)
button3.pack(padx=10, pady=10)


#Tab 4
#Add the widgets to Tab 4
label4 = ttk.Label(tab4, text='Number of Suicide as per Occupation', font=('TkDefaultFont', 16))
label4.pack(padx=10, pady=10)

button4 = ttk.Button(tab4, text='Show Chart', command=show_suicide_occupation_counts)
button4.pack(padx=10, pady=10)

#Tab 5
#Add the widgets to Tab 5
label5 = ttk.Label(tab5, text='Distribution of Deaths over Year', font=('TkDefaultFont', 16))
label5.pack(padx=10, pady=10)

button5 = ttk.Button(tab5, text='Show Chart', command=show_suicide_rate)
button5.pack(padx=10, pady=10)

#Run the GUI
root.mainloop()