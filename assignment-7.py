
"""
def vowel_convert(fun):
    def innerfun(n):
        output=""
        vowels="aieou"
        space=" "
        res=fun(n)
        for i in range(len(res)):
            if(res[i] in vowels):
                ans=res[i].upper()
                output=output+ans
            else:
                output=output+res[i]
        return output
    return innerfun

def decorator(fun):
    start="***"
    total=""
    def inner_fun(n):
        res_str=fun(n)
        total=start+res_str+start
        return total
    return inner_fun
@decorator
@vowel_convert
def string(n):
    return n

n="hello world"
print(string("hello world"))"""



"""def generator_word(s):
    words=s.split()
    for i in range(len(words)-1,-1,-1):
        yield words[i]

s="python is very powerful"
for i in generator_word(s):
    print(i)"""



def s_o_d(n):
    if(n<=9):
        return n
    else:
        return s_o_d(n//10+n%10)
print(s_o_d(98756))
