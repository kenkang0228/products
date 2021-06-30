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

#練習寫入並存檔
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價錢 \n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')