import requests
import json
import csv

FIELDS = [
    '_id',
    'metadata.overallScore',
    'metadata.responseCount',
    'metadata.usNewsRanking',
    'metadata.totalUndergradEnrollment',
    'metadata.publicOrPrivate',
    'metadata.undergradType',
    'metadata.admissionsRate',
    'metadata.outOfStateTuition',
    'metadata.usNewsRankingURL',
    'metadata.campusPhotoURL',
    'metadata.collegeLogoURL',
    'slug',
    'unitid',
    'institutionName',
    'viewpointRatio',
    'viewpoint',
    'speechCode',
    'scores.speechCode',
    'scores.viewpoint',
    'scores.speechClimate',
    'scores.overall',
    'scores.comfort',
    'scores.selfCensorship',
    'scores.toleranceForLiberals',
    'scores.toleranceForConservatives',
    'scores.meanTolerance',
    'scores.toleranceDifference',
    'scores.disruptiveConduct',
    'scores.adminSupport',
    'scores.openness',
    'scores.deplatformings',
    'scores.attemptedDisruptions',
    'scores.sanctionedScholars',
    'scores.sanctionedStudents',
    'scores.honorRollStatements'
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

def traverse(root, path):
    """
    Traverse nested dictionaries.
    """
    value = root
    for segment in path.split('.'):
        if isinstance(value, list):
            value = value[int(segment)] if len(value) > int(segment) else None
        else:
            value = value.get(segment, None) if value else None
    return value

def fetch_results_page(json_data, writer):
    """
    Fetch JSON data and write to CSV.
    """
    for school in json_data:
        row = []
        for field in FIELDS:
            row.append(traverse(school, field))
        writer.writerow(row)

def main():
    url = "https://speechapi.collegepulse.com/api/public/speech/schools/overall?filters=[]&search=&pageSize=260&page=0&sortBy=rank&sortOrder=asc&year=2024"
    response = requests.get(url, headers=HEADERS)
    json_data = json.loads(response.text)

    #Write to a CSV file
    with open('college_data.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(FIELDS)
        fetch_results_page(json_data, writer)

if __name__ == "__main__":
    main()
