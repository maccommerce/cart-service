# def test_cart_view(client):
    
#     with client.test_client() as c:
#         response = c.get('/cart')
#         assert response.status_code != 404


# def test_cart_modify_item(client):
    
#     with client.test_client() as c:
#         response = c.put('/cart_item')
#         assert response.status_code != 404


# def test_cart_remove_item(client):
    
#     with client.test_client() as c:
#         response = c.delete('/cart_item')
#         assert response.status_code != 404


# def test_clear_cart(client):
    
#     with client.test_client() as c:
#         response = c.delete('/cart')
#         assert response.status_code != 404


# def test_cart_add_single(client):
    
#     with client.test_client() as c:
#         response = c.post('/cart_item')
#         assert response.status_code != 404


# def test_cart_add_many(client):
    
#     with client.test_client() as c:
#         response = c.post('/cart')
#         assert response.status_code != 404
