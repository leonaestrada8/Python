"""
strings = ["ab","ab","abc"]
queries = ["ab","abc","bc"]


There are 2 instances of "ab", 1 of 'abc' and 0 of 'bc'. For each query, add an element to the return array, 
results = [2,1,0].

"""

def matching(strings, queries):
    count = [0] * len(queries)
    for i in range(0, len(strings)):
        for j in range(0,len(queries) -1):
            if queries[j] == strings[i]:
                count[j] += 1
    print(count)



strings = ["ab","ab","abc"]
queries = ["ab","abc","bc"]

matching (strings, queries)