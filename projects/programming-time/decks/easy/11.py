# | computer memory      |
# |......................| 0  - 21
# |..2 2 104 101.........| 22 - 43
# |..^...................| 44 - 65
# |..|...2 3 108 108 111.| 66 - 87
# |..|...^...............| 88 -109
# '--+---+---------------'
# x -+   |    x addr: 24
# y -----+    y addr: 72
#
# ASCII:
#  a -> 97
#  b -> 98
#  c -> 99
#  ...
#
# len() returns the length of a
# string.

x = 'he'
y = 'llo'

print(len(x) + len(y))
