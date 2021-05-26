data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 1000 == 0:
			print(len(data))
print('資料讀取完了，總共有', len(data), '筆資料')

sum_led = 0
for d in data:
	sum_led = sum_led + len(d)
print('資料平均長度為', sum_led/len(data))