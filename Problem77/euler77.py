def isPrime(n, primeList):
    for prime in primeList:
        if (n % prime == 0):
            return False
    return True

def returnPrimeList(num):
    primeList = [2,3,5,7]
    for i in range (8, num+1):
        if isPrime(i, primeList):
            primeList.append(i)
    return primeList

def findIndexLessThan(num, primeList):
    for i in range(0, len(primeList)):
        if primeList[i] > num:
            return i-1
        if primeList[i] == num:
            return i
    return len(primeList)-1

def fillSumsPrime(num):
    primeList = returnPrimeList(num)
    for n in range (2, num+1):        
        append_this = [0, 0]
        for k in range (2, num+1):
            if n == 0:
                append_this.append(1)
            elif n == 1:
                append_this.append(0)
            elif n == 2:
                append_this.append(1)
            elif n == 3 and k <= 2:
                append_this.append(0)
            elif n == 3:
                append_this.append(1)
            elif k > n:
                append_this.append(append_this[n])
            else:
                totalSum = 0
                for i in primeList[:findIndexLessThan(k, primeList) + 1]:
                    if (n-i < 0):
                        totalSum += 0
                    else:
                        totalSum += sum_array[n-i][i]
                append_this.append(totalSum)
        sum_array.append(append_this)
        

def findNum(n):
    append_this = []
    for i in range(0, n+1):
        append_this.append(1)
    sum_array.append(append_this)
    append_this = []
    for i in range(0, n+1):
        append_this.append(0)
    sum_array.append(append_this)
    fillSumsPrime(n)
    return (sum_array[n][n-1])

sum_array=[]
for i in range(0,100):
    sum_array=[]
    if (findNum(i) > 5000):
        print(i)
        break
