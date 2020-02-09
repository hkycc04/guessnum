
import random
start = input('請決定數字開始範圍: ')
end = input('請決定數字結束範圍: ')

r = random.randint(int(start), int(end))
count = 0
while True:
	count += 1 #count = count + 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('您猜中了!')
		print('您猜了第', count, '次')
		break
	elif num > r:
		print('比較大喔')
	elif num < r:
		print('比較小喔')
	print('您猜了第', count, '次')
