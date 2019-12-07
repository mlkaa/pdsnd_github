import time
import pandas as pd
import numpy as np
import datetime as dt


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
    city = str.lower(input("What is the required city you want to be analyzed? ( chicago , new york city , washington ) : "))
    while city not in CITY_DATA:
        print("invalid input")
        city = str.lower(input("What is the required city you want to be analyzed? ( chicago , new york city , washington ) : "))

    # TO DO: get user input for month (all, january, february, ... , june)
    month = int(input("What is the required month you want to be analyzed? ( number of the month from 1 to 6 ) which 1 is January and 6 is June : "))
    while month not in range(1,7):
        print("invalid input")
        month = int(input("What is the required month you want to be analyzed? ( number of the month from 1 to 6 ) which 1 is January and 6 is June : "))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = int(input("What is the required day you want to be analyzed? ( number of the day from 1 to 7 ) which 1 is Saterday and 7 is Friday : " ))
    while day not in range(1,8):
        print("invalid input")
        day = int(input("What is the required day you want to be analyzed? ( number of the day from 1 to 7 ) which 1 is Saterday and 7 is Friday : " ))


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] =(df['Start Time']).dt.month
    df['Day'] = (df['Start Time']).dt.day
    
    if month in range(1,7):
        df = df[df['Month'] == month]
    if day in range (1,8):
        df = df[df['Day'] == day]      

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""        
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    Most_Common_Month = df['Month'].mode()[0]
    print('The most common month is: ', Most_Common_Month)

    # TO DO: display the most common day of week
    Most_Common_Day = df['Day'].mode()[0]
    print('The most common day of week is: ', Most_Common_Day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    Most_Common_Hour = df['hour'].mode()[0]
    print('The most common start hour is: ', Most_Common_Hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Most_Started_Station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: ', Most_Started_Station)

    # TO DO: display most commonly used end station
    Most_End_Station = df['End Station'].mode()[0]
    print('The most commonly used end station is: ', Most_End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    Most_Frequent_Combination = df['Start Station'] +'to'+ df['End Station']
    print('The most frequent combination of start station and end station trip is: ', Most_Frequent_Combination.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = df['Trip Duration'].sum()
    print('The total travel time is: ', Total_Travel_Time)

    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('The mean travel time is: ', Mean_Travel_Time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    User_Types = df['User Type'].value_counts()
    print('The counts of user types is: \n', User_Types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print("What is your gender?")
        genderInput = str.lower(input("Enter 'M' for Male or 'F' for Female\n"))
    
        if genderInput == 'm':
            gender = df.loc[df.Gender == 'Male', 'Gender'].count()
            print('The counts of gender (Male) is: ', gender)
        
        elif genderInput == "f":
            gender = df.loc[df.Gender == 'Female', 'Gender'].count()
            print('The counts of gender (Female) is: ', gender)
          
        
    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        print("\nEarliest year of birth: ", df["Birth Year"].min())
        print("Most recent year of birth: ", df["Birth Year"].max())
        print("Most common year of birth: ", df["Birth Year"].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    raw_data = str(input("\nDo you want to see raw data? Enter yes or no.\n"))
    
    
    counter = 0
    line = 0
    if raw_data.lower() == 'yes':
        while line < len(df) :
            if counter < 5 :
                result = df.iloc[[line]]
                print (result)
                line += 1
                counter += 1 
            
            else:
                counter = 0
                raw_data = str(input("\nDo you want to see raw data? Enter yes or no.\n")) 
                if raw_data.lower() != 'yes':
                    break

            
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)       
                
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break 

if __name__ == "__main__":
	main()
