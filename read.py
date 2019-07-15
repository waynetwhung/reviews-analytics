data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print('檔案讀取完成，總共有 ', len(data), '筆資料。')

sum_len = 0
for d in data:
	sum_len += len(d)
print('每筆留言的平均長度為 ', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有 ', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有 ', len(good), '筆留言內容含有good')
print(good[0])

print(data[0])

# 文字計數
wc = {} # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增新的key進wc字典

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))

while True:
	word = input('請問您想查詢什麼字： ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為： ', wc[word])
	else:
		print('查無此字！')

print('感謝使用本查詢功能')