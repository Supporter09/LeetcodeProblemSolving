def checkInclusion(s1, s2):
    for i in range(len(s2) - len(s1)+1):
        if sorted(s1) == sorted(s2[i:i+len(s1)]):
            return True
        
    return False
print(checkInclusion("hello", "ooolleoooleh"))
