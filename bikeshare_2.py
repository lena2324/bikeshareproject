import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york.csv',
             'washington': 'washington.csv'}

def get_filters():
     return city, month, day

    #Asks user to specify a city, month, and day to analyze.
    #Returns:
       # #(str) city - name of the city to analyze
        #(str) month - name of the month to filter by, or "all" to apply no month filter
        #(str) day - name of the day of week to filter by, or "all" to apply no day filter


print("Hello! Let's explore some US Bikeshare data!")
# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

city_name: list[str] = ['chicago', 'washington', 'new york', 'all']

month_name: list[str] = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
day_name: list[str] = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

while True:
    city = input('What city would you like to explore? ')
    city = city.lower()  #to make sure that any kind of the input will be taken
    if city in city_name:
        break
    else:
        print("invalid input. Please enter a valid input")

# get user input for month (all, january, february, ... , june)
while True:
    month = input("What month would you like to check? Please choose in this range Jan - June  ")
    month = month.lower()  #to make sure that any kind of the input will be taken
    if month in month_name:
        break
    else:
        print("invalid input. Please enter a valid input")

# get user input for day of week (all, monday, tuesday, ... sunday)
while True:
    day = input("What day would you like to check? ")
    day = day.lower()   #to make sure that any kind of the input will be taken
    if day in day_name:
        break
else:
     print("invalid input. Please enter a valid input")

print('-' * 40)


def load_data(city, month, day):
    return df   #I had to move df here because otherwise it was giving me an error that it's outside of the range
   #
    #Loads data for the specified city and filters by month and day if applicable.
#
    #Args:
       # (str) city - name of the city to analyze
        #(str) month - name of the month to filter by, or "all" to apply no month filter
       # (str) day - name of the day of week to filter by, or "all" to apply no day filter
   # Returns:
        #df - Pandas DataFrame containing city data filtered by month and day
    #

    # load data file into a dataframe
print("Loading data...")

df = pd.read_csv("{}.csv".format(city.replace(" ","_"))) #the given code wasn't working for me so I found this solution


# convert the Start Time column to datetime

df['Start Time'] = pd.to_datetime(df['Start Time'])
df['End Time'] = pd.to_datetime(df['End Time'])

# extract month and day of week and hour from Start Time to create new columns

df['month'] = df['Start Time'].apply(lambda x: x.month)
df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())

# filter by month if applicable
if month != 'all':
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = months.index(month) + 1

df = df.loc[df['month'] == month, :]


# filter by day of week if applicable
if day != 'all':
# filter by day of week to create the new dataframe
 df = df.loc[df['day_of_week'] == day, :]


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

print("Calculating The Most Frequent Times of Travel...")
start_time = time.time()

# display the most common month

print("The most common month is: {}".format(
        str(df['month'].mode().values[0])))
# display the most common day of week

print("The most common day of the week: {}".format(
        str(df['day_of_week'].mode().values[0])))
# display the most common start hour

df['start_hour'] = df['Start Time'].dt.hour
print("The most common start hour: {}".format(
        str(df['start_hour'].mode().values[0])))

print("This took %s seconds." % (time.time() - start_time))
print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

print("Calculating The Most Popular Stations and Trip...")
start_time = time.time()

# display most commonly used start station

most_common_start_station = df['Start Station'].value_counts().idxmax()
print("The most commonly used start station :", most_common_start_station)

# display most commonly used end station

most_common_end_station = df['End Station'].value_counts().idxmax()
print("The most commonly used end station :", most_common_end_station)

# display most frequent combination of start station and end station trip

most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
print("The most commonly used start station and end station : {}, {}" \
          .format(most_common_start_end_station[0], most_common_start_end_station[1]))

print("This took %s seconds." % (time.time() - start_time))
print('-' * 40)


def trip_duration_stats(df):
   """Displays statistics on the total and average trip duration."""

print("Calculating Trip Duration...")
start_time = time.time()

# display total travel time

total_travel = df['Trip Duration'].sum()
print("Total travel time :", total_travel)

# display mean travel time

mean_travel = df['Trip Duration'].mean()
print("Mean travel time :", mean_travel)

print("This took %s seconds." % (time.time() - start_time))
print('-' * 40)


def user_stats(df):
    """Displays statistics on Bikeshare users."""

print("Calculating User Statistics...")
start_time = time.time()

# Display counts of user types

print("Here are the counts of various user types:")
print(df['User Type'].value_counts())

# Display earliest, most recent, and most common year of birth
print("The earliest birth year is: {}".format(
    str(int(df['Birth Year'].min()))))
print("The latest birth year is: {}".format(
    str(int(df['Birth Year'].max()))))
print("The most common birth year is: {}".format(
    str(int(df['Birth Year'].mode().values[0]))))

print("This took %s seconds." % (time.time() - start_time))
print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

restart = input("Would you like to restart? Enter yes or no? ")
if restart.lower() != 'yes':

 if __name__ == "__main__":
        main()
