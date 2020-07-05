def pao(f):
	def wrapper(recheio):
		print("(pao)")
		f(recheio)
		print("(pao)")
	return wrapper



@pao
def lanche(recheio):
	print("hamburguer")
	

lanche("adad")