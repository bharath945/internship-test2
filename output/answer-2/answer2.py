import csv
f1=open(r"C:\Users\Lenovo\OneDrive\Desktop\internship-test2-master\input\question-2\main.csv","r")
reader=csv.reader(f1)
dict1={}
f2=open(r"C:\Users\Lenovo\OneDrive\Desktop\internship-test2-master\output\answer-2\main.csv","w",newline='')
writer=csv.writer(f2)
nd=0
for i in reader:
    if nd==0:
        nd+=1
        continue
    if i[3] not in dict1:
        dict1[i[3]]=[1<<31,-1<<31]
        dict1[i[3]][0]=min(dict1[i[3]][0],int(i[1]))
        dict1[i[3]][1]=max(dict1[i[3]][1],int(i[1]))
    else:
        dict1[i[3]][0]=min(dict1[i[3]][0],int(i[1]))
        dict1[i[3]][1]=max(dict1[i[3]][1],int(i[1]))
writer.writerow(["","min","max"])
for i in sorted(dict1.keys()):
    writer.writerow([i,dict1[i][0],dict1[i][1]])
f1.close()
f2.close()
