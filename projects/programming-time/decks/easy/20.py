# To check if two strings are
# equal to each other, first check
# the length, and then check the
# characters at each position.
def equal(a,b):
  if len(a) != len(b):
    return False

  for i in range(len(a)):
    if a[i] != b[i]:
      return False

  return True

x = '⚂'
y = '⚂'

# or just use x == y
if equal(x,y):
    print(x)
