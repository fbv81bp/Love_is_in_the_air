s = "Two can play that game."
count = []
for c in s:
    if c not in count:
        count.append(c)
pmr = []
for c in s:
    pmr.append(count.index(c)+1)    
code = []
for e in count:
    code.append(ord(e))
print('call codes:', code, 'all:', len(count))
print('channel series:', pmr)

