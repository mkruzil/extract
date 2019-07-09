'''
	===========================================================================
    Filename:     	extract.py
    Description:    Applies data extraction rules on a CSV file
    Author:   	    Michael Kruzil (mkruzil@mikruweb.com) 
    Date Created:   7/7/2019 4:00 PM
	===========================================================================
'''
import functions

#Read a CSV file into a list of rows
rows = functions.openCSV("data.csv")

#Extract the headings row
headings = functions.getHeadings(rows)

#Add two new columns to the headings row
headings.append("first_two_letters_of_name")
headings.append("content_to_the_left_of_period")

#Perform the data extraction
i = 0
for row in rows:
    #Get the value of the first column in each row
    value = row[0]
 
    #Rule 1: Extract the first two letters of the value
    initials = value[0:2]
    #Insert the new value in a new column
    rows[i].append(initials)

    #Rule 2: Extract everything to the left of the period
    #Get the position of the period in the string
    period_pos = value.find(".")
    #If a period is found, extract everything to the left of it. Otherwise, keep the entire value
    if period_pos != -1:
        value = value[0:period_pos]
    #Insert the new value in a new column
    rows[i].append(value)
 
    i += 1

#Print the modified table
print(headings)
print(rows)

#Save the modified table to a new file
functions.saveCSV(headings, rows, "results.csv")