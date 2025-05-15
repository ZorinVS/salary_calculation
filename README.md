# Salary calculation

Написан [скрипт](main.py), который читает данные сотрудников из [файлов в формате csv](data) и формирует простой [отчет по заработной плате](reports/payout_2025-05-14_22-35-59.json).

### Пример запуска

Скрипт можно запускать из терминала, передав один или несколько CSV-файлов и указав тип отчета с помощью аргумента `--report`.
На данный момент поддерживается только отчет `payout`.

###### Пример команды:

```sh
python3 main.py data1.csv data2.csv data3.csv --report payout
```

[пример вывода в консоли](screenshots/demo.png)

### Структура проекта

```text
project-root/
│
├── main.py                          # Точка входа
├── requirements.txt                 # Зависимости проекта
│
├── screenshots/                     # Пример запуска скрипта
├── data/                            # CSV-файлы с входными данными
├── reports/                         # Сгенерированные отчеты
├── src/
│   ├── __init__.py
│   ├── employees/                   # Работа с данными сотрудников
│   │   ├── __init__.py
│   │   ├── csv_parser.py
│   │   ├── employee.py
│   ├── output/                      # Форматы вывода
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── json_output.py
│   │   ├── utils.py
│   └── reports/                     # Логика формирования отчетов
│       ├── __init__.py
│       ├── base.py
│       ├── payout.py
│       └── utils.py
│
└── tests/                           # Тесты (на pytest)
```

### Возможность расширения отчетов

Для расширения необходимо:

- Создать новый файл в [src/reports/](src/reports), например `average_rate.py`
- Унаследовать класс от `Report`
- Зарегистрировать новый тип отчета в [src/reports/__init__.py](src/reports/__init__.py)
- Добавьnm новую команду в CLI

### Тестирование

- Покрытие: >80% основных модулей
- Библиотеки: pytest, pytest-cov 

###### Примеры запуска:
```sh
pytest --cov=src tests/
```
```sh
pytest --cov=src --cov-report=html
```

###### Code Coverage Report

| File                              | Statements | Missing | Excluded | Coverage |
|-----------------------------------|------------|---------|----------|----------|
| src/employees/csv_parser.py       | 36         | 1       | 0        | 97%      |
| src/output/utils.py               | 19         | 7       | 0        | 63%      |
| src/reports/base.py               | 18         | 2       | 0        | 89%      |
| src/reports/payout.py             | 16         | 0       | 0        | 100%     |
| src/employees/employee.py         | 11         | 0       | 0        | 100%     |
| src/output/base.py                | 8          | 1       | 0        | 88%      |
| src/output/json_output.py         | 8          | 0       | 0        | 100%     |
| src/reports/utils.py              | 5          | 0       | 0        | 100%     |
| src/output/__init__.py            | 2          | 0       | 0        | 100%     |
| src/reports/__init__.py           | 2          | 0       | 0        | 100%     |
| src/__init__.py                   | 0          | 0       | 0        | 100%     |
| src/employees/__init__.py         | 0          | 0       | 0        | 100%     |
| **Total**                         | **125**    | **11**  | **0**    | **91%**  |

