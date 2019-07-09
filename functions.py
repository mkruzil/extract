'''
	===========================================================================
    Filename:     	functions.py
    Description:    Functions used by extract.py
    Author:   	    Michael Kruzil (mkruzil@mikruweb.com) 
    Date Created:   7/7/2019 4:00 PM
	===========================================================================
'''

#Get the contents of the CSV file
def openCSV(path):
    #Read the contents of the CSV file into an array of lines
    file = open(path, "r")
    str = file.read()
    arr = str.split()

    #Convert the array into table rows
    rows = []
    for line in arr:
       row = line.split(",");
       rows.append(row)

    return rows

#Extract the headings row
def getHeadings(rows):
    headings = rows.pop(0)
    return headings

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
