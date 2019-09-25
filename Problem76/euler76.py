def fillSums(num):
    for n in range (1, num+1):
        append_this = [0]
        for k in range (1, num+1):
            if n == 1:
                append_this.append(1)
            elif k == 1:
                append_this.append(1)
            elif k > n:
                append_this.append(append_this[n])
            else:
                totalSum = 0
                for i in range (1, k+1):
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
    fillSums(n)
    print(sum_array[n][n-1])

sum_array = []    
findNum(100)
