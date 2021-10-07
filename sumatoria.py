def sumatoria_cubica(n):
	res = 0
	for i in range(1,n+1):
		for j in range(1,i+1):
			for k in range(j,i+j+1):
				res+=1
	return res			

def sumatoria_constante(n):
    res = 0
    res = (n*(n+1)*(n+2))/3
    return res

