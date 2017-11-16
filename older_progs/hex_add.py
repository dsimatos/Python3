hex_add = [(hex(x+y).replace('0x','')).upper() for x in range(5,16) for y in range(5,16)]
print '    5   6   7   8   9   A   B   C   D   E   F'
count=0; modu=11; fchar=5
for i in range(0,121):
	if count%11==0:
		print (hex(fchar).replace('0x','')).upper(),
		fchar+=1
	print '{:>3s}'.format(hex_add[i]),
	count+=1
	if count%11==0:
		print
