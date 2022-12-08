def replace_substr(f_s1,f_s2,pos):
  f_s2 = f_s2.split(sep=" ")
  pos = pos - 3
  for i in f_s2:
    if i == f_s2[pos]:
      f_s2[pos] = f_s1
    else:
      continue
  return " ".join(f_s2)

s1 = 'lazy'
s2 = 'the quik brown fox'
s = replace_substr(s1,s2,4)
print(s) 	# output = the lazy brown fox
