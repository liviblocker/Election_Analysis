# # print("How Many Numbers?")
# # y = 0
# # while y <= 5:
# #     print(y)
# #     y = y + 1
# def average(list_of_numbers):
#     #print(my_list)
#     list_len = len(list_of_numbers)
#     list_sum = 0
#     for my_var in list_of_numbers:
#         #Below syntax is the same as list_sum = list_sum + my_var
#         list_sum += my_var

#     return list_sum/list_len

# # Test your function with the following:
# my_list = [1, 5, 9]
# results = average(my_list)
# print(results)
# #print(list_len)

# import os
# import csv

# Path to collect data from the Resources folder

# Define the function and have it accept the 'wrestlerData' as its sole parameter

# Find the total number of matches wrestled

# Find the percentage of matches won

# Find the percentage of matches lost

# Find the percentage of matches drawn

# Print out the wrestler's name and their percentage stats

# # Read in the CSV file
# with open(wrestling_csv, 'r') as csvfile:

#     # Split the data on commas
#     csvreader = csv.reader(csvfile, delimiter=',')

#     # Prompt the user for what wrestler they would like to search for
#     name_to_check = input("What wrestler do you want to look for? ")

#     # Loop through the data
#     for row in csvreader:

#         # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
#         if(name_to_check == row[0]):
#             print_percentages(row)

# Import the datetime class from the datetime module.
import datetime as dt