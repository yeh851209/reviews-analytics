data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('每一筆留言的平均是', sum_len / len(data))

