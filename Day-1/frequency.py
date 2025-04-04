freq="To speak to a computer in its non-human language, we came up with two solutions interpreters and compilers. Ironically, most of us know very little about them, although theyre a part of our daily coding life."
words=freq.split()
print(words)
dict={}

for i in freq:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)