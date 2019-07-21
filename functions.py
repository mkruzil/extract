'''
	===========================================================================
    Filename:     	functions.py
    Description:    Functions used by extract.py
    Author:   	    Michael Kruzil (mkruzil@mikruweb.com) 
    Date Created:   7/21/2019 3:00 PM
	===========================================================================
'''

#Read the contents of a text file into a string
def openTXT(path):
    file = open(path, "r")
    str = file.read()
    return str

#Get the contents of a CSV file
def openCSV(path):
    #Get the contents of the file
    str = openTXT(path)
    arr = str.split()

    #Convert the array into table rows
    rows = []
    for line in arr:
       row = line.split(",");
       rows.append(row)

    return rows

#Pop off the headings row from an array
def getHeadings(rows):
    headings = rows.pop(0)
    return headings

def trimText(start_marker, end_marker, text):
    #Get the start and end positions
    start_pos = text.find(start_marker)
    end_pos = text.find(end_marker)

    #If the start and end markers were found
    if (start_pos > -1) and (end_pos > -1):
        #Advance the start position to skip over the start marker
        start_pos += len(start_marker) + 1
        #Rewind the end position to trim off the trailing character
        end_pos -= 1
        #Extract the marked text
        text = text[start_pos:end_pos]
    return text

def convertWebTextToTable(str):
    rows = []
    #Split the text into an array of lines
    lines = str.split("\n")
    #Pop off the headings line
    headings = getHeadings(lines)
    #Convert the headings line into columns (heading values are assumed to be delimited by tabs)
    headings = headings.split("\t")
    #Get the number of columns
    length = len(headings)
    #Initialize a new row and counter
    row = []
    i = 0
    #Loop through the lines array, converting each line into columns
    for line in lines:
       row.append(line)
       i = i + 1
       #If the number of columns is reached, push the row into the table array
       if i == length:
           rows.append(row)
           #Reinitialize the row data
           row = []
           i = 0
    #Push the headings row back onto the table array
    rows.insert(0, headings)
    return rows

#Save the modified contents to a CSV file
def saveCSV(headings, rows, path):
    #Reattach the headings row
    rows.insert(0, headings)

    #Convert the rows back to a string
    str = ""
    hlen = len(headings)
    rlen = len(rows)
    i = 0
    for row in rows:
        j = 0
        for value in row:
            str += value
            if j < hlen - 1:
                str += "," 
            else:
                if i < rlen - 1:
                    str += "\n"
            j += 1 
        i += 1

    #Write the results to a new file
    file = open(path, "w")
    file.write(str)  
