#1
def add(a,b):
    return a + b
#2    
def max(a,b):
    if (a>b):
        print ("a is max")
    else:
        print ("b is max")
#3
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
#4
def si(p,t,r):
    return (p*t*r)/100
#5
def ci(p,t,r):
    return (p*((1+r/100)**t-1))
#6
def sum_of_digits(n):
    i=0
    while (n>0):
        i=i+(n%10)
        n=n//10
    return i
#7
def amst(n):
    m=n  
    a=str(n)
    b=len(a)
    i=0
    while (n>0):
        i=i+(n%10)**b
        n=n//10
    if (m==i):
        print ("its an amstrong")
    else:
        print ("not an amstrong")
    #if we not put return statement it state none in out put
#8
def area_circle(r):
    return (3.141*r**2)
#9
def prime(n):
    for i in range(2,n):
        if (n%i==0):
            print ("not a prime")
            break
    else:
        print ("its a prime")
#10
def prime_interval(m,n):
    for i in range(m,n+1):
            if i>1:
                for j in range(2,n):
                    if (i%j==0):
                      break
            else:
                print (i)
#11            
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
#12
def fib_or_not(n):
    import math
    a=(5*n*n+4)
    b=(5*n*n-4)
    c=math.sqrt(a)
    d=math.sqrt(b)
    if(c*c==a or d*d==b):
        print('its a fibinacci')
    else:
        print('not a fibinacci')
#13
def sum_of_cb(n):
    return (n*(n+1)/2)**2//1
#14
def sum_of_n(n):
    return (n*(n+1))/2
#15
def sum_of_sqre_of_n(n):
    return n*(n+1)*((2*n+1))//6
#16
def ascii(n):
    return ord(n)
#17
def prime1(n):
    if(n>1):
        i=1
        while(i<n-1):
            i=i+1
            a=n%i
            
            if(a==0):
                return a
        else:
            return 'its prime'
#18
def sort(arr):
    l=len(arr)
    b=[]
    while (l>0):
        m=max(arr)
        b.append(m)
        arr.remove(m)
        l=l-1
    print('dessending order',b)
    return 'assending order',b[::-1]
#19
def sum_of_arr(arr):
    sum=0
    for i in range(0,len(arr)):
        sum=sum+arr[i]
    return sum 
#20
def max_in_arr(arr):
    return max(arr)

#21
def largest(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max
#22
def rot(array,d):
       return  array[d:len(array)]+array[0:d]

#23
def rem_of_arr_divided_by_n(arr,n):
    pro=1
    for i in range(0,len(arr)):
        pro=pro*arr[i]
    return pro%n
#24
def swaplist_1st_and_last(list):
    l=len(list)
    a=list[0]
    list[0]=list[l-1]
    list[l-1]=a
    return list
#25
def lenoflist(list):
    return len(list)
#26
def clearlist(list):
    return list.clear
#27
def placevalue(n):
    l=n
    j=0
    while (n>0):
        i=(n%10)
        n=n//10
        j=j+1
        print(j,'s place of number is',i)
    return 'number is',l
#28
def duplicate(list):
    a=[]
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if (list[i]==list[j]):
                if list[i] in a:
                    break
                else:
                    a.append(list[i])
    return a
        

#29 
def removeduplicate(list):
    a=[]
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if (list[i]==list[j]):
                if list[i] in a:
                    break
                else:
                    a.append(list[i])
    for k in range(0,len(a)):
        list.remove(a[k])
    return list
#30
def cumsumlist(list):
    a=[]
    sum=0
    for i in range(0,len(list)):
        sum=list[i]+sum
        a.append(sum)
    return a

#31
def palindrome(n):
    m=str(n)
    if (m==m[::-1]):
        return 'its a palindrome'
    else:
        return 'not a palindrome'
#32
def sum_dig_list(list):
    arr=[]
    for n in range(0,len(list)):
        m=list[n]
        k=str(m)
        l=len(k)
        i=0
        while (m>0):
            i=i+m%10
            m=m//10
        arr.append(i)   
    return arr
#33
def positive_list(list):
    for i in list:
        if(i<0):
            list.remove(i)
    return list
        
#34
def negetive_list(list):
    for i in range(0,len(list)):
        if (list[i]>0):
            list.remove(list[i])
    return list

#35
def even_list(list):
    for i in list:
        if(i%2!=0):
            list.remove(i)
    return list
#36
a=[[1,2,3],[1,2,3],[1,2,3]]
b=[[1,2,3],[1,2,3],[1,2,3]]
r=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,len(a)):
    for j in range(0,len(a[0])):
        r[i][j]=a[i][j]+b[i][j]
for i in range(0,len(r)):
    for j in range(0,len(r[0])):
        print(r[i][j])
