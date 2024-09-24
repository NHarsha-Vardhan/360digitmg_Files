'''
Q1) Calculate Mean, and Standard Deviation using Python code & draw inferences on the following data. 
    Refer to the Datasets attachment for the data file.

Hint: [Insights drawn from the data such as data is normally distributed/not, outliers, measures like mean, median, 
      mode, variance, std. deviation]
'''
# a) Car’s speed and distance
import pandas  as pd
import numpy  as np
car_s_d = {'speed':[4,4,7,7,8,9,10,10,10,11,11,12,12,12,12,13,13,13,13,14,14,14,14,15,15,15,16],
        'distance':[2,10,4,22,16,10,18,26,34,17,28,14,20,24,28,26,34,34,46,26,36,60,80,20,26,54,32]}
car_s_d_df = pd.DataFrame(car_s_d)
car_s_d_df
#mean
car_s_d_mean = car_s_d_df.mean()

#standard deviation
car_s_d_std = car_s_d_df.std()

# Dropping the duplicates fetching the mean and standard deviation

car_s_d_dup = car_s_d_df.drop_duplicates(subset=['speed'])
car_s_d_dup
#Finding the mean of duplicate data
car_s_d_dup.mean()
car_s_d_dup.std()

#b) Top speed(SP) and weight(WT)

car_sp_wt = pd.read_excel(r'F:\Liser Time\360digitmg\2.EDA\Data Sets\Book1.xls')
# mean 
car_sp_wt.mean()
# standard deviation 
car_sp_wt.std()
#mode
car_sp_wt.mode()
'''Q2) Below are the scores obtained by a student on tests. 
34, 36, 36, 38, 38, 39, 39, 40, 40, 41, 41, 41, 41, 42, 42, 45, 49, 56
1)	Find the mean, median and mode, variance, and standard deviation.
2)	What can we say about the student marks? 
3)	What can you say about the Excepted value for the student score?
'''
scores = pd.DataFrame(columns=['scores'])
scores['scores'] = np.array([34, 36, 36, 38, 38, 39, 39, 40, 40, 41, 41, 41, 41, 42, 42, 45, 49, 56])
scores
#1)	Find the mean, median and mode, variance, and standard deviation.
#mean 
scores.mean()
# median
scores.median()
# mode 
scores.mode()
#variance
scores.var()
# standard deviation
scores.std()

# 2) What can we say about the student marks?
The mean is close to the median so it is the distribution is roughly symmetric


#3)	What can you say about the Excepted value for the student score?

The expected value for the student score is dependent on the mean 

'''
Q3) Three Coins are tossed, find the probability that two heads and one tail are obtained.
'''
When tossing three coins, the possible outcomes can be represented as a set of eight outcomes

But we need the probability of of 2 heads and 1 tail so final probalibility is 3/8

'''
Q4) Two Dice are rolled, find the probability that the sum is
a)	Equal to 1
b)	Less than or equal to 4
c)	Sum is divisible by 2 and 3

'''

#a)	Equal to 1

There is only one combination where the sum is 1, which is (1, 1).

Probability P(Equal to 1) = 1/36

# b)	Less than or equal to 4
The combinations for sums less than or equal to 4 are (1, 1), (1, 2), (2, 1), (1, 3), (2, 2), and (3, 1).

Probability P(Sum<=4) =  7/ 36 

# c)	Sum is divisible by 2 and 3
The sums divisible by 2 and 3 are 2, 4, 6, 8, 10, and 12. The corresponding combinations are 
(1, 1), (1, 2), (2, 1), (1, 5), (2, 4), (3, 3), (4, 2), and (5, 1),(6,6)

Probability P(Sum Divisible by 2and 3) = 9/36 = 1/4


'''
Q5) A bag contains 2 red, 3 green, and 2 blue balls. Two balls are drawn at random.
 What is the probability that none of the balls drawn is blue?
'''

The number of ways to draw 2 balls without getting any blue balls is given by the combination of the non-blue balls:

Ways to draw 2 non-blue balls
is 5C2 = 10
import math

# Total number of balls
total_balls = 2 + 3 + 2

# Total ways to draw 2 balls
total_ways = math.comb(total_balls, 2)
    
# Ways to draw 2 non-blue balls
non_blue_ways = math.comb(2 + 3, 2)

# Probability
probability_none_blue = non_blue_ways / total_ways

'''
Q6) Calculate the Expected number of candies for a randomly selected child:
Below are the probabilities of the count of candies for children 
(ignoring the nature of the child-Generalized view)
i. Child A – the probability of having 1 candy is 0.015.
ii. Child B – the probability of having 4 candies is 0.2.

CHILD	Candies count	Probability
A	1	0.015
B	4	0.20
C	3	0.65
D	5	0.005
E	6	0.01
F	2	0.12

'''
A, B, C, D, E, F = 'A', 'B', 'C', 'D', 'E', 'F'
exp_candies = pd.DataFrame(columns=['CHILD','Candies count','Probability'])
exp_candies['CHILD'] ,exp_candies['Candies count'], exp_candies['Probability']= [A,B,C,D,E,F],[1,4,3,5,6,2],[0.015,0.20,0.65,0.005,0.01,0.12]
 
exp_candies.mean()

child_values = [1, 4, 3, 5, 6, 2]
probabilities = [0.015, 0.20, 0.65, 0.005, 0.01, 0.12]

# Calculate the expected value
expected_value = sum(value * prob for value, prob in zip(child_values, probabilities))

'''
Q7) Calculate Mean, Median, Mode, Variance, Standard Deviation, and Range & comment about the values / draw inferences, for the given dataset.
-	For Points, Score, Weigh>
Find Mean, Median, Mode, Variance, Standard Deviation, and Range and comment on the values/ Draw some inferences. 

'''
points = [3.9,3.9,3.85,3.08,3.15,2.76,3.21,3.69,3.92,3.92,3.92,3.07,3.07,3.07,2.93,3,3.23,4.08,4.93,4.22,3.7,2.76,3.15,3.73,3.08]
score = [2.62,2.875,2.32,3.215,3.44,3.46,3.57,3.19,3.15,3.44,3.44,4.07,3.73,3.78,5.25,5.242,5.345,2.2,1.615,1.835,2.465,3.52,3.435,3.84,3.845]
weigh = [16.46,17.02,18.61,19.44,17.02,20.22,15.84,20,22.9,18.3,18.9,17.4,17.6,18,17.98,17.82,17.42,19.47,18.52,19.9,20.01,16.87,17.3,15.41,17.05]

p_s_w = {'points':points,'score':score,'weigh':weigh}
psw = pd.DataFrame(p_s_w)
psw.mean()
psw.median()
psw.mode()
psw.var()
psw.std()

range_p = max(psw.points) - min(psw.points)
range_s = max(psw.score) - min(psw.score)
range_w = max(psw.weigh) - min(psw.weigh)

psw.points.skew()
psw.score.skew()
psw.weigh.skew()

'''
Q8) Calculate the Expected Value for the problem below.
a)	The weights (X) of patients at a clinic (in pounds), are.
108, 110, 123, 134, 135, 145, 167, 187, 199
Assume one of the patients is chosen at random. What is the Expected Value of the Weight of that patient?

'''

weights = [108, 110, 123, 134, 135, 145, 167, 187, 199]

# Calculate the expected value
expected_value = sum(weight / len(weights) for weight in weights)

# Display the result
print("Expected value of the weight of a randomly selected patient:", expected_value)

'''
Q9) Look at the data given below. Plot the data, find the outliers, and find out:  μ,σ,σ^2
Hint: [Use a plot that shows the data distribution, and skewness along with the outliers; also use Python code to evaluate measures of centrality and spread]

Name of company	Measure X
Allied Signal	24.23%
Bankers Trust	25.53%
General Mills	25.41%
ITT Industries	24.14%
J.P.Morgan & Co.	29.62%
Lehman Brothers	28.25%
Marriott	25.81%
MCI	24.39%
Merrill Lynch	40.26%
Microsoft	32.95%
Morgan Stanley	91.36%
Sun Microsystems	25.99%
Travelers	39.42%
US Airways	26.71%
Warner-Lambert	35.00%

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Data
data = {
    'Name of Company': ['Allied Signal', 'Bankers Trust', 'General Mills', 'ITT Industries', 'J.P. Morgan & Co.',
                        'Lehman Brothers', 'Marriott', 'MCI', 'Merrill Lynch', 'Microsoft', 'Morgan Stanley',
                        'Sun Microsystems', 'Travelers', 'US Airways', 'Warner-Lambert'],
    'Measure X': [24.23, 25.53, 25.41, 24.14, 29.62, 28.25, 25.81, 24.39, 40.26, 32.95, 91.36, 25.99, 39.42, 26.71, 35.00]
}

df = pd.DataFrame(data)

# Plot the distribution
plt.figure(figsize=(12, 6))
sns.boxplot(x='Measure X', data=df)
plt.title('Distribution of Measure X with Outliers')
plt.show()

# Identify and print outliers
Q1 = df['Measure X'].quantile(0.25)
Q3 = df['Measure X'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Measure X'] < (Q1 - 1.5 * IQR)) | (df['Measure X'] > (Q3 + 1.5 * IQR))]
print("Outliers:")
print(outliers)

# Calculate mean, standard deviation, and variance
mean_value = np.mean(df['Measure X'])
std_deviation = np.std(df['Measure X'])
variance = np.var(df['Measure X'])
df['Measure X'].var()

print("\nMeasures of Centrality and Spread:")
print("Mean (μ):", mean_value)
print("Standard Deviation (σ):", std_deviation)
print("Variance (σ^2):", variance)


'''
Q10)
AT&T was running commercials in 1990 aimed at luring back customers who had switched to one of the other long-distance 
phone service providers. One such commercial shows a businessman trying to reach Phoenix and mistakenly getting Fiji,
where a half-naked native on a beach responds incomprehensibly in Polynesian. When asked about this advertisement, AT&T 
admitted that the portrayed incident did not actually take place but added that this was an enactment of something that 
“could happen.” Suppose that one in 200 long-distance telephone calls is misdirected. 
'''

import numpy as np

# Probability of a misdirected call
probability_misdirected = 1 / 200

# Number of simulations
num_simulations = 10000

# Simulate misdirected calls
misdirected_calls = np.random.choice([0, 1], size=num_simulations, p=[1 - probability_misdirected, probability_misdirected])

# Calculate the simulated probability of a misdirected call
simulated_probability = np.mean(misdirected_calls)

print(f"Simulated Probability of a Misdirected Call: {simulated_probability:.4f}")

'''
Q11) Returns on a certain business venture, to the nearest $1,000, are known to follow the following probability distribution.
X	P(x)
-2,000	0.1
-1,000	0.1
0	0.2
1000	0.2
2000	0.3
3000	0.1

(i)What is the most likely monetary outcome of the business venture?
Hint: [The outcome is most likely the expected returns of the venture]

(ii)Is the venture likely to be successful? Explain.
Hint: [Probability of % of the venture being a successful one]

(iii)What is the long-term average earning of business ventures of this kind? Explain.
Hint: [Here, the expected return to the venture is considered as the
required average]

(iv)What is a good measure of the risk involved in a venture of this kind? Compute this measure. 
Hint: [Risk here stems from the possible variability in the expected returns, therefore, name the risk measure for this venture]

'''
import numpy as np

# Given data
outcomes = [-2000, -1000, 0, 1000, 2000, 3000]
probabilities = [0.1, 0.1, 0.2, 0.2, 0.3, 0.1]
df_out_pro = pd.DataFrame(columns=['outcomes','probabilities'])
df_out_pro['outcomes'] = outcomes
df_out_pro['probabilities'] = probabilities+
df_out_pro.var()
df_out_pro.std()
# (i) Expected return (most likely monetary outcome)
expected_return = np.sum(np.array(outcomes) * np.array(probabilities))
expected_return.mean()
print(f"(i) Most Likely Monetary Outcome (Expected Return): ${expected_return:,.0f}")

# (ii) Likelihood of success
success_probability = np.sum(np.array(probabilities)[np.array(outcomes) > 0])
print(f"(ii) Likelihood of Success: {success_probability:.2%}")

# (iii) Long-term average earnings
long_term_average_earnings = expected_return
print(f"(iii) Long-Term Average Earnings: ${long_term_average_earnings:,.0f}")

# (iv) Measure of risk (standard deviation)
variance = np.sum((np.array(outcomes) - expected_return)**2 * np.array(probabilities))
standard_deviation = np.sqrt(variance)
print(f"(iv) Measure of Risk (Standard Deviation): ${standard_deviation:,.0f}")

