res1 = [ ]
res2 = [ ]
res3 = [ ]
res4 = [ ]
res5 = [ ]
n = 0

a = input('Input any amount of 1,2,3 in random sequence: ')
def check(a):
    alph = ('1','2','3')
    if not a:
        return True
    for j in a:
        if j is alph:
            return True
              
while check(a):
    a = input('Only 1,2,3 in any amount and sequence: ')
   
for i in a:
    if(a[n]) == '1':
        res1.append('*')
        res2.append('*')
        res3.append('*')
        res4.append('*')
        res5.append('*')
        n += 1
    elif(a[n]) == '2':
        res1.append('222222')
        res2.append('     2')
        res3.append('222222')
        res4.append('2     ')
        res5.append('222222')
        n +=1
    elif(a[n]) == '3':
        res1.append('333333')
        res2.append('     3')
        res3.append('333333')
        res4.append('     3')
        res5.append('333333')
        n +=1
   
    
myString1 = '  '.join(res1)
print(myString1)
myString2 = '  '.join(res2)
print(myString2)
myString3 = '  '.join(res3)
print(myString3)
myString4 = '  '.join(res4)
print(myString4)
myString5 = '  '.join(res5)
print(myString5)
