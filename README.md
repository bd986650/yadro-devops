# yadro-devops

Тестовое задание 

---

## Структура проекта

```
yadro-devops/
├── first-part/
│   ├── app.py
│   └── requirements.txt
│
├── second-part/
│   └── Dockerfile
│
├── third-part/
│   ├── playbook.yml
│   ├── inventory.ini
│   └── ansible.cfg
│
└── README.md
```

---

## Part 1 — Python script

### Описание

Скрипт выполняет HTTP-запросы к сервису:

https://tools-httpstatus.pickup-services.com/

Обрабатывает HTTP status codes:

- 1xx / 2xx / 3xx → логирует статус и тело ответа
- 4xx / 5xx → выбрасывает exception

### Запуск

```bash
cd first-part

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python app.py
```

### Зависимости

- requests

---

## Part 2 — Docker

### Описание

Docker-образ на базе `ubuntu:22.04`, который:

- устанавливает Python3 и pip
- копирует скрипт
- ставит зависимости
- запускает скрипт при старте контейнера

### Сборка

```bash
docker build -f second-part/Dockerfile -t http-status-checker .
```

### Запуск

```bash
docker run --name http-checker http-status-checker
```

### Логи

```bash
docker logs http-checker
```

---

## Part 3 — Ansible

### Описание

Ansible playbook автоматизирует:

- установку Docker (Linux)
- запуск Docker service
- сборку Docker image
- запуск контейнера
- получение логов
- проверку exit code

### Запуск

```bash
cd third-part
ansible-playbook playbook.yml
```