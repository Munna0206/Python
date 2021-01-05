#String Count
def strcount(string):
    dict={i:string.count(i) for i in string}
    return dict

def wordcount(string):
    lst=string.split()
    max=0
    for i in lst:
        if(max<len(i)):
            max=len(i)

    for i in range(max+1):
        for j in lst:
            if(i==len(j)):
                print(str(j),":",str(len(j)))


# This function computes LCM
def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm

#Palindrome
def pal(str):
    set2=set()
    rev=str[::-1]
    size=0
    #Palindrome
    for i in range(len(str)):
        for j in range(i+1,len(str)+1):
            if(str[i:j] in rev):
                if(len(str[i:j])>size):
                    size=len(str[i:j])
                set2.add(str[i:j])
    print("Palindrome:",set2)
    
    newlist=[i for i in set2 if(len(i)==size)]
    print("\nLongest:",newlist)

#Reverse
def rev(str2):
    list=str2.split()
    print(list)
    for i in list:
        print(i[::-1],end=" ")



#Remove Characters
def rm(str1,str2):
    for i in str1:
        if(i in str2):
            str2=str2.replace(i,'')
    print("String 1:",str1)
    print("String 1:",str2)

#Date Validation
def date_validation(day, month, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        max_day_value = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_day_value = 30
    elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        max_day_value = 29
    else:
        max_day_value = 28
    if day in range(1,day > max_day_value+1):
        print("Date is invalid.")
    else:
        print("Valid Date")

#Append at the end
def string_encode(str1):
    lst=str1.split()
    count2=[]
    for i in lst:
        count2.append(len(i))
    print(count2)
    str1=str1.replace('a','@')
    str1=str1.replace('e','e#')
    str1=str1.replace('m','m$')
    str1=str1.replace('t','t%')
    str1=str1.replace('i','i&')
    counti=0
    text1=""
    for i in range(len(str1)):
        if(str1[i] == ' '):
            text1=text1+str(count2[counti])
        else:
            text1=text1+str1[i]
    print(text1)


def calcfrequency(str1):
    lst=[]
    lst.extend(str1)
    for i in str1:
        if(i!=" "):
            print(i,":",lst.count(i))