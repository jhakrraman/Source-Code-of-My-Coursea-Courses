# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
value = float(0)
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else : 
        pos = line.find("0")
        pos1 = line.find(" ",pos)
        count += 1	
        value += float(line[pos:pos1])
print("Average spam confidence:", float(value/count))