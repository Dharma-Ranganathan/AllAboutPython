print()
print("self work based on overall concepts done so far...")
print()

# import statements
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import time as t

"""
Target : get inputs from user and do operations using libraries...
"""
# helper functions

# 1. make_list_dataset
def make_list_dataset():
    x = np.array([])
    y = np.array([])

    # getting inputs from user to append in x,y
    for i in range(0,5):
        x_inp = input(f"enter x{i+1}: ").strip()
        y_inp = input(f"enter y{i+1}: ").strip()

        # checking data type entered in inputs
        if x_inp.isnumeric():
            x_inp = float(x_inp)
        else:
            x_inp = str(x_inp)

        if y_inp.isnumeric():
            y_inp = float(y_inp)
        else:
            y_inp = str(y_inp)

        x = np.append(x,x_inp)
        y = np.append(y,y_inp)

    return x,y

# labels and titles from user
def labels_title():
    title = input('Enter title for chart : ').strip().capitalize()
    labelX = input('Enter xLabel name for chart : ').strip().capitalize()
    labelY = input('Enter yLabel name for chart : ').strip().capitalize()

    return title,labelX,labelY


# line_chart_by_list
def line_chart_by_list(x,y):
    # getting labels and titles from user
    title,labelX,labelY = labels_title()
    # line format - marker|line|color - "d--r" - 'd - diamond','-- - dashed','r - red'
    plt.plot(x,y,'o-r')
    plt.title(title)
    plt.xlabel(labelX)
    plt.ylabel(labelY)
    print()
    print('Creating your line chart ready...')
    plt.show()


# bar_chart_by_list
def bar_chart_by_list(x,y):
    # getting labels and titles from user
    title,labelX,labelY = labels_title()

    # bar chart contains border - edgecolor, width of border - linewidth, each bar in chart contains 'X' like pattern
    plt.bar(x,y,color='#00ffce',edgecolor='green',linewidth=.8,hatch='X')
    plt.title(title)
    plt.xlabel(labelX)
    plt.ylabel(labelY)
    print()
    print('Creating your bar chart ready...')
    plt.show()

# scatter_chart_by_list
def scatter_chart_by_list(x,y):
    # getting labels and titles from user
    title,labelX,labelY = labels_title()

    # scatter chart - takes marker as param extra as same as bar chart does
    plt.scatter(x,y,color='#ff0000',marker='x')
    plt.title(title)
    plt.xlabel(labelX)
    plt.ylabel(labelY)
    print()
    print('Creating your scatter chart ready...')
    plt.show()

# pie_chart_by_list
def pie_chart_by_list(x,y):
    # getting labels and titles from user
    title,labelX,labelY = labels_title()

    explode = [.1,.1,.1,.1,.1]
    colors = ['#00ffce','#ff00ce','#00ceff','#ce00ff','#ceff00']
    # pie chart - takes explode as param in int
    plt.pie(y,labels=x,colors=colors,autopct='%1.1f%%',explode=explode)
    plt.title(title)
    plt.xlabel(labelX)
    plt.ylabel(labelY)
    print()
    print('Creating your pie chart ready...')
    plt.show()


# graph choices from user
def graph_choices_by_list(x,y):
    print()
    print("Getting you available charts ready...")
    t.sleep(2)

    while True:
        print()
        print('1. Line Chart')
        print('2. Bar Chart')
        print('3. Scatter Chart')
        print('4. Pie Chart')
        print('5. Return back')
        print()

        ch = input("enter choice number : ").strip()

        if ch.isalpha():
            print("Only numbers are allowed...")
            print("Returning back...")
            return
        if ch == '1':
            line_chart_by_list(x,y)
            # pass
        elif ch == '2':
            bar_chart_by_list(x,y)
            # pass
        elif ch == '3':
            scatter_chart_by_list(x,y)
            # pass
        elif ch == '4':
            pie_chart_by_list(x,y)
            # pass
        elif ch == '5':
            print("Returning back...")
            t.sleep(2)
            return
        else:
            print("Invalid choice selection...")
            print("Returning back...")
            return

