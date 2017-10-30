rainfile = open("rainfall.txt", "r")
outfile = open("rainfallfmt.txt", "w")

for aline in rainfile:
    values = aline.split()
    
    city = values[0]
    
    inches = float(values[1])
    outfile.write("%+25s %5.1 f" % (city, inches))

rainfile.close()
outfile.close()
