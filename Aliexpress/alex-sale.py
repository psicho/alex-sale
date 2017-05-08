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

links = AliExpress.get_promotion_links(['url', 'promotionUrl'], urls)

promotionUrls = 'http://ru.aliexpress.com/'

for link in links['promotionUrls']:
    print('%s: %s' % (link['url'], link['promotionUrl']))


