from aliexpress_api_client import AliExpress

aliexpress = AliExpress('17802', '888')

# Получение списка продуктов:
keywords = 'sony'
products = aliexpress.get_product_list(['productId', 'productTitle', 'salePrice'], keywords)
products = products['products']
for product in products:
   pass
   #print('Product Id: ', product['productId'], 'Sale Price', product['salePrice'], 'Product Title: ', product['productTitle'])

    #products = aliexpress.get_product_list(['productId', 'productTitle', 'salePrice'])

    #for product in products:
    #    print('#%s %s: %s' % (product['productId'], product['productTitle'], product['salePrice']))


# Получение деталей продукта:
product_id = '32682005396'
product = aliexpress.get_product_details(['productId', 'productTitle', 'originalPrice', 'salePrice', 'volume', 'imageUrl'], product_id)
#print(product['productId'], product['productTitle'], product['originalPrice'], product['salePrice'], 'volume = ', product['volume'], product['imageUrl'])
print('-------')

    #product = aliexpress.get_product_details(['productId', 'productTitle', 'salePrice'], product_id)

    #print('#%s %s: %s' % (product['productId'], product['productTitle'], product['salePrice']))


# Получение партнерской ссылки на товар:
urls = ['https://ru.aliexpress.com/item/Apple-iPad-mini-4-Wi-Fi-cellular-16GB/32807670869.html']

links = aliexpress.get_promotion_links(['url', 'promotionUrl'], urls)

for link in links['promotionUrls']:
   #print(link['url'], link['promotionUrl'])
   print(link['promotionUrl'])



