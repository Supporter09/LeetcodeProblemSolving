# The idea is basically check sorted word 
# If exist in dict then append
# Else create that key with [word]

def groupAnagrams(strs):
    word_dict = dict()

    for word in strs:
        test = ''.join(sorted(word))
        if word_dict.get(test) != None:
            tmp = word_dict[test] + [word]
            word_dict[test] = tmp
        else:
            word_dict[test] = [word]

    return list(word_dict.values())

groupAnagrams(["eat","tea","tan","ate","nat","bat"])