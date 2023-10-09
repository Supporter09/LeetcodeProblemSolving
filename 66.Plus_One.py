
def plusOne(digits):
    tmp = [str(x) for x in digits]
    num = int(''.join(tmp))
    num += 1
    arr = [int(x) for x in str(num)]
    return arr

print(plusOne([9]))
