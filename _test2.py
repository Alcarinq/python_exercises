flist = []
for i in range(3):
    flist.append(lambda a = i: a)

a = [f() for f in flist]  # what will this print out?
print(a)
