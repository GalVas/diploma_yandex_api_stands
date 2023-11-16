from main import possitive_assert, negative_assert_empty_order_track, negative_assert_nonexistent_order_track

# 1-й тест: Получение информации о существующем заказе
def test_get_order_info_by_track():
    possitive_assert()

# 2-й тест: Получение информации при запросе без номера заказа
def test_get_order_info_empty_track_get_unsuccessful_response():
    negative_assert_empty_order_track('')

# 3-й тест: Запрос с несуществуюшим номером заказа
def test_get_order_info_nonexistent_track_get_unsuccessful_response():
    negative_assert_nonexistent_order_track('000000')