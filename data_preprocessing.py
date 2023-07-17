from data_analysis import Dataanalysis

def data_preprocessing():
    dataset = Dataanalysis()
    # removing the duplicates from the dataset
    duplicate = dataset[dataset.duplicated()]
    for i in duplicate.index:
        print("index", i) 
        dataset.drop(index = [i], inplace = True)
        dataset.reset_index()
    # Removing the x, y, z dimension values which are equal to 0
    dataset = dataset.drop(dataset[dataset["x"]==0].index)
    dataset = dataset.drop(dataset[dataset["y"]==0].index)
    dataset = dataset.drop(dataset[dataset["z"]==0].index)
    return dataset
data_preprocessing()