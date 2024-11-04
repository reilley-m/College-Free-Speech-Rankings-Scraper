##Ranking algorithm

#User Defined Weights Example
weights = {
    'Overall Score': 0.3,  #(30%)
    'Admissions Rate': 0.1,  #(10%)
    'Out of State Tuition': 0.2,  #(20%)
    'Openness': 0.1,  #(10%)
    'Tolerance for Liberals': 0.1,  #(10%)
    'Tolerance for Conservatives': 0.1,  #(10%)
    'Comfort': 0.1  #(10%)
}

#Normalize numeric columns used in ranking (0-1)
scaler = MinMaxScaler()
numeric_columns = ['Overall Score', 'Admissions Rate', 'Out of State Tuition', 'Openness', 
                   'Tolerance for Liberals', 'Tolerance for Conservatives', 'Comfort']
college_raw[numeric_columns] = scaler.fit_transform(college_raw[numeric_columns])

#Calculate score for each college based on UD weights
college_raw['Total Score'] = (
    college_raw['Overall Score'] * weights['Overall Score'] +
    college_raw['Admissions Rate'] * weights['Admissions Rate'] +
    (1 - college_raw['Out of State Tuition']) * weights['Out of State Tuition'] +  #(lower tuition = better score)
    college_raw['Openness'] * weights['Openness'] +
    college_raw['Tolerance for Liberals'] * weights['Tolerance for Liberals'] +
    college_raw['Tolerance for Conservatives'] * weights['Tolerance for Conservatives'] +
    college_raw['Comfort'] * weights['Comfort']
)

#Sort colleges by total score in desc order
ranked_colleges = college_raw.sort_values(by='Total Score', ascending=False)
ranked_colleges['Rank'] = range(1, len(ranked_colleges) + 1) #add ranking column

#Save to CSV file
ranked_colleges.to_csv('ranked_colleges.csv', index=False)

#Display top 10 ranked colleges
print(ranked_colleges.head(10))
