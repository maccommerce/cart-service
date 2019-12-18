def test_view_cart(client):
    
    with client.test_client() as c:
        response = c.get('/cart/view')
        assert response.status_code != 404


def test_modify_cart_item(client):
    
    with client.test_client() as c:
        response = c.post('/cart/update')
        assert response.status_code != 404


def test_remove_cart_item(client):
    
    with client.test_client() as c:
        response = c.post('/cart/remove')
        assert response.status_code != 404


def test_clear_cart(client):
    
    with client.test_client() as c:
        response = c.post('/cart/clear')
        assert response.status_code != 404


def test_add_cart_single(client):
    
    with client.test_client() as c:
        response = c.post('/cart/add')
        assert response.status_code != 404


def test_add_cart_many(client):
    
    with client.test_client() as c:
        response = c.post('/cart/add-pack')
        assert response.status_code != 404
