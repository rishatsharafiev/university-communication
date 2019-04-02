# university-communication

## Порядок запуска сервисов
1. Запустить zookeeper и kafka
2. Создать топики в kafka
3. Запустить сервис university-communication
4. Запустить сервис university-files (см. https://github.com/rishatsharafiev/university-files)
5. Отправить сообщение в топик для скачивания файла (university-download)
6. Ожидать события готовности загрузки в другом топике (university-success)


### Зависимости
- kafka_2.12-2.2.0
- docker 18.06.3-ce
- docker-compose 1.21.0

### (1) Запуск kafka для разработки
См. пункты Step 1-5 в https://kafka.apache.org/quickstart

### (2) Создание рабочих топиков
Топик для загрузки файлов
```
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic university-download
```

Топик для уведомления об успешной записи
```
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic university-success
```


### (3) Запуск приложения
```
cp src/env-example src/.env
cp devops/env-compose devops/.env
cd devops && docker-compose -p university-communication up
```

### (5) Отправка сообщений в топик для скачивания файла
```
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic university-download
> {"action": "download", "source": "application1", "url": "https://bit.ly/2F5nCiI"}
```

### (6) Ожидать события готовности загрузки
```
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic university-success --from-beginning
```