# 2. make_dict_dataset
def make_dict_dataset():
    seab = {
        'x':[],
        'y':[]
    }
    print()
    print("if you are going to use hist plot, don't need to give inputs, just leave it empty and press ENTER...")
    print()
    # getting inputs from user to append in x,y
    for i in range(0,5):
        x_inp = input(f"enter x{i+1}: ").strip()
        y_inp = input(f"enter y{i+1}: ").strip()

        # checking data type entered in inputs
        if x_inp.isnumeric():
            x_inp = float(x_inp)
        else:
            x_inp = str(x_inp)

        if y_inp.isnumeric():
            y_inp = float(y_inp)
        else:
            y_inp = str(y_inp)

        seab['x'].append(x_inp)
        seab['y'].append(y_inp)

    df = pd.DataFrame(seab)
    return df

# line_chart_by_dict
def line_chart_by_dict(df):

    # getting labels and titles
    title,labelX,labelY = labels_title()

    # creating line plot using seaborn
    sns.lineplot(x='x',y='y',data=df,color='#ceff00')
    plt.title(title)
    plt.xlabel(labelX)
    plt.ylabel(labelY)
    plt.show()

# bar_chart_by_dict
def bar_chart_by_dict(df):

    # getting labels and titles
    title,labelX,labelY = labels_title()

    # creating bar plot using seaborn
    colors = ['#00ffce','#ff00ce','#00ceff','#ce00ff','#ceff00']

    sns.barplot(x='x',y='y',data=df,palette=colors,hue='y')
    plt.title(title)
    plt.xlabel(labelX)
    plt.ylabel(labelY)
    plt.show()

# scatter_chart_by_dict
def scatter_chart_by_dict(df):

    # getting labels and titles
    title,labelX,labelY = labels_title()

    # creating scatter plot using seaborn
    sns.scatterplot(x='x',y='y',data=df,palette='Set2',markers='X',hue='y')
    plt.title(title)
    plt.xlabel(labelX)
    plt.ylabel(labelY)
    plt.show()
    

# hist_plot_by_dict
def hist_plot_by_dict(df):

    # getting loaded dataset inbuilt from seaborn
    datas = sns.load_dataset('tips')
    df = pd.DataFrame(datas)

    # getting labels and titles
    title,labelX,labelY = labels_title()

    # creating hist plot using seaborn
    sns.histplot(df['total_bill'],kde=True,color='#ff00ce')
    plt.title(title)
    plt.xlabel(labelX)
    plt.ylabel(labelY)
    plt.show()



# graph choices from user
def graph_choices_by_dict(df):
    print()
    print("Getting you available charts ready...")
    t.sleep(2)

    while True:
        print()
        print('1. Line Plot')
        print('2. Bar Plot')
        print('3. Scatter Plot')
        print('4. Hist Plot')
        print('5. Return back')
        print()

        ch = input("enter choice number : ").strip()

        if ch.isalpha():
            print("Only numbers are allowed...")
            print("Returning back...")
            return
        if ch == '1':
            line_chart_by_dict(df)
            
        elif ch == '2':
            bar_chart_by_dict(df)
            
        elif ch == '3':
            scatter_chart_by_dict(df)
            
        elif ch == '4':
            hist_plot_by_dict(df)

        elif ch == '5':
            print("Returning back...")
            t.sleep(2)
            return
        else:
            print("Invalid choice selection...")
            print("Returning back...")
            return


def dataset_helper1():
    
    while True:
        print()
        print("choose one dataset type below: ")
        print("1. Array / List dataset for matplotlib")
        print("2. Dictionary dataset for seaborn")
        print("3. Return back")
        print()

        ch = input('enter dataset number : ').strip()

        if ch.isalpha():
            print("choices should not be number...")
            return
        if ch == '1':
            x,y = make_list_dataset()
            graph_choices_by_list(x,y)
        elif ch == '2':
            df = make_dict_dataset()
            graph_choices_by_dict(df)
        elif ch == '3':
            print("Returning back...")
            t.sleep(2)
            return
        else:
            print("Invalid choice selection...")
            return


# functions to do operations
# 1. create dataset
def create_dataset():
    dataset_helper1()



while True:
    print()
    print("1. Create Dataset")
    print("2. Quit")
    print()

    ch = input("Enter operations number : ").strip()

    if ch.isalpha():
        print("choice should not be numbers...")
        break
    if ch == '1':
        create_dataset()

    elif ch == '2':
        print("Quitting the program...")
        t.sleep(2)
        break
    else:
        print("Due to Invalid choice selection, we are quitting the program...")
        t.sleep(2)
        print('Re-run if you want to try again...')
        break

