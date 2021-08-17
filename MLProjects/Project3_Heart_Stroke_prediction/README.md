**Patient Heart Stroke Prediction**

***Dataset source :*** https://www.kaggle.com/fedesoriano/stroke-prediction-dataset

***Problem Statement:***

According to the WHO, stroke is the 2nd leading cause of death globally.
Stroke is responsible for approximately 11% of total deaths in the world.
The dataset is provided to predict whether a patient is likely to get stroke or not on the basis of given input parameters :
Input parameters : (gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, Average_glucose_level,bmi and smoking_status)
The target variable is to predict whether the patient is likely to get storke or not.
Surfacely, it looks like a binary classification problem.

		
 
***Insights From Univariate Analysis***
 
***Categorical Columns***
 
<li>58.6% of people are female and 41.4% female are males and almost 0% of people belong to the other gender.</li>

65.6% of people are married and 34.4% of people are unmarried.
50.8% of people are living in Urban areas whereas 49.2% of people are living in Rural areas.
57.2 % of people work in private companies, 16 % of people are self-employed and 12.9 % of people work in government jobs whereas 13.4 % of people are children and 0.4 % of people have never worked.
37 % of people never smoked, 30.2 % of people's smoking status is unknown whereas 17.3 % of people smoking status are formerly smoken and 15.4 % are regular smokers.
We have 498 patients with hypertension which represents at around 10 % of the sample.
More than 90% of the sample represent the people with no hypertension in the datasets.
We have 276 patients with heart disease which is 5.4 % of the sample.
More than 94% of samples belong to the people with no heart disease.
 
Numerical Columns
 
We have three numerical features in our dataset.
All of our numerical features are measured in different scales.
Based on the mean & median score differences, we can expect.
Slightly left skew on the 'age' (mean: 43.23 & median: 45).
Slightly right skew on the 'bmi' (mean: 28.89 & median: 28.10).
And right skew distribution on the 'avg_glucose_level' (mean: 106.14 & median: 91.88).
 
 
Insights From Bivariate Analysis
 
Categorical Columns
 
People with hypertension are 13.25% likely to get strokes.
People without hypertension are only 3.97% likely to get strokes.
It means that people with hypertension are almost 3.3 times more likely to get strokes than the ones who don't have hypertension.
Male population is 5.11% likely to get strokes.
Female population is 4.71% likely to get strokes.
It means that people with hypertension are only 1.08 times more likely to get strokes than the ones who don't have hypertension.
People with heart disease are 17.03% likely to get strokes.
People without heart disease are only 4.18% likely to get strokes.
It means that people with heart disease are almost 4.07 times more likely to get strokes than the ones who don't have hypertension.
Married people are 6.56% likely to get strokes.
Unmarried people are only 1.65% likely to get strokes.
It means that married people are almost 3.98% times more likely to get strokes than unmarried ones.
People dwelling in rural areas are 5.2% likely to get strokes.
People dwelling in urban areas are only 1.65% likely to get strokes.
It means that people dwelling in rural areas are almost 1.15% times more likely to get strokes than the people dwelling in urban areas.
Self employed person has more probability to get strokes than other work types.
This data suggests that if you have never worked, you will not die by stroke !!! Only 0.28% of people who never worked are likely to get strokes.
People with private jobs and government jobs almost have the same probability of getting strokes.
A formerly smoked person has a probability of getting a stroke 1.66 times more than a person who has never smoked.
A person smokes has a probability to get stroke 1.11 times more than person never smoked
 
Numerical Columns
 