#37
import numpy as np
a=np.array([[6,1,1],[1,3,-3],[2,8,7]])
b=np.array([[1,2,3],[1,2,3],[1,2,3]])
c=np.array([1,1,3])
print(np.add(a,b))
print(np.subtract(a,b))
#38
print(np.dot(a,b))
#39
print(np.transpose(a))
#40
print(np.linalg.det(a))
#41 
print(np.linalg.inv(a))
#42 to find unqnowns as A*UNKNOWN=C
#unqnown =A inverse*C
print(np.dot(np.linalg.inv(a),c))
#43
print(np.trace(a))
#44
print(np.mean(c))
#45
print(np.median(c))
#46
import statistics
print(statistics.mode(c))
#47 for  how many times element is repeated
def count(d,m):
    print(d.count(m))
#48
def round(n):
    print(round(4.6))
#49
def abs(n):
    print(abs(-4.6))
#50
def int(n):
    print(int(-4.6))
#51
def max_int(n):
    return n//1
#52
def col_matrics(mat,c):
    for i in range(0,len(mat)):
        print(mat[i][c-1])
    return ''
print(col_matrics([[1,2,3],[1,2,3],[1,2,3]],1))
#53
def Rank_of_matrice(mat):
    import numpy
    return(numpy.linalg.matrix_rank(mat))
#54
def trace_of_mat(mat):
# we can use np.trace(matrice)
    sum=0
    for i in range(0,len(mat)):
            sum=sum+mat[i][i]
    return sum  
#56
def upper_triangler_mat(mat):
    for i in range(0,len(mat)):
        for j in range(0,len(mat[0])):
             if i>j:
                 mat[i][j]=0
    return mat,'upper triangler'
#57
def lower_triangler_mat(mat):
    for i in range(0,len(mat)):
        for j in range(0,len(mat[0])):
             if i<j:
                 mat[i][j]=0
    return mat,'lower triangler'
#58
def dia_of_mat(mat):

    for i in range(0,len(mat)):
            print(mat[i][i])
    return 'are the diagonal elements'



#59
def vre_con_matrics_str(mat):
    b=[]
    j=0
    while(len(b)<len(mat)):
        sum=''
        for i in range(0,len(mat)):
            sum=sum+str(mat[i][j])
        b.append(sum)
        j=j+1
    return b
#60
def hor_con_matrics_str(mat):
    b=[]
    j=0
    while(len(b)<len(mat)):
        sum=''
        for i in range(0,len(mat)):
            sum=sum+str(mat[j][i])
        b.append(sum)
        j=j+1
    return b
#61
def vre_con_matrics(mat):
    b=[]
    j=0
    while(len(b)<len(mat)):
        sum=0
        for i in range(0,len(mat)):
            sum=sum+(mat[i][j])
        b.append(sum)
        j=j+1
    return b
#62
def hor_con_matrics(mat):
    b=[]
    j=0
    while(len(b)<len(mat)):
        sum=0
        for i in range(0,len(mat)):
            sum=sum+(mat[j][i])
        b.append(sum)
        j=j+1
    return b
#63 number conversions (binqry,octal,hexa,etc...)
def to_m(n,m):
    i=[]
    while(n>0):
        a=n%m
        n=n//m
        i.append(a)
    b=i[::-1]
    for j in range(0,len(b)):
        print(b[j],end='')
    return ''
#64
def rev(n):
    return n[::-1]
#65
def rev_of_sen(a):
    b=a.split('+')
    return '-'.join(b[::-1])
#66
def array_join(a):
    return ' '.join(a)
#67
#remove charecter in str
def rem_from_str(a,m,z):
    # string.replace(old char,new char,how many number of old char it should remove)
    return a.replace(m,' ',z)
    
#68 to remove element through index
def rem_i_from_str(n,i):
    return n[0:i]+n[i+1:len(n)]

#69
def rem_fromstr(n,i):
    s=n[i]
    a=n.split(str(s))
    return ' '.join(a)
#70
def sub_str(str,sub):
    if sub in str:
        print('found')
    else:
        print('not found')
#71
def sub_str_replace(string,sub,a):
    
    if sub in string:
         n=string.replace(str(sub),' ',a)
         return n
    else:
        return 'not found'
#72
def cout_sub_in_str(n,m):
    a=n.count(str(m))
    return a
#73
def len_str(n):
    return len(n)
#74
def freq(n,w):
    return n.count(str(w))

#75
def freq_in_str(n):
    a=n.split(' ')
    for i in range(len(a)):
        b=a.count(a[i])
        print(b,'is frequency of',a[i])
#76
def even_length(n):
    a=n.split(' ')
    for i in range(len(a)):
        if len(a[i])%2==0:
            print(a[i],':even length')
        else:
            print(a[i],':odd length')
    return ''    
#77
def pascals(n):
    a=n.split('_')
    print(a)
    return ''.join(a)#(or)return ' '.join(n.split('_'))
#78
def vowels(n):
    if 'a' and 'e'and 'i'and 'o'and 'u' in n:
        print('found:',n)
        return ''
    else:
        print('not found:')
#79
def matching(a,b):
    for i in range(0,len(a)):
        if a[i] in b:
            print(a[i])
    return ''
#80
def min_freq(n):
    for i in range(0,len(n)):
        p=n.count(n[i])
        if p==1:
            return n[i]
print(min_freq('geeksforgeeks'))
        





            

