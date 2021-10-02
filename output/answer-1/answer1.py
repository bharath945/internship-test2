import csv
f1=open(r"E:\internship-test2-master\input\question-1\main.csv")
reader=csv.reader(f1)
f2=open(r"E:\internship-test2-master\output\answer-1\main.csv","w",newline='')
writer=csv.writer(f2)
cnt=0
lst=[]
for i in reader:
    i.pop(2)
    if cnt==0:
        writer.writerow([" "]+i[1:])
        cnt+=1
        continue
    if len(lst)==0:
        for j in i:
            lst.append(int(j))
    else:
        if (int(i[0])-int(lst[0]))<=9:
            for j in range(1,11):
                lst[j]=int(lst[j])+int(i[j])
        else:
            writer.writerow(lst)
            lst=[]
            for j in i:
                lst.append(j)
    cnt+=1
if len(lst)!=0:
    writer.writerow(lst)
f1.close()
f2.close()