There is very small positive correlation between numerical features.
Let's see the correlation of numerical variables with the target variable
When age increases, the mean score on the stroke also increases.
Average glucose level's mean scores have differences between a person who has a stroke or not.
Bmi mean scores are close to each other.
Correlations with the target variable are very small.
Among all numerical features, age is the most dominant feature with a correlation of 0.24
People with an age greater than 45 years are more likely to get a heart stroke than people below age groups.
Very few people have a BMI greater than 60.
People with age greater than 45 years are more likely to get a stroke
People with avg_glucose level higher than 150 mm are more likely to get a stroke than people with lower glucose level than that.
Very few people have bmi less than 60 and there is presence of some outliers in bmi value.
If the avg_glucose_level of a person goes higher than 150 mm then, the probability of getting a stroke also increases.
 
 
Insights From Exploratory Data Analysis
Age and target variable weak positive relationship (almost .25).
Average glucose level's mean scores on the target have differences between a person who has a stroke or not. But these differences are small.
BMI does not have any significant relationship with the target variable.
A person with hypertension is almost 3.3 times more likely to get a stroke than the ones who don't have hypertension.
Male compared to female are more likely to get strokes, but the difference between female and male is very small.
A person with heart disease is 4.07 times more likely to get a stroke than the ones who don't have heart disease.
A person who is married(or married before) is 5.7 times more likely to get a stroke than the ones who don't have a marriage history.
Self employed person has more probability to get strokes than other work types.
Person who lives in a rural area slightly has a higher probability of getting a stroke than a person who lives in a rural area. Difference is small.
There is a small difference between who smokes and who does not smoke in regard to the probability of getting a stroke.
 
Insights from Target Variable 
Almost %95 of the instances of our target variable is 'No stroke'
4861 patients do not have a stroke.
%5 of the instances of our target variable is 'Stroke'.
249 patients have a stroke.
We have imbalanced data.
Our stroke dataset is an example of a so-called imbalanced dataset.
There are 19 times more people who didn’t have strokes in our data than who had, and we say that the non-stroke class dominates the stroke class.
We can clearly see that: the stroke rate in our data is 0.048 Which is a strong indicator of class imbalance
 
Imbalance Datasets
Instances across classes are imbalanced, like in our dataset, we have imbalance data.
The problem is, most of the machine learning algorithms do not work well with the imbalanced data.
Some of the metrics (like accuracy) give us misleading results.
Most of the time in classification problems our interest is to get better predictions on the minority class.
In our example: People who had a stroke are in the minority class.
Otherwise our machine learning algorithm falsely predicts the majority class.
In our example: No stroke is the majority class.
 
Feature Selection
'Age','heart_disease','avg_glucose_level','hypertension','ever_married' are selected as the features according to their scores.
 
Decide the metric
This is the first step when approaching a machine learning problem: decide the metric!
The choice of the wrong metric can mean choosing the wrong algorithm.
We see that the target is skewed and thus the best metric for this binary classification problem would be Area Under the ROC Curve (AUC).
We can use precision and recall too, but AUC combines these two metrics.
We have already seen the label/target distribution, and we know that it is a binary classification problem with skewed targets.
Just for further info, it is not advisable to use accuracy as an evaluation metric, when dealing with highly imbalanced data.
 
 
Model Performance
On our baseline model, every model gets an accuracy score of 95% since 95% of data belong to one class and all models fail to predict the lower minority class. 
We have used an oversampling technique to balance the classes of each instance of our target variable to solve class imbalance problems.
Then, we were able to get around 75% auc roc score or 22% F1 score. Recall is around 80% but precision of the model was still low. 
 
Conclusions
On our first hypothesis, we have thought bmi would be a good indicator or measure in predicting the likelihood of getting a stroke.
But, according to the data, there are many outliers in the bmi column and found as a weak feature for our target which is against the medical use case.
Accuracy metric is not a good metric to choose for imbalance datasets.
Oversampling techniques like Smote are really good tools to use incase of class imbalance problems.
More features can be added to the dataset such as the patient's exercise pattern, blood pressure and so on.
This model is best suited for  the prognosis of stroke prediction.
Since it has high recall and low precision, early signs or predictions of  getting a stroke can be useful for the patient to take care of their health problems even more seriously.
