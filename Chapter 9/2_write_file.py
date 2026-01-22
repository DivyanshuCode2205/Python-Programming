str = 'Hey, today\'s day is totally hectic for me.'

f = open("myfile_2.txt", "w") # creates the file if it doesn't exit

f.write(str) # writes the content of str to file
f.close()