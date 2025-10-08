import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

# load data frame
df = pd.read_csv("Survey.csv")
surveyData = pd.DataFrame(df)
print("-_"*20)
print("Head of the Dataframe") 
print(surveyData.head())

print("-_"*20)
print("Tail of the Dataframe") 
print(surveyData.tail())


print("-_"*20)
print("Summary of the Dataframe") 
print(surveyData.info())


print("-_"*20)
print("Statistiics") 
print(round(surveyData.describe()))


print("-_"*20)
print("Count of Favorite Restaurants") 
print(surveyData['Favorite'].value_counts())

print("-_"*20)
print("Count of Least favorite restaurants") 
print(surveyData['Least Favorite'].value_counts())

print("-_"*20)
print("First Data Sample") 
print(surveyData.iloc[0] )

surveyData.groupby("Favorite")["Times Ate (MF)"].mean().plot(kind="bar", color="red")
plt.title("average times ate per favorite restaurants")
plt.xlabel("Favorite")
plt.ylabel("Times Ate (MF)")
plt.show()

surveyData.groupby("Least Favorite")["Times Ate (LF)"].mean().plot(kind="bar", color="red")
plt.title("average times ate per least favorite restaurants")
plt.xlabel("Least Favorite")
plt.ylabel("Times Ate (LF)")
plt.show()

surveyData["Times Ate (MF)"].plot(kind="hist", bins=5)
plt.title("Times Ate for Favorite")
plt.xlabel("Times Ate (MF)")
plt.ylabel("Frequency")
plt.show()

surveyData["Times Ate (LF)"].plot(kind="hist", bins=5)
plt.title("Times Ate for Least Favorite")
plt.xlabel("Times Ate (LF)")
plt.ylabel("Frequency")
plt.show()

# plt.scatter(surveyData("Credits Completed"), surveyData["GPA"])
# plt.title("GPA Distribution")
# plt.xlabel("GPA")
# plt.ylabel("Number of Students")
# plt.show()



# Made the data
# amount = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# most_Favorite = ["McDonalds", "Burger King", "Wendy's", "Arby's", "Chick fil-a", "Others", "KFC", "Culver's", "Popeye's"]
# least_Favorite = ["McDonalds", "Burger King", "Wendy's", "Arby's", "Chick fil-a", "Others", "KFC", "Culver's", "Popeye's"]
# calories = ["<1000", 1000, 2000, 2000, 3000, 3000, 4000, 4000, 5000, ">5000"]


# data = {
#     "Favorite": [random.choice(most_Favorite) for _ in amount],
#     "Times Ate (MF)": [random.randint(0,10)for _ in amount],
#     "Least Favorite": [random.choice(least_Favorite) for _ in amount],
#     "Times Ate (LF)": [random.randint(0,10) for _ in amount],
#     "Calories per meal": [random.choice(calories) for _ in amount],
# }

# surveyData = pd.DataFrame(data)
# print(surveyData)
# surveyData.to_csv("Survey.csv", index=False)



