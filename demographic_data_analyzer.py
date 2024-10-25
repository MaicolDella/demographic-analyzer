import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.value_counts('race')

    # What is the average age of men?
    average_age_men = int(df[df['sex'] == 'Male']['age'].mean()*10)/10

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((len(df[df['education'] == 'Bachelors'])/len(df))*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_count = len(higher_education)
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_count = len(lower_education)

    # percentage with salary >50K
    higher_education_rich_count = len(higher_education[higher_education['salary'] == '>50K'])
    lower_education_rich_count = len(lower_education[lower_education['salary'] == '>50K'])

    higher_education_rich = round(higher_education_rich_count/higher_education_count*100, 1)
    lower_education_rich = round(lower_education_rich_count/lower_education_count*100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df['hours-per-week'] == 1]
    num_min_workers = len(min_workers)
    rich_min_workers = min_workers[min_workers['salary'] == '>50K']
    num_rich_min_workers = len(rich_min_workers)
    rich_percentage = round(num_rich_min_workers/num_min_workers*100, 1)

    # What country has the highest percentage of people that earn >50K?
    df_high_earners = df[df['salary'] == '>50K']    
    total_per_country = df['native-country'].value_counts()

    high_earners_per_country = df_high_earners['native-country'].value_counts()
    percentage_high_earners = (high_earners_per_country / total_per_country) * 100

    highest_earning_country = percentage_high_earners.idxmax()
    highest_earning_country_percentage = round(percentage_high_earners.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    high_earners_india = df.loc[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    top_IN_occupation = high_earners_india['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
