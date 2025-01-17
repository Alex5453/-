### Багрепорт 1: Не правильный статус код при создании объявления

**Описание:**
Тест `test_create_item_success` ожидает статус код 201 Created при успешном создании объявления, однако API возвращает статус код 200 OK.

**Шаги для воспроизведения:**
1. Отправьте POST-запрос на `https://qa-internship.avito.com/api/1/item` с корректными данными объявления.

**Ожидаемый результат:**
Статус код ответа должен быть 201 Created.

**Фактический результат:**
Статус код ответа - 200 OK.

**Примечания:**
Проверьте конфигурацию API для правильного кода состояния и настройте тест соответственно.

---

### Багрепорт 2: Ошибка при создании объявления с отсутствующими обязательными полями

**Описание:**
Тест `test_create_item_missing_fields` ожидает статус код 400 Bad Request при попытке создать объявление с отсутствующими обязательными полями. Однако API возвращает статус код 500 Internal Server Error.

**Шаги для воспроизведения:**
1. Отправьте POST-запрос на `https://qa-internship.avito.com/api/1/item` с неполными данными.

**Ожидаемый результат:**
Статус код ответа должен быть 400 Bad Request с соответствующим сообщением об ошибке.

**Фактический результат:**
Статус код ответа - 500 Internal Server Error.

**Примечания:**
Необходимо проверить обработку ошибок в API и корректность сообщения об ошибке.

---

### Багрепорт 3: Неверный формат ответа при получении объявления по идентификатору

**Описание:**
Тест `test_get_item_success` ожидает, что ответ будет в виде одного объекта (dict), однако API возвращает список объектов (list).

**Шаги для воспроизведения:**
1. Отправьте GET-запрос на `https://qa-internship.avito.com/api/1/item/{id}` с существующим идентификатором.

**Ожидаемый результат:**
Ответ должен быть в формате одного объекта (dict).

**Фактический результат:**
Ответ представлен в формате списка объектов (list).

**Примечания:**
Проверьте формат ответа API и корректность тестов в соответствии с этим форматом.

---

### Багрепорт 4: Не совпадающий формат ответа при попытке получения несуществующего объявления

**Описание:**
Тест `test_get_item_not_found` ожидает, что ответ будет содержать поле 'message' с текстом ошибки, однако API возвращает ответ с полем 'result'.

**Шаги для воспроизведения:**
1. Отправьте GET-запрос на `https://qa-internship.avito.com/api/1/item/invalid-id`.

**Ожидаемый результат:**
Ответ должен содержать поле 'message' с текстом ошибки.

**Фактический результат:**
Ответ содержит поле 'result' с описанием ошибки.

**Примечания:**
Проверьте структуру ответа API на ошибки и настройте тесты в соответствии с этим.

---

### Багрепорт 5: Неправильное количество объявлений при получении объявлений продавца

**Описание:**
Тест `test_get_items_by_seller_not_found` ожидает, что список объявлений будет пустым для несуществующего продавца, однако API возвращает 49 объявлений.

**Шаги для воспроизведения:**
1. Отправьте GET-запрос на `https://qa-internship.avito.com/api/1/{sellerID}/item` с несуществующим идентификатором продавца.

**Ожидаемый результат:**
Список объявлений должен быть пустым.

**Фактический результат:**
API возвращает список с 49 объявлениями.

**Примечания:**
Проверьте правильность данных и работу API для несуществующих продавцов.
