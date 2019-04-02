# university-communication

### Зависимости
- kafka_2.12-2.2.0
- docker 18.06.3-ce
- docker-compose 1.21.0

### Запуск kafka для разработки
См. пункты Step 1-5 в https://kafka.apache.org/quickstart

### Создание рабочих топиков
Топик для загрузки файлов
```
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic university-download
```

Топик для уведомления об успешной записи
```
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic university-success
```

### Отправка сообщений в топик
```
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic university-download
> {"action": "download", "source": "application1", "url": "https://bit.ly/2F5nCiI"}
```

### Запуск приложения
```
cp src/env-example src/.env
cp devops/env-compose devops/.env
cd devops && docker-compose -p university-communication up
```
