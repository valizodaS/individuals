import os

def doOp(var1, var2, op):
	res = 0
	if op == '+':
		res = var1+var2
	elif op == '-':
		res = var1-var2
	elif op == '/':
		if var2 == 0:
			return 'div by zero'
		res = var1/var2
	elif op == '*':
		res = var1 * var2
	elif op == '^':
		res = pow(var1,var2)
		
	return int(res*10000)/10000 # округляем до 5 знаков после запятой

fullPath = os.getcwd()
fname = input('вводите имя файла(по умолчанию inp.txt):')
if len(fname)==0:
    fname = 'inp.txt'
op = input('Вводите операцию(*/-+^):')  # + по умолчанию
if len(op)==0:
    op='+'

f = open(fullPath + fname,'r')
fPos = open(fullPath + 'outPos.txt','w')
fNeg = open(fullPath + 'outNeg.txt','w')
line = f.readline()
i = 1
while line:
	s = line.split(' ')
	var1 = float(s[0])
	var2 = float(s[1])
	res = doOp(var1, var2, op)
	if float(res) >= 0:
		fPos.write(str(i)+') ' + str(res)+'\n')
	else:
		fNeg.write(str(i)+') ' + str(res)+'\n')
	i+=1
	line = f.readline()

f.close()
fPos.close()
fNeg.close()
