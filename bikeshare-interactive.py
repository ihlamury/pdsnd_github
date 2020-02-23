# First interactive project
import time
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 13)

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! This is Yağız! Let\'s explore some US bikeshare data!\n')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('\nWhich city would you like to conduct the analysis for? \n\n Options:  |Chicago| |New York City| |Washington|\n').lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print('\nPlease provide a valid answer from the options.\n')
            continue
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input('\nFor which month would you like to conduct the analysis? \n\n Options: |January| |February| |March| |April| |May| |June| or |All|\n').lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print('\nPlease provide a valid answer from the options.\n')
            continue
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input('\nFor which weekday would you like to conduct the analysis? \n\n Options: |Monday| |Tuesday| |Wednesday| |Thursday| |Friday| |Saturday| |Sunday| or |All|\n').lower()
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            print('\nPlease provide a valid answer from the options.\n')
            continue
        else:
            break


    print('-'*40)
    return city , month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or 'all' to apply no day filter
        (stry) day - name of the day of week to filter by, or 'all' to apply no day filter

    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day of week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #filter by month to create the new dataframe
        df = df[df['month'] == month]


    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day of week'] == day.title()]


    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month = df['month'].mode()[0]
   # print('The most common month: ', common_month)
    if common_month == 1:
        print('The most common month: January')
    elif common_month == 2:
        print('The most common month: February')
    elif common_month == 3:
        print('The most common month: March')
    elif common_month == 4:
        print('The most common month: April')
    elif common_month == 5:
        print('The most common month: May')
    else:
        print('The most common month: June')


    # TO DO: display the most common day of week

    common_day = df['day of week'].mode()[0]
    print('The most common day: ', common_day)

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]

    print('The most common hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start statation: ', common_start)


    # TO DO: display most commonly used end station
    common_end = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station: ', common_end)


    # TO DO: display most frequent combination of start station and end station trip
    df['Combine Start&End'] = df['Start Station'] + df['End Station']
    frequent_combination = df['Combine Start&End'].value_counts().idxmax()
    print('The most frequent combination of start and end station trip: ', frequent_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = np.sum(df['Trip Duration'])/86400
    print('Total travel time in days: ', total_travel)

    # TO DO: display mean travel time
    mean_travel = np.mean(df['Trip Duration'])/60
    print('The mean of travel time in minutes: ', mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_usertype = df['User Type'].value_counts()
    print('User tpye count:\n', count_usertype.to_string())

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('\nGender of users:\n', gender_count.to_string())
    except:
        print('\nNo available gender information.')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = min(df['Birth Year'])
        recent_birth = max(df['Birth Year'])
        common_birth = df['Birth Year'].mode()[0]
        print('\nEarliest birth year: ', earliest_birth)
        print('\nMost recent birth year: ', recent_birth)
        print('\nMost common year of birth: ', common_birth)
    except:
        print('\nNo available birth year information.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw(df):
    """Raw data is displayed upon request by the user."""

 # Hint: df.iloc[index1:index2]

    display_start = 0

    show_raw = input('\nWould you like to see the raw data?\n \nOptions:  |Yes| or |No|\n').lower()
    while show_raw == 'yes':
        print(df.iloc[display_start:display_start + 5])
        display_start += 5
        show_raw = input('\nWould you like to see more?\n \nOptions:  |Yes| or |No|\n').lower()


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
