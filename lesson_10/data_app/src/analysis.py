def filter_age_data(data):
    """
    Filters the dataset to include only rows related to age distribution.

    :param data: A pandas DataFrame containing the population data.
    :return: A pandas DataFrame with rows filtered to include only age distribution data.
    """
    age_data = data[data['MEASURE'].str.contains('Population')]
    return age_data


def process_age_data(age_data):
    """
    Processes the age data to summarize the population count for each age group.

    :param age_data: A pandas DataFrame containing the age distribution data.
    :return: A pandas Series with the total population count for each age group.
    """
    age_summary = age_data.groupby('AGE_GROUP')['OBS_VALUE'].sum().reset_index()
    age_summary.columns = ['Age Group', 'Population Count']  # Customizing column names
    return age_summary

def process_age_data_over_time(data):
    """
    Process age distribution data over time.

    This function groups the given data by year and age group, 
    calculates the sum of the observation values for each group, 
    and returns a DataFrame with the results.

    Parameters:
    data (DataFrame): The pandas DataFrame containing the population data 
                      with columns 'YEAR', 'AGE_GROUP', and 'OBS_VALUE'.

    Returns:
    DataFrame: A pandas DataFrame with columns 'YEAR', 'AGE_GROUP', 
               and the sum of 'OBS_VALUE' for each group.
    """
    age_summary_over_time = data.groupby(['YEAR', 'AGE_GROUP'])['OBS_VALUE'].sum().reset_index()
    age_summary_over_time.columns = ['Year', 'Age Group', 'Population Count']  # Customizing column names
    return age_summary_over_time

def filter_data_by_year(data, year):
    """
    Filters the data for the given year.
    
    Parameters:
        data (DataFrame): The dataset containing population information.
        year (int): The year for which to filter the data.
    
    Returns:
        DataFrame: The filtered data for the specified year.
    """
    filtered_data = data[data['YEAR'] == year]
    renamed_data = filtered_data.rename(columns={
        'YEAR': 'Year',
        'MEASURE': 'Category',
        'AGE_GROUP': 'Age Group',
        'OBS_VALUE': 'Population'
    })
    return renamed_data
