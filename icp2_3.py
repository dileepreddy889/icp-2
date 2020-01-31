fname = open("icp2text.txt", 'r')

d= dict()

for line in fname:
        line = line.lower()
        words = line.split()
        for word in words:
                if word in d:
                        d[word] = d[word] + 1
                else:
                        d[word] = 1
print(d)
f = open("icp2text.txt","a")
f.write(str(d))

