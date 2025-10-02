import pandas as pd
import seaborn as sns
import matplotlib.pyplot as ply
import random

# Makes data
fNames = ["Richard", "Lucian", "Van", "Kyle", "Andrew", "Jack", "Danica", "Emma", "Amy", "Rosanne", "Scott", "Johnathan", "Eli", "Jill", "Jose"]
lNames = ["Smith", "Larson", "Jones", "Furgeson", "Campbell", "Wilson", "Garcia", "Curtis", "Roosevelt", "Thompson", "Watson", "Anderson", "Foster", "Davey", "MacDonald"]
years = ["Freshman", "Sophomore", "Junior", "Senior", "Super Senior"]
pathways = ["Early College", "Engineering", "Computer Science", "Business", "Marketing", "Early Childhood Education", "Culinary", "Criminal Justice", "Construction", "Bio Med"]
names = []

for i in range(200):
    names.append(f"{random.choice(fNames)} {random.choice(lNames)}")

print(names)
data = {
    "Name": names,
    "Age": [random.randint(14,19) for _ in names],
    "GPA": [round(random.uniform(0.3, 4.5),2) for _ in names],
    "Credits Completed": [random.randint(0, 60) for _ in names],
    "Year": [random.choice(years) for _ in names],
    "Pathway": [random.choice(pathways) for _ in names],
}
# Comment
pennData = pd.DataFrame(data)

pennData.to_csv("pennData.csv", index=False)



# load data frame
df = pd.read_csv("Survey.csv")
surveyData = pd.DataFrame(df)
print("-_"*20)
print("Head of the Dataframe") 
print(surveyData.head())