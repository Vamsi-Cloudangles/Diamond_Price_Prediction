from feature_engineering import Featureengineering

def Featureselecton():
    data = Featureengineering()
    # Removing the unnecessary coloumns and add anything other needed.
    # The first column seems to be just index
    data = data.drop(["SI.NO"], axis=1)
    data.describe()
    # Save the cleanedn dataframe in csv format.
    data.to_csv("Dimond_Price_Prediction_Cleaned_Dataset.csv", index = False)
    return data
Featureselecton()