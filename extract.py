'''
	===========================================================================
    Filename:     	extract.py
    Description:    Extracts table content from text copied off of a web page
    Author:   	    Michael Kruzil (mkruzil@mikruweb.com) 
    Date Created:   7/21/2019 3:00 PM
	===========================================================================
'''
import functions

#Convert the content in the file to a string variable
str = functions.openTXT("content.txt")

#Step 1: Indicate the start and end markers of the table content in the string
start_marker = "Start extraction here"
end_marker = "End extraction here"

#Step 2: Extract the table content from the string
str = functions.trimText(start_marker, end_marker, str)

#Step 3: Convert the table content to a table array
rows = functions.convertWebTextToTable(str)

#Step 4: Pop off the headings row
headings = functions.getHeadings(rows)

#Print the table data
print(headings)
print(rows)

#Save the table to a CSV file
functions.saveCSV(headings, rows, "results.csv")