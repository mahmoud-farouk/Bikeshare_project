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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    city=input("kindly select the one of these citie chicago\n or \n new york city\n or washington\n :").lower()
    while city not in CITY_DATA.keys():
        print("invalid input") 
        city=input("kindly select the one of these citie chicago\n or \n new york city\n or washington\n :").lower()
    
    
    # get usnc
    # er input for month (all, januaryy, february, ... , june)
    months=["January","February","March","April","May" ,"Jun", "All"]
    month=input("selct one of these months to help you more in analysis the data required,,,\n January,\n February\n March \n April \n May \n Jun \n All...:").capitalize()    
    for value in month:
        if month in months:
            break
        else:
            print("invalid input")
        month=input("selct one of these months to help you more in analysis the data required,,,\n January,\n February\n March \n April \n May \n Jun \n All...:").capitalize() 
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days=["Saturday","Sunday","Monday","Tuesday","Wensday","Thursday","All"]
    day=input("select day to display ,,, Saturday\n Sunday\n Monday\n Tuesday\n Wensday\n Thursday\n All ? :").capitalize()
    while day not in days:
        print("invalid input")
        day=input("select day to display ,,, Saturday\n Sunday\n Monday\n Tuesday\n Wensday\n Thursday\n or All ? :").capitalize()

    print('-'*40)
    return city,month,day


def load_data(city,month,day):
    
    #Loads data for the specified city and filters by month and day if applicable.
    
    df=pd.read_csv(CITY_DATA[city])
   
        #(str) city - name of the city to analyze
    df["Start Time"]=pd.to_datetime(df['Start Time'])
      #  (str) month - name of the month to filter by, or "all" to apply no month filter
    df['month']=df["Start Time"].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months=["January",'Febraury','March','April','May','Jun','All']
        month=months.index(month) + 1

    df=df[df["month"]==month]
       # (str) day - name of the day of week to filter by, or "all" to apply no day filter
    if day!= "all":
           #days=['Saturday','sunday','monday','Tuesday','wensday','Thusday','All']
        df = df[df['day_of_week']==day.title()]
    
    #Returns:
       # df - Pandas DataFrame containing city data filtered by month and day
       


    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_month=df['month'].mode()
    print("the most cmmon month is : ",most_month)
    
    # display the most common day of week
    most_day=df['day_of_week'].mode()
    print("the most common day of the week is :",most_day)

    # display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station=df['Start Station'].mode()[0]
    print("most commonly used Start Station is :",start_station)

    # display most commonly used end station
    end_station=df['End Station'].mode()[0]
    print("most commonly used End Station is :",end_station)


    # display most frequent combination of start station and end station trip
    df["rout"] = df["Start Station"] + "-" + df["End Station"] 
    Rout=df['rout'].mode()[0]
    print("most frequent rout is :",Rout)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Total_travel=df['Trip Duration']
    print("our total travel will beas ", Total_travel.sum())

    # display mean travel time
    print("our mean travel as :",Total_travel.mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    User_types=df['User Type'].value_counts()
    print("all counts of user types will be :", User_types)

    # Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print("count of gender is", gender_count)

    except:

        print('This data is not available for Washington')



    # Display earliest, most recent, and most common year of birth
    try:
       earliest=int(df['Birth Year'].min())
       most_recent=int(df['Birth Year'].max())
       common_year=int(df['Birth Year'].mode()[0])
       print('the most earliest year of birth will be :',earliest)
       print("the most recent year of birth will be :",most_recent)
       print("the most common year of birth will be ",common_year)
    except:
        print('this data not available for washington')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city,month,day = get_filters()
        print(city,month,day)
        df = load_data(city, month, day)
        print(df.head)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
