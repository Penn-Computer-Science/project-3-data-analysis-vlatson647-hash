import pandas as pd
import seaborn as sns
import matplotlib.pyplot as ply
import random

# Makes data
amount = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
most_Favorite = ["McDonalds", "Burger King", "Wendy's", "Arby's", "Chick fil-a", "Others", "KFC", "Culver's", "Popeye's"]
least_Favorite = ["McDonalds", "Burger King", "Wendy's", "Arby's", "Chick fil-a", "Others", "KFC", "Culver's", "Popeye's"]
calories = ["<1000", 1000, 2000, 2000, 3000, 3000, 4000, 4000, 5000, ">5000"]


data = {
    "Favorite": [random.choice(most_Favorite) for _ in amount],
    "Times Ate (MF)": [random.randint(0,10)for _ in amount],
    "Least Favorite": [random.choice(least_Favorite) for _ in amount],
    "Times Ate (LF)": [random.randint(0,10) for _ in amount],
    "Calories per meal": [random.choice(calories) for _ in amount],
}

surveyData = pd.DataFrame(data)
print(surveyData)
surveyData.to_csv("Survey.csv", index=False)



# load data frame
# df = pd.read_csv("Survey.csv")
# surveyData = pd.DataFrame(df)
# print("-_"*20)
# print("Head of the Dataframe") 
# print(surveyData.head())