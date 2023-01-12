#import modules
import os
import csv

#set csv file path
csvpath = os.path.join("Resources", "election_data.csv")
#open file, set reader variable, skip header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None)

#create variable for vote tally, set it to zero to start
    totalvotes = 0
#create a list for candidates, and a dictionary for the results
    candidates = []
    results = {}
#for loop - if candidate is not in results, add candidate to dictionary and set value to 1.  
#Once candidate has been added to dictionary, keep adding 1 every time their value pops up
    for row in csvreader:
        totalvotes = totalvotes +1
        if row[2] not in results:
           
            results[row[2]]= 1
        else:
             results[row[2]]+=1
    
#find max value from dictionary, return the key
    winner = max(results, key=results.get)

#print results
print(f"Election Results")
print(f"__________________________________")
print(f"Total Votes = {totalvotes}")
print(f"__________________________________")
tally = []
for a, b in results.items():
    tally.append(str(a) + ': ' + str(round(((b/int(totalvotes))*100),3))+ "% (" + str(b) + ")")
    print((str(a) + ': ' + str(round(((b/int(totalvotes))*100),3))+ "% (" + str(b) + ")"))

print(f"__________________________________")
print(f"Winner: {winner}") 
print(f"__________________________________")

#set file path for summary file
summary = 'summary.txt'

#print to text file

lines = [f"Election Results",f"__________________________________",f"Total Votes = {totalvotes}",f"__________________________________",'\n']
lines2 =['\n',f"__________________________________",f"Winner: {winner}",f"__________________________________"]
with open(summary, 'w') as text:
    text.write('\n'.join(lines))
    text.write('\n'.join(tally))
    text.write('\n'.join(lines2))
    text.close()
    
