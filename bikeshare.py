import time
import pandas as pd
import numpy as np

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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in ('chicago', 'new york City', 'washington'):
        city = input("Please choose the city you want to analyse (Chicago, New York City or Washington): ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    while month not in ('all','january','february','march','may','june'):
        month = input("Please choose the month you want to analyse (all, january, february, ... , june): ").lower()

    day = ''
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
        day = input("Please choose the day of week you want to analyse (or choose 'all'): ").lower()
                


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
  
    # load data file into a dataframe
    df = pd.DataFrame(pd.read_csv(CITY_DATA[city.lower()]))

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.lower().title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("The most common month: " + str(popular_month))

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week: " + str(popular_day_of_week))

    # TO DO: display the most common start hour
    popular_start_hour = df['Start Time'].dt.hour.mode()[0]
    print("The most common start hour: " + str(popular_start_hour))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most common start station: " + popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most common end station: " + popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_stations = (df['Start Station'] + ' ' + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station: " + popular_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time: ' + str(total_travel_time))
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time: ' + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of different user types:")
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        genders = df['Gender'].value_counts()
        print("Gender Usage:")
        print(genders)
    else: 
        print("No gender information available")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        min_year = df['Birth Year'].min()
        print('Earliest year of birth: ' + str(min_year))
        max_year = df['Birth Year'].max()
        print('Most Recent year of birth: ' + str(max_year))
        most_year = df['Birth Year'].mode()[0]
        print('Most Common year of birth: ' + str(most_year))
    else:
        print("No birth information available")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Display raw data"""
    print(df.iloc[:5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        display = input('\nWould you like to see raw data? Enter yes or no.\n').lower()
                
        while(display.lower() != 'no'):
            if display == 'yes':
                display_data(df)
                display = input('\nWould you like to see more 5 lines of raw data? Enter yes or no.\n').lower()
            else:
                break
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
