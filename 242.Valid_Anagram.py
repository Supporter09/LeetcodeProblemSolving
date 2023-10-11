# Approach 1: Using sort then compare
# TC: O(n.log(n))
# SC: O(n)
# def isAnagram(s, t):
#     return sorted(s) == sorted(t)

# print(isAnagram('rat', 'car'))

# => But there is no reason for sorting string. All we need is the frequencies of char

# Approach 2: Using hashmap
# The thing that make .get good is it accepts second argument is the default value return if the key does not exist
# TC: O(n)
# SC: O(n)
def isAnagram(s, t):
    f_set = {}
    s_set = {}

    for char in s:
        f_set[char] = f_set.get(char, 0) + 1

    for char in t:
        s_set[char] = s_set.get(char, 0) + 1

    return f_set == s_set

print(isAnagram('anagram', 'nagaram'))