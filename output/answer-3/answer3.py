import csv
f1=open(r"E:\internship-test2-master\input\question-3\main.csv","r")
reader=csv.reader(f1)
f2=open(r"E:\internship-test2-master\output\answer-3\main.csv","w",newline='')
writer=csv.writer(f2)
dict1={}
cnt=0
for i in reader:
    if cnt==0:
        cnt+=1
        continue
    t=(int(i[31]),int(i[30]))
    if t in dict1.keys():
        dict1[t].append([i[0],cnt-1])
    else:
        dict1[t]=[[i[0],cnt-1]]
    cnt+=1
writer.writerow(["","Team","Yellow Cards","Red Cards"])
for i in sorted(dict1.keys(),reverse=True):
    for j in dict1[i]:
        writer.writerow([j[1],j[0],i[1],i[0]])
f1.close()
f2.close()
    
