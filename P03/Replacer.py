def replace_char(f_c,f_s2,pos):
    #Insert your codes here
    f_s2 = list(f_s2)
    for i in f_s2:
        if i == f_s2[pos]:
            f_s2[pos] = f_c
        else:
            continue
    return "".join(f_s2)

c = 'i'
s = 'kristy'
s = replace_char(c,s,5)
print(s)	# output = 'kristi'