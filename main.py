import data
import configuration
import stand_request

#Заголовки для создания заказа
def get_order_headers():
    order_headers = data.headers.copy()
    return order_headers

#Получение "тела" заказа
def get_order_body():
    order_body = data.oder_body.copy()
    return order_body

#Создание заказа
def create_order():
    # response = stand_request.post_new(get_order_body(), get_order_headers(), configuration.CREATE_ORDER)
    response = stand_request.post_new(current_body, get_order_headers(), configuration.CREATE_ORDER)
    return response

#Получение трек-номера заказа (парсим ответ на запрос на создание заказа)
def get_order_id():
    return create_order().json()['track']

#Добавление GET-параметра для отправки запроса на получение инфы по указанному параметру (треку заказа)
def create_order_info_url(track):
    end_path = configuration.GET_ORDER_INFO + '?t=' + track
    return end_path

#По треку заказа можно получить данные о заказе проверки (успешное получение информации о заказе)
def possitive_assert():
    response = stand_request.get_new(get_order_headers(), create_order_info_url(str(current_order_track)))
    # response = stand_request.get_new(get_order_headers(), create_order_info_url(str(get_order_id())))
    assert response.status_code == 200
    assert str(response.json()["order"]["track"]) == str(current_order_track)
    #проверки на соотвествие параметров запроса и ответа
    assert response.json()["order"]["firstName"] == current_body["firstName"]
    assert response.json()["order"]["lastName"] == current_body["lastName"]
    assert response.json()["order"]["address"] == current_body["address"]
    assert response.json()["order"]["metroStation"] == current_body["metroStation"]
    assert response.json()["order"]["phone"] == current_body["phone"]
    assert response.json()["order"]["rentTime"] == current_body["rentTime"]
    assert response.json()["order"]["comment"] == current_body["comment"]
    assert response.json()["order"]["color"] == current_body["color"]
    #assert response.json()["order"]["deliveryDate"] == current_body["deliveryDate"] -
    #данная проверка заблокирована, так как в требованиях нет точного указания на то,
    #какой формат должен быть у данного поля

#Неуспешная попытка получения данных о заказе (не передан трек-номер)
def negative_assert_empty_order_track(order_track):
    response = stand_request.get_new(get_order_headers(), create_order_info_url(order_track))
    assert response.status_code == 400
    assert response.json()['message'] == 'Недостаточно данных для поиска'

#Неуспешная попытка получения данных о заказе (передан несуществующий трек-номер)
def negative_assert_nonexistent_order_track(order_track):
    response = stand_request.get_new(get_order_headers(), create_order_info_url(order_track))
    assert response.status_code == 404
    assert response.json()['message'] == 'Заказ не найден'


current_body = get_order_body() #информация о заказе, который будет создан
current_order_track = get_order_id() #трек-номер заказа

