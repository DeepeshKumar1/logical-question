a = open('deepesh.txt', 'r')
b = a.read()
c = b.split()
print c
next_word =  c[c.index('Checkpoint') + 2]
print next_word



