"""
Customer Churn: Causal Analysis of True Drivers
Author: Pratima Dhende
Dataset: Telco Customer Churn (Kaggle)
"""
# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import dowhy
from dowhy import CausalModel

# load dataset
df=pd.read_csv("Telco_Churn.csv")
print(df.head())

# data cleaning and preprocessing
# convert TotalCharges to numeric
df["TotalCharges"]=pd.to_numeric(df["TotalCharges"],errors="coerce")

# drop missing values
df.dropna(inplace=True)

# convert target variable
df["Churn"]=df["Churn"].map({"Yes":1,"No":0})

# drop customer ID 
df.drop(columns=["customerID"],inplace=True)

# encode categorical variables
label_encoder=LabelEncoder()
for col in df.select_dtypes(include="object").columns:
    df[col]=label_encoder.fit_transform(df[col])

# exploratory data analysis (EDA)
# churn distribution
sns.countplot(x="Churn",data=df)
plt.title("Churn Distribution")
plt.savefig("Churn_Distribution.png",dpi=300,bbox_inches="tight")
plt.show()

# Churn vs Contract Type
sns.barplot(x="Contract",y="tenure",hue="Churn",data=df)
plt.title("Churn vs Contract Type by Churn") 
plt.savefig("Churn vs Contract.png",dpi=300,bbox_inches="tight")
plt.show()

# Correlation Analysis
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(),cmap="coolwarm",linewidths=0.5)
plt.title("Correlation Heatmap")
plt.savefig("Correlation_analysis.png",dpi=300,bbox_inches="tight")
plt.show()

# define causal problem
"""Causal Questuion:
Does having a long-term contract reduce customer churn?

Treatment:Contract
Outcome:Churn
Confounders:tenure,MonthlyCharges,InternetService
"""
# Build Causal Model(dowhy)
Causal_Model=CausalModel(data=df,treatment="Contract",outcome="Churn",common_causes=["tenure","MonthlyCharges","InternetService"])
Causal_Model.view_model()
Causal_Model._graph.render("causal_model",format="png",cleanup=True)

# identify causal effect
identified_estimand=Causal_Model.identify_effect()
print(identified_estimand)

# estimate causal effect(ATE)
estimate=Causal_Model.estimate_effect(identified_estimand,method_name="backdoor.linear_regression")
print("Causal Effect (ATE): ",estimate.value)

# refutation tests(validation)
refutation=Causal_Model.refute_estimate(identified_estimand,estimate,method_name="placebo_treatment_refuter")
print(refutation)

# random confounder test 
refutation2=Causal_Model.refute_estimate(identified_estimand,estimate,method_name="random_common_cause")
print(refutation2)

# correlation vs causation comparison
corr_value=df["Contract"].corr(df["Churn"])
print("Correlation between Contract and Churn: ",corr_value)
print("Causal Effect (ATE): ",estimate.value)

# Final Bussiness Insight
if estimate.value < 0:
    print("Long-term contracts causally reduce customer churn.")
else:
    print("Contract type does not causally reduce churn.")

# save results
results={"Correlation":corr_value,"Causal_Effect_ATE":estimate.value}
pd.DataFrame([results]).to_csv("Causal_result.csv",index=False)