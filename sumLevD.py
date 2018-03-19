def lev(a, b):
    if not a: return len(b)
    if not b: return len(a)
    return min(lev(a[1:], b[1:])+(a[0] != b[0]), lev(a[1:], b)+1, lev(a, b[1:])+1)

finalData = []
levSum = 0

with open("data.txt","r") as d:
    myData = d.readlines()
    for i in myData:
        i = i.split()
        finalData.append(i)
    for j in finalData:
        levSum += lev(j[0],j[1])
    print(levSum)
