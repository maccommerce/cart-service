def test_existing_get_cart(client):
    print(client.get('/cart'))