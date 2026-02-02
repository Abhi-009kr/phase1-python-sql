#Count frequency in list
l=[1,2,1,2,3,3,4,52]
d={}
for i in l:
    if i in d:
        d[i] +=1
    else:
        d[i]=1
print(d)

#Second Largest Number
nums = [10, 20, 4, 45, 99]
l2=sorted(nums)
print(l2[1])

#Remove duplicates (order same)
nums = [1,2,2,3,1,4]
num=[]
for i in nums:
    if i not in num:
        num.append(i)
print(num)

#Word count in string
text = "python is easy and python is powerful"
a = text.split()
d1={}
for j in a:
    if j in d1:
        d1[j]+=1
    else:
        d1[j]=1
print(d1)

#Student marks → total, average, grade
marks = [78, 85, 90, 66]
s = sum(marks)
avg = s/len(marks)
if avg>=80:
    grade = "A"
elif avg>=60:
    grade = "B"
else:
    grade = "C"

print("Total marks:-", s)
print("Average marks:-",avg)
print("Grade:-", grade)