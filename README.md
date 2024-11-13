# College Ranking Project

## Overview

This project aims to provide a data-driven college ranking system for prospective students based on metrics like overall student satisfaction, admissions rate, tuition cost, political tolerance, and campus support for free speech. The goal is to help students identify schools that align with both their preferences and values.

The project includes the following components:

- **A web scraper utilizing API endpoints to collect data on colleges.**
- **A data cleaning script.**
- **A ranking algorithm that generates scores for colleges based on user-defined weightings of different factors**
- **Tableau visualizations to provide insights into specific metrics of the dataset.**

The goal is to help students identify institutions that align with their preferences and values.
Data source: https://rankings.thefire.org/rank

## Files in This Repository

1. **`college_scraper.py`**: This script scrapes data from the API endpoints of online college ranking sources. The data is gathered in JSON format.
2. **`data_cleaning.py`**: This script processes the raw data collected from the API.
3. **`ranking_algorithm.py`**: Contains the ranking algorithm logic.
4. **`college_data_raw.csv`**: Raw dataset before cleaning.
5. **`college_data_ranked.csv`**: Final ranked dataset.

## Visualizations in Tableau

- **Political Tolerance Scores**: This visualization shows the tolerance scores for conservatives and liberals at every college. https://public.tableau.com/views/TotalScorebreakdownforTop10Colleges/CollegesWithTheMostInstancesofCampusFreeSpeechSupport?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link 
- **Top 11 Colleges for Campus Support of Free Speech**: Highlights the colleges with the most instances of public support for free speech.
https://public.tableau.com/views/PoliticalToleranceScores/Sheet1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link
- **Ranked Colleges Based on User Defined Metrics**:
https://public.tableau.com/views/RankedCollegesBasedonUserDefinedMetrics/Sheet1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link 

