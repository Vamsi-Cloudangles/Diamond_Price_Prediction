import seaborn as sns
import matplotlib.pyplot as plt
from data_preprocessing import data_preprocessing

def data_visualization():
    dataset = data_preprocessing()
    print(dataset.head())
    # Histogram plots ....................
    sns.histplot(dataset['cut'])
    plt.show()
    sns.histplot(dataset['color'])
    plt.show()
    sns.histplot(dataset['clarity'])
    plt.show()

    # Count plots ..................
    sns.countplot(x='cut',data=dataset)
    plt.show()
    sns.countplot(x='color',data=dataset)
    plt.show()
    sns.countplot(x='clarity',data=dataset)
    plt.show()

    # Distribution plots ..............
    plt.subplots(1,1, figsize=(8,4))
    sns.distplot(x = dataset['carat'])
    plt.xlabel('carat')
    plt.show()
    plt.subplots(1,1, figsize=(8,4))
    sns.distplot(x = dataset['depth'])
    plt.xlabel('depth')
    plt.show()
    plt.subplots(1,1, figsize=(8,4))
    sns.distplot(x = dataset['table'])
    plt.xlabel('table')
    plt.show()

    # Scatter Plots .................
    plt.scatter(dataset['x'], dataset['y'])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    plt.scatter(dataset['y'], dataset['z'])
    plt.xlabel('y')
    plt.ylabel('z')
    plt.show()
    plt.scatter(dataset['z'], dataset['x'])
    plt.xlabel('z')
    plt.ylabel('x')
    plt.show()
    plt.scatter(dataset['carat'], dataset['depth'])
    plt.xlabel('carat')
    plt.ylabel('depth')
    plt.show()

    # Box plots ...................
    plt.subplots(1,1, figsize=(5,5))
    sns.boxplot(dataset['carat'])
    plt.xlabel('Carat')
    plt.show()
    plt.subplots(1,1, figsize=(5,5))
    sns.boxplot(dataset['depth'])
    plt.xlabel('Depth')
    plt.show()
    plt.subplots(1,1, figsize=(5,5))
    sns.boxplot(dataset['table'])
    plt.xlabel('Table')
    plt.show()
    plt.subplots(1,1, figsize=(5,5))
    sns.boxplot(dataset['x'])
    plt.xlabel('x')
    plt.show()
    plt.subplots(1,1, figsize=(5,5))
    sns.boxplot(dataset['y'])
    plt.xlabel('y')
    plt.show()
    plt.subplots(1,1, figsize=(5,5))
    sns.boxplot(dataset['z'])
    plt.xlabel('z')
    plt.show()

    #correlation matrix
    cmap = sns.diverging_palette(70,20,s=50, l=40, n=6,as_cmap=True)
    corrmat = dataset.corr()
    f, ax = plt.subplots(figsize=(12,12))
    sns.heatmap(corrmat,cmap=cmap,annot=True, )
    plt.show()

data_visualization()