
f = open("captions-labelled.txt","w+")
with open("captions.txt", "r") as fd:
	count = 1
	for row in fd:
		f.write(str(count)+","+row)
		count += 1


f.close()
print(count)
