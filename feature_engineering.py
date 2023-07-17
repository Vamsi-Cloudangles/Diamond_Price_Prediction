from  data_preprocessing import data_preprocessing
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

def Featureengineering():
    # Removing the outliers
    data = data_preprocessing() 
    data = data[(data["depth"]<75)&(data["depth"]>45)]
    data = data[(data["table"]<80)&(data["table"]>40)]
    data = data[(data["x"]<30)]
    data = data[(data["y"]<30)]
    data = data[(data["z"]<30)&(data["z"]>2)]

    # Changing the catregorical values to numerical values
    for col in data.select_dtypes(include="object").columns:
        data[col] = le.fit_transform(data[col])
    return data
Featureengineering()           

