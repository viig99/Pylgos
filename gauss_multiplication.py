import math as ma
def gauss(x,y,b):
	lx,ly = (int(ma.log10(x))+1)/2 , (int(ma.log10(y))+1)/2
	m = lx if lx > ly else ly
	if max(x,y) < b**m or max(x,y) < 1000:
		return x*y
	bm = b**m
	b2m = b**(2*m)
	x1 = x / bm
	x0 = x % bm
	y1 = y / bm
	y0 = y % bm
	z2 = gauss(x1,y1,b)
	z0 = gauss(x0,y0,b)
	z1 = gauss(x1+x0,y1+y0,b)-z2-z0
	return (z2*b2m) + (z1*bm) + z0
	
if __name__ == "__main__":
	print(gauss(1234223123,1234,100))