def triangle_area(a, b, c):
	p = (a + b + c) / 2
	print((p * (p - a) * (p - b ) * (p - c)) ** 0.5)


triangle_area(float(input()), float(input()), float(input()))
