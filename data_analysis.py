from load_data import Data_extraction

def Dataanalysis():
    dataset = Data_extraction()
   # Providing the details of data 
    print(dataset.columns)
    print(dataset.head())
    print(dataset.shape)
    print(dataset.dtypes)
    print(dataset.info())
    print(dataset.describe)
    print(dataset.isnull().sum())
    for col in dataset.columns:
        print(col, len(dataset[col].unique()))
    return dataset
Dataanalysis()