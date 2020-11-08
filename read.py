data = []
count = 0
def open:
	with open('reviews.txt', 'r') as f:
		for line in f:
			data.append(line)
			count += 1
			if count % 100000 == 0:
				print(len(data))


sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('每一筆留言的平均是', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print(len(new)) 

good = []
for d in data:
	if 'good' in d:
		good.append(d)
		

#文字技術
wc ={} #word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 10000:
		print(word, wc[word])

while True:
	want = input('請問你想查什麼字：（離開請打q）')
	if want == "q"
		print('感謝你使用本功能')
		break
	elif want in wc:
		print(want,'出現過',wc[want],'次')want == 'q':
	else:
		print('這個字沒有出現過喔')
		

