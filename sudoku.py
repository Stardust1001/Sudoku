import random
import time
 
 
class Sudoku:
	'''
	数独生成器类， 调用Sudoku实例的 make_digits() 方法，尝试生成数独
	但，数独生成是随机的，那么，可能会成功，也许会失败
	因此，make_digits() 方法的返回值代表生成数独是否成功
	如果 make_digits() 返回 True，那么可以使用实例的 digits 属性，里面有生成的新数独
	'''
	def __init__(self):
		'''
		digits 属性里面保存着当前的数独矩阵
		'''
		self.digits = [[] for i in range(9)]
 
	def make_digits(self):
		'''
		尝试生成数独，返回值代表生成是否成功
		'''
		#  数独矩阵的列数组，即9个竖行
		col_lists = [[] for i in range(9)]
		#  数独矩阵的区域数组，即九宫格的几个区域
		area_lists = [[] for i in range(3)]
		#  1 - 9 的随机排列
		nine = self.random_nine()
		for i in range(9):
			col_lists[i].append(nine[i])
		area_lists[0] = nine[0:3]
		area_lists[1] = nine[3:6]
		area_lists[2] = nine[6:]
 
		for i in range(8):
			nine = self.random_nine()
			#  九宫格的当前格已变换，重置当前格的数字
			if i % 3 == 2:
				area_lists[0] = []
				area_lists[1] = []
				area_lists[2] = []
			for j in range(9):
				area_index = j // 3
				count = 0
				error = False
				while nine[0] in col_lists[j] or nine[0] in area_lists[area_index]:
					count += 1
					if count >= len(nine):
						error = True
						break
					nine.append(nine.pop(0))
				if error:
					return False
				first = nine.pop(0)
				col_lists[j].append(first)
				area_lists[area_index].append(first)
		self.digits = col_lists
		return True
 
	def random_nine(self):
		'''
		1 - 9 的随机排列
		'''
		nine = [i + 1 for i in range(9)]
		for i in range(5):
			nine.append(nine.pop(random.randint(0, 8)))
		return nine
 
 
if __name__ == '__main__':
	#  实例化数独生成器
	sudoku = Sudoku()
	#  开始生成时间
	start = time.time()
	#  不断尝试生成数独，直到生成成功
	while not sudoku.make_digits():
		pass
	#  结束时间
	end = time.time()
	print('Milliseconds:\t{0}'.format((end - start) * 1000))
	for row in sudoku.digits:
		print(row)
