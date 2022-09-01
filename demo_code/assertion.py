def check_http_response(transaction, response):
    response_body = response.text
    response_code = response.status_code
    if transaction == 'login':
        if 'Token' not in response_body:
            response.failure(f'Тело ответа логина  {response_body} статус код {response_code}')

    if transaction == 'add_to_cart':
        if 'добавлен в корзину' not in response_body:
            response.failure(f'Тело ответа  добавления в корзину  {response_body} статус код {response_code}')
