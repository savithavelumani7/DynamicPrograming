


def repeat(string, word):
    k = 0
    while word * (k + 1) in string:
        k += 1
    return k

string=str(input())
word=str(input())
result=repeat(string,word)
print(result)