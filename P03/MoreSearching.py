def find_string(f_s1, f_s2):
  #  Insert your codes here
  isFound = True

  if (f_s1.upper() in f_s2.upper()):
    isFound = True
  else:
    isFound = False

  return isFound
  
s1 = 'ox'
s2 = 'the quick brown fox'
print(find_string(s1, s2))