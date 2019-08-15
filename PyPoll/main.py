import os
import csv

election_csv = os.path.join('..', 'Resources', 'election_data.csv')
print(election_csv)
# Method 2: Improved Reading using CSV module

with open(election_csv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

# Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    Khan_Vote = 0
    Correy_Vote = 0
    Li_Vote = 0
    OTooley_Vote = 0

    # Read each row of data after the header
    for row in csvreader:
        if row[2] == "Khan":
            Khan_Vote += 1
        elif row[2] == "Correy":
            Correy_Vote += 1
        elif row[2] == "Li":
            Li_Vote +=1
        else:
            row[2] == "O'Tooley"
            OTooley_Vote +=1

    print(Khan_Vote)
    print(Correy_Vote)
    print(Li_Vote)
    print(OTooley_Vote) 

Total_Votes = (Khan_Vote + Correy_Vote + Li_Vote + OTooley_Vote)
print(Total_Votes)


