f = open("note.txt")
concordance = {}
lcount = 0

for aline in f:
    lcount = lcount + 1
    wordlist = aline.split()
    for aword in wordlist:
        
        if aword in concordance:
            if lcount not in concordance[aword]:
                concordance[aword].append(lcount)
        else:
            concordance[aword] = [lcount]
            
for aword in concordance:
	print(aword, "appears on line(s)", end="")
	for linenum in concordance[aword]:
		print(" ",linenum,"\n", end="")
