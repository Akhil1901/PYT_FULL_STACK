
"""Write a program to find the longest consecutive increasing subsequence in a list of 
integers. 
Input: [1, 2, 3, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5] 
Output : [1,2,3,4,5]  """
"""li=[1,2,3,1,2,3,4,5,1,2,3,4,5,]
curr_list=[]
long_list=[]
for i in range(len(li)):
    first=li[i]
    prev=li[i-1]
    if(first>prev):
        curr_list.append(prev)
        curr_list.append(first)
    else:
        curr_list.clear()
    if(len(curr_list)>len(long_list)):
        for j in curr_list:
            if(j not in long_list):
                long_list.append(j)
print(long_list)"""

"""Write a Python program to decode a string where a number before brackets indicates 
how many times the characters inside the brackets should be repeated. 
Input: 3[a]2[bc] 
Output: aaabcbc """
"""st = "3[a]2[bc]"
n_st = ""
for i in range(len(st)):
    count = 0
    content = ""
    if st[i]=="[":
        for j in range(i+1,len(st)):
            if st[j]=="]":
                break
            content+=st[j]
    if st[i]=="[":
        count=int(st[i-1])
    n_st+=count*content
print(n_st)"""

""" 3. Write a program to group all the words that are anagrams of each other. 
 Explaination: Two words are called anagrams if they contain the same characters with the same frequency, but the characters may appear in a different order. 
 Input: ["eat", "tea", "tan", "ate", "nat", "bat"] 
 Output: [["eat", "tea", "ate"],["tan", "nat"],["bat"]]"""
"""li = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups= {}
for i in li:
    words = i
    key = tuple(sorted(i))
    if key not in groups:
        groups[key] = [words]
    else:
        groups[key].append(words)
print(list(groups.values()))"""
"""4. Write a program to count all substrings that are palindromes in a given string.A palindromic substring is a substring that reads the same forward and backward. For "aaa", the palindromic substrings are a, a, a, aa, aa, aaa, so the total count is 6. 
Input: ’aaa’ 
Output: 6 """
st = "aaa"
count=0
for i in range(len(st)):
    for j in range(i+1,len(st)+1):
        sub = st[i:j]
        if sub == sub [::-1]:
            count+=1
print(count) 
