import numpy as np
import random
import matplotlib.pyplot as plt
from sympy.polys.polyfuncs import interpolate
from sympy.abc import x

class classname:
	def __init__(self, a = list, b = list):
		self.a = a
		self.b = b

	
	def first_plot(self):
		a = list(set(np.array([random.random() for i in range(100000)])))
        	#print(a)
        	b = list(set(np.array([random.random() for i in range(100000)])))
        	#print(b)
		try:
			test_dict = dict(zip(a,b))
		except e as Exception:
			test_dict = ""
		finally:
			
			len_list = [x for x in range(len(a))]
			#print(len_list)
			ploat = plt.plot(len_list, a, 'r--', len_list, b, 'b--')
			s = plt.show()
		return s
	
	
	def interpolate(self):
		n = self.first_plot()
		if isinstance(self, list):
			func = interpolate(a, b)
		
		
		
	
	def apply_funct(self):
		a = list(set(np.array([random.random() for i in range(100000)])))
		f =  self.interpolate()
		c = [f for f in a]
		return c
		

	def second_plot(self):
		array = self.apply_funct()
		len_list = [x for x in range(len(array))]
		ploat_c = plt.plot(len_list, array, 'g--')
		c = plt.show()
		return c

if __name__ == "_main_":
	class_ex = classname()
	print(class_ex.first_plot())
	print(class_ex.interpolate())
	print(class_ex.apply_funct())
	print(class_ex.second_plot())
