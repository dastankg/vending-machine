# Симулятор Торгового Автомата

Django-проект, который симулирует работу торгового автомата с API интерфейсом. Позволяет пользователям просматривать
доступные товары, совершать покупки и получать сдачу.

## 🛠️ Настройка и установка

### Требования

- Docker

### Настройка переменных окружения

Создайте файл `.env` на основе `env_example` со следующими параметрами:

```
# Django настройки
SECRET_KEY=         # Django Secret key
DEBUG=              # True для режима разработки, False для production

# Настройки базы данных PostgreSQL
DB_ENGINE=          # Database engine (или storage engine )
DB_NAME=            # Имя базы данных
DB_USER=            # Имя пользователя PostgreSQL
DB_PASSWORD=        # Пароль пользователя PostgreSQL
DB_HOST=            # Хост для локальной разработки
DB_DOCKER_HOST=     # Хост для Docker контейнеров
DB_PORT=            # Порт PostgreSQL
```

### Использование Docker

Клонировать репозиторий:

```
git clone <url-репозитория>
cd vending-machine
```

Создать файл окружения:

```
touch .env
```

Собрать и запустить Docker-контейнеры:

```
docker-compose up -d
```

Это запустит Django-приложение и PostgreSQL базу данных в отдельных контейнерах.

Документация API
OpenAPI (Swagger) по API доступен по адресу: http://0.0.0.0:8000/docs
## 🔌 API Endpoints

### Получение списка всех товаров

```
GET /api/products/
```

Ответ:

```json
[
  {
    "id": "a8098c1a-f86e-11da-bd1a-00112444be1e",
    "name": "Кока-Кола",
    "price": 150.00,
    "count": 10
  },
  {
    "id": "b3498d2b-f86e-11da-bd1a-00112444be1e",
    "name": "Чипсы",
    "price": 120.00,
    "count": 15
  },
  {
    "id": "c5672e3c-f86e-11da-bd1a-00112444be1e",
    "name": "Шоколадка",
    "price": 80.00,
    "count": 20
  }
]
```

### Покупка товара

```
POST /api/products/purchase/
```

Тело запроса:

```json
{
  "product_id": "a8098c1a-f86e-11da-bd1a-00112444be1e",
  "quantity": 1,
  "money": 200.00
}
```

Успешный ответ (200 OK):

```json
{
  "message": "Purchase successful",
  "products": {
    "name": "Кока-Кола",
    "price": 150.00,
    "remaining_count": 9
  },
  "quantity": 1,
  "remaining_money": 50.00
}
```

Ответы с ошибками:

- Товар не найден (400 Bad Request):

```json
{
  "product_id": [
    "Указанный продукт не существуют."
  ]
}
```

- Недостаточно средств (400 Bad Request):

```json
{
  "money": [
    "Недостаточно средств. Общая стоимость составляет 1999.98"
  ]
}
```

- Товар закончился (400 Bad Request):

```json
{
  "quantity": [
    "Недостаточно товара на складе."
  ]
}
```
