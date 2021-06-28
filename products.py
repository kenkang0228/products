#練習二維清單

products = []
while True:
	name = input('輸入商品名稱: ')
	if name == 'q': #quit
		break
	price = input('輸入價錢: ')
	products.append([name, price]) #建立小清單加入大清單
print(products)

for p in products:
	print(p[0], '的價錢是', p[1])

with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
