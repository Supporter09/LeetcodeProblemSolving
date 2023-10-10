def generate(numRows):
    arr = [[1], [1,1]]
    if numRows == 1:
        return [arr[0]]
    elif numRows == 2:
        return arr
    else:
        j = 2
        while j < numRows:
            tmp = []
            for i in range(j + 1):
                if i == 0 or i == j:
                    tmp.append(1)
                else:
                    res = arr[j - 1][i-1] + arr[j - 1][i]
                    tmp.append(res)
            arr.append(tmp)
            j += 1
    print(arr)


print(generate(1))
