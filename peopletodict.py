f=open("people.txt",'r+')

peeps = {}

# Loop over the lines in the file and fill the dictionary
for line in f:
    peeps[line.split()[0]] = int(line.split()[1])

print(peeps)
