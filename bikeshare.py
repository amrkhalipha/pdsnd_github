#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 07:14:28 2019

@author: Khalipha
"""



import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

Months = ('january', 'february', 'march', 'april', 'may', 'june')
Days = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')

# Dictionary used to reference user input as integer to actual weekday name    
days_dict = {'1': 'sunday',
             '2': 'monday',
             '3': 'tuesday',
             '4': 'wednesday',
             '5': 'thursday',
             '6': 'friday',
             '7': 'saturday'}

def get_filters():

    Cities = ('chicago', 'new york', 'washington')
    
    
    print('\nYo Yo! Let\'s explore some US bikeshare data!')

    # While loop to handle any inputs other than "Chicago", "New York", or "Washington".
    # Used .casefold() to remove case sensitivity
    while True:
        city = input("Would you like to see data for Chicago, New York, or Washington?\n").casefold()
        if city in Cities:
            break
        print('\nOops! Please only choose from either Chicago, New York, or Washingston\n')

    # While loop to handle any inputs other than "both", "month", "day", "none".
    # Used .casefold() to remove case sensitivity
    while True:
        filter = input('\nWould you like to filter the data by month, day, both, or not at all? Type "none" for no time filter.\n').casefold()
        if filter in ('both', 'month', 'day', 'none'):
            break
        print('\nOops! Please only enter the words "month", "day", "both", or "none"\n')
    
    
    if filter == 'both':
        # While loop to handle any inputs other than correct month name from Months list.
        # Used .casefold() to remove case sensitivity
        while True:
            month = input("\nWhich month? January, February, March, April, May, or June?\n").casefold()
            if month in Months:
                break
            print('\nOops! Please make sure you have spelled the month correctly\n')
        # While loop to handle any inputs other than correct integer 1-7 for weekdays from Days list referencing days_dict Dictionary.
        while True:
            day = days_dict.get(input("\nWhich day? Please type your response as an integer (e.g., 1=Sunday).\n"))
            if day in Days:
                break
            print('\nOops! Please make sure you have entered a number from 1-7 (e.g., 1=Sunday).\n')
    
    elif filter == 'month':
          # While loop to handle any inputs other than correct month name from Months list.
        # Used .casefold() to remove case sensitivity
        while True:
            month = input("\nWhich month? January, February, March, April, May, or June?\n").casefold()
            if month in Months:
                break
            print('\nOops! Please make sure you have spelled the month correctly\n')
        day = "all"
    
    elif filter == 'day':
        # While loop to handle any inputs other than correct integer 1-7 for weekdays from Days list referencing days_dict Dictionary.
        while True:
            day = days_dict.get(input("\nWhich day? Please type your response as an integer (e.g., 1=Sunday).\n"))
            if day in Days:
                break
            print('\nOops! Please make sure you have entered a number from 1-7 (e.g., 1=Sunday).\n')
        month = "all"
    
    elif filter == 'none':
        month = "all"
        day = "all"
    # Confirmation statement to give better visibility to user on the filters chosen
    print ("\nFiltering data for the city of {} using the month filter {} and the day filter {}.\n".format(city.title(), month.title(), day.title()))
    print ('-'*40)
    return city, month, day
   
    
def load_data(city, month, day):
    
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['Month'] = df['Start Time'].dt.month_name()
    
    df['Day_Of_Week'] = df['Start Time'].dt.weekday_name
    
    # Added "City" column to inform user which City they are viewing data for
    df['City'] = city.title()
    
    # Replaced Gender fields that are NaNs with "Undisclosed"
    df['Gender'].fillna("Undisclosed", inplace = True)
    
     # Replaced User Type fields that are NaNs with "Undisclosed"
    df['User Type'].fillna("Undisclosed", inplace = True)
    
    if month in Months:
        df = df[df['Month'] == month.title()]
    
    if day in Days:
        df = df[df['Day_Of_Week'] == day.title()]
    
    # Renamed "Unnamed: 0" column to "Row #"
    return df.rename(columns={'Unnamed: 0':'Row #'})

def time_stats(df):
    
    print ("\nCalculating The Most Frequent Times of Travel...")
    
    
    print ("\nCalculating statistic...")
    print ("\nWhat is the most popular month for traveling?")
    start_timepopmonth = time.time()
    popular_month = df['Month'].mode()
    for popmonthvalue in popular_month:
        print (popmonthvalue)
    print ("That took %s seconds." % (time.time() - start_timepopmonth))
    
    
    print ("\nCalculating statistic...")
    print ("\nWhat is the most popular day for traveling?")
    start_timepopday = time.time()
    popular_day = df['Day_Of_Week'].mode()
    for popdayvalue in popular_day:
        print (popdayvalue)
    print ("That took %s seconds." % (time.time() - start_timepopday))
    
    
    print ("\nCalculating statistic...")
    print ("\nWhat is the most popular hour of the day to start your travels?")
    start_timepophour = time.time()
    popular_hour = df['Start Time'].dt.hour.mode()
    for pophourvalue in popular_hour:
        print (pophourvalue)
    print ("That took %s seconds." % (time.time() - start_timepophour))
    print ('-'*40)
    
def station_stats(df):
    
    print ("\nCalculating The Most Popular Stations and Trip...")
    
    
    print ("\nCalculating statistic...")
    print ("\nWhat is the most popular Start Station?")
    start_timepopstartstation = time.time()
    popular_start_station = df['Start Station'].mode()
    for popstartstationvalue in popular_start_station:
        print (popstartstationvalue)
    print ("That took %s seconds." % (time.time() - start_timepopstartstation))
    
    
    print ("\nCalculating statistic...")
    print ("\nWhat is the most popular End Station?")
    start_timepopendstation = time.time()
    popular_end_station = df['End Station'].mode()
    for popendstationvalue in popular_end_station:
        print (popendstationvalue)
    print ("That took %s seconds." % (time.time() - start_timepopendstation))
    
    
    print ("\nCalculating statistic...")
    print ("\nWhat was the most popular trip from Start to End?")
    start_timepopstarttoendstation = time.time()
    print (df.groupby(['Start Station', 'End Station']).size().nlargest(1))
    print ("That took %s seconds." % (time.time() - start_timepopstarttoendstation))
    print ('-'*40)
    
def trip_duration_stats(df):
    
    print ("\nCalculating Trip Duration...")
    
    
    print ("\nCalculating statistic...")
    print ("\nWhat was the total traveling done for 2017 through June?")
    start_timetripduration = time.time()
    total_duration = df['Trip Duration'].sum()
    print (str(total_duration) + " seconds")
    print ("That took %s seconds." % (time.time() - start_timetripduration))
    
    
    print ("\nCalculating statistic...")
    print ("\nWhat was the average traveling done for 2017 through June?")
    start_timeavgtripduration = time.time()
    avg_duration = df['Trip Duration'].mean()
    print (str(avg_duration) + " seconds")
    print ("That took %s seconds." % (time.time() - start_timeavgtripduration))
    print ('-'*40)
    
def user_stats(df):
    print ("\nCalculating User Stats...")
    
    print ("\nCalculating statistic...")
    print ("\nWhat is the breakdown of users?")
    start_timeusers = time.time()
    # Used try statement to handle KeyError incase user filtered by city that does not have "User Type" column
    try:
        print (df.groupby(['User Type'])['User Type'].count())
    except KeyError:
        print ('No user type data to share.\nNone')
    print ("That took %s seconds." % (time.time() - start_timeusers))
    
    
    print ("\nCalculating statistic...")
    print ("\nWhat is the breakdown of gender?")
    start_timegender = time.time()
    # Used try statement to handle KeyError incase user filtered by city that does not have "Gender" column
    try: 
        print (df.groupby(['Gender'])['Gender'].count())
    except KeyError:
        print ('No gender data to share.\nNone')
    print ("That took %s seconds." % (time.time() - start_timegender))
    
    
    print ("\nCalculating statistic...")
    print ("\nWhat is the oldest, youngest, and most popular year of birth, respectively?")
    start_timebirthyear = time.time()
    # Used try statement to handle KeyError incase user filtered by city that does not have "Birth Year" column
    try:
        print ('Oldest: ' + str(int(df['Birth Year'].min())) + '\nYoungest: ' + str(int(df['Birth Year'].max())) + '\nMost Popular: ' + str(int(df['Birth Year'].mode())))
    except KeyError:
        print ('No birth year data to share.\nNone')
    print ("That took %s seconds." % (time.time() - start_timebirthyear))
    print ('-'*40)
    
def individual_trip_data(df):   
  
    # Calculated row_length to use in for loop for range end
    row_length = df.shape[0]
    
    for i in range(0, row_length, 5):
        print ('\nDisplaying individual trip date...\n')  
        print (df.iloc[i:i+5])
        print ('-'*40)
        viewmore = input('\nWould you like to view more individual trip date? Enter yes or no.\n')
        if viewmore.lower() != 'yes':
            break
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
    
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        individual_trip_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
    
if __name__ == "__main__":
    main()