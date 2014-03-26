# -*- coding: utf-8 -*-
import time
import random
#--------------------------Laboration 1------------------------------------------
def randarray(antal):
                                                            # Skapar en slumpmässigt fylld array.
    y = 0
    a =[]
    while y < antal:
        y = y + 1
        a.append(random.randint(1, 100))
        #print a
    return a

def makearray(antal):

    y = 0
    a =[]                                                   # Skapar en ordnad array.
    while y < antal:
        a.append(y)
        y = y + 1
    return a

def msort(array,m):

    if len(array) <= 1: return array
    if m > len(array): m = len(array)
    
    noe = len(array)/m
    re = len(array)%m
    nr_arrays = 0
    end = 0
    
    if re != 0:
        end = noe
    else:
        end = noe + re

    for i in range(0, m):
        if nr_arrays < m:
            array[i:i+end]=[array[i:i+end]]
            nr_arrays += 1

            if nr_arrays == m-1:
                end += re 

    for x in range(0,len(array)):
        array[x] = msort(array[x],m)
        
    while len(array) > 1:
        array[:2] = [merge(array[0],array[1])]
    result = array[0]

    return result

def merge(left,right):
    result=[]
    x, y = 0, 0
    while x < len(left) and y < len(right):
        if left[x] <= right[y]:
            result.append(left[x])
            x += 1
        else:
            result.append(right[y])
            y += 1
            
    result += left[x:]
    result += right[y:]
    return result


import random
import time
import copy

def maketestsets(n):
	tmplst = [[],[],[],[],[]]
	for x in range(0,n):
		tmplst[0].append(random.randrange(0,n))	
		tmplst[1].append(random.randrange(-n,n))	
		tmplst[2].append(random.randrange(0,n/10))	
		tmplst[3].append(random.randrange(0,n*100))	
		tmplst[4].append(x)
	tmplst[4].sort()
	tmplst[4].reverse()
	return tmplst


testlst=maketestsets(1000)
testlst2=copy.deepcopy(testlst)
print '-'*32
print 'm=2'
for sub in testlst:
    t1=time.time()
    msort(sub,2)
    print time.time()-t1
print '-'*32
testlst = copy.deepcopy(testlst2)
print 'm=10'
for sub in testlst:
    t1=time.time()
    msort(sub,10)
    print time.time()-t1
print '-'*32
testlst = copy.deepcopy(testlst2)
print 'm=100'
for sub in testlst:
    t1=time.time()
    msort(sub,100)
    print time.time()-t1

print '-'*32
testlst = copy.deepcopy(testlst2)
print 'm=1000'
for sub in testlst:
    t1=time.time()
    msort(sub,1000)
    print time.time()-t1
print '-'*32
testlst = copy.deepcopy(testlst2)
print 'm=10000'
for sub in testlst:
    t1=time.time()
    msort(sub,10000)
    print time.time()-t1
print '-'*32







