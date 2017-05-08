from aliexpress_api_client import AliExpress

aliexpress = AliExpress('17802', '888')

# Получение списка продуктов:

    #products = aliexpress.get_product_list(['productId', 'productTitle', 'salePrice'])

    #for product in products:
    #    print('#%s %s: %s' % (product['productId'], product['productTitle'], product['salePrice']))


# Получение деталей продукта:

    #product = aliexpress.get_product_details(['productId', 'productTitle', 'salePrice'], product_id)

    #print('#%s %s: %s' % (product['productId'], product['productTitle'], product['salePrice']))


# Получение партнерской ссылки на товар:
urls = ['http://ru.aliexpress.com/']

links = aliexpress.get_promotion_links(['url', 'promotionUrl'], urls)

for link in links['promotionUrls']:
   print(link['url'], link['promotionUrl'])


