def find_string(f_s1,f_s2):
  #  Insert your codes here
    pos = 0
    if (f_s1.upper() in f_s2.upper()):
        for i in f_s2:
          if i != f_s1[0]:
            pos += 1
          else:
            break
    else:
        pos -= 1
    return pos

s1 = 'qui'
s2 = 'the quick brown fox'
pos = find_string(s1, s2)
if pos == -1:			# s1 in s2 at index 4
  print('Not found')
else:
  print('Found at index:', pos)
