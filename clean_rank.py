import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
#Read data
college_raw = pd.read_csv('college_data.csv')
#Change column names
column_names = college_raw.columns
college_raw.rename(columns={
    'metadata.overallScore': 'Overall Score',
    'metadata.responseCount': 'Response Count',
    'metadata.usNewsRanking': 'US News Ranking',
    'metadata.totalUndergradEnrollment': 'Total Undergrad Enrollment',
    'metadata.publicOrPrivate': 'Public or Private',
    'metadata.undergradType': 'Undergrad Type',
    'metadata.admissionsRate': 'Admissions Rate',
    'metadata.outOfStateTuition': 'Out of State Tuition',
    'metadata.usNewsRankingURL': 'US News Ranking URL',
    'metadata.campusPhotoURL': 'Campus Photo URL',
    'metadata.collegeLogoURL': 'College Logo URL',
    'slug': 'Slug',
    'unitid': 'Unit ID',
    'institutionName': 'Institution Name',
    'viewpointRatio': 'Viewpoint Ratio',
    'viewpoint': 'Viewpoint',
    'speechCode': 'Speech Code',
    'scores.speechCode': 'Scores Speech Code',
    'scores.viewpoint': 'Scores Viewpoint',
    'scores.speechClimate': 'Speech Climate',
    'scores.overall': 'Overall Score',
    'scores.comfort': 'Comfort',
    'scores.selfCensorship': 'Self Censorship',
    'scores.toleranceForLiberals': 'Tolerance for Liberals',
    'scores.toleranceForConservatives': 'Tolerance for Conservatives',
    'scores.meanTolerance': 'Mean Tolerance',
    'scores.toleranceDifference': 'Tolerance Difference',
    'scores.disruptiveConduct': 'Disruptive Conduct',
    'scores.adminSupport': 'Admin Support',
    'scores.openness': 'Openness',
    'scores.deplatformings': 'Deplatformings',
    'scores.attemptedDisruptions': 'Attempted Disruptions',
    'scores.sanctionedScholars': 'Sanctioned Scholars',
    'scores.sanctionedStudents': 'Sanctioned Students',
    'scores.honorRollStatements': 'Honor Roll Statements'
}, inplace=True)

##Cleaning
college_raw.drop(['Slug', 'Campus Photo URL', 'College Logo URL', '_id', 'US News Ranking URL', 'Unit ID', 'Scores Speech Code', 'Scores Viewpoint'], axis=1, inplace=True)

#Delete missing rows
print(college_raw.isnull().sum())
college_raw.dropna(inplace = True)

#Delete duplicate columns
college_raw = college_raw.loc[:, ~college_raw.columns.duplicated()]

#Change negative overall score values to 0
college_raw['Overall Score'] = college_raw['Overall Score'].apply(lambda x: 0 if x < 0 else x)
college_raw.to_csv('cleaned_colleges.csv', index = False)
