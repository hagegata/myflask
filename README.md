# MyFlask

Flask-приложение со счётчиком посещений, развёрнутое в Docker и управляемое через Docker Compose.

## Стек

- Python 3.11 (Flask)
- Redis
- Docker (multi-stage)
- Docker Compose
- GitHub Actions (CI/CD)
- Trivy

## Запуск

```bash
docker-compose up -d --build
curl http://localhost:5000
```

## Путь изучения

- **19.08** – Первый Dockerfile, сборка и запуск простого Python-приложения.
- **20.08** – Flask в Docker; переменные окружения.
- **24.08** – Healthcheck, ограничения памяти и CPU, тома.
- **24.08** – Docker Compose: один сервис, затем Flask + Redis.
- **26.08** – Многостадийная сборка Dockerfile.
- **25.08** – Git: инициализация, первый коммит, SSH, пуш на GitHub.
- **25.08** – Первый workflow GitHub Actions (сборка).
- **27.08** – CI/CD: Compose-тест, пуш в GHCR, сканирование Trivy.
- **26.08** – Kubernetes: манифесты Deployment, Service, ConfigMap, Secret.

## Технические трудности

### 1. Проброс портов через `-p` на ALT Linux
Контейнеры с пробросом портов не отвечали с хоста, хотя внутри сервис работал.  
**Решение:** использовать `--network host`. Для CI (Ubuntu) проблема неактуальна.

### 2. Недоступность внешних ресурсов из-за TLS
Не скачивались файлы с `raw.githubusercontent.com` и образы с `ghcr.io`.  
**Решение:** зеркала (jsDelivr), Docker Hub, отключение проверки TLS.

### 3. Сетевой плагин Kubernetes (CNI)
Поды не запускались: `stat /var/lib/calico/nodename: no such file or directory`.  
**Статус:** сеть в кластере не настроена, объекты создаются, но поды в `ContainerCreating`.
