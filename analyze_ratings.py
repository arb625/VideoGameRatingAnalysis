import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

users_scores = []
critic_scores = []
global_sales_values = []
with open('Video_Games_Sales_as_at_22_Dec_2016.csv', 'r') as csvfile:
    row_reader = csv.DictReader(csvfile)
    for row in row_reader:
        user_score = row["User_Score"]
        critic_score = row["Critic_Score"]
        global_sales_value = row["Global_Sales"] 

        if is_number(user_score) and is_number(critic_score) and is_number(global_sales_value):  #make sure both scores are numbers
            users_scores.append(float(user_score))
            critic_scores.append(float(critic_score))
            global_sales_values.append(float(global_sales_value))
            
users_vs_critics_scores = np.polyfit(users_scores, critic_scores, 1)  #deg = 1: least squares linear regression

plt.subplot(2,1,1)
plt.title("User Scores vs Critic Scores for Video Games")
plt.ylabel("Critic Score")
plt.plot(users_scores, critic_scores, 'o')  #plot actual data points
plt.plot(users_scores, np.polyval(users_vs_critics_scores, users_scores), 'r')  #plot line of best fit

users_scores_vs_global_sales = np.polyfit(users_scores, global_sales_values, 1)  #deg = 1: least squares linear regression

plt.subplot(2,1,2)
plt.title("User Scores vs Global Sales for Video Games")
plt.xlabel("User Score")
plt.ylabel("Global Sales")
plt.plot(users_scores, global_sales_values, 'g+')  #plot actual data points
plt.plot(users_scores, np.polyval(users_scores_vs_global_sales, users_scores), 'r')  #plot line of best fit

plt.show()

df = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')

def mean_of_col(df, col_name):
    return pd.to_numeric(df[col_name], errors='coerce').mean()

print("Average User Score:", mean_of_col(df, "User_Score"))
print("Average Critic Score:", mean_of_col(df, "Critic_Score"), "\n")

print("Average Critic Scores by Genre")
print(df.groupby("Genre").mean()["Critic_Score"].sort_values(ascending=False))
print()

print("Average Critic Scores by Platform")
print(df.groupby("Platform").mean()["Critic_Score"].sort_values(ascending=False))
print()

print("Average Critic Scores by Publisher")
print(df.groupby("Publisher").mean()["Critic_Score"].sort_values(ascending=False))
print()