# Flask_REST_API_CRUD

https://flask-rest-api-crud-app.herokuapp.com/api/employees

Aplikacja udostępniająca API dla podstawowych metod REST. Umożliwia zarządzanie pracownikami (CRUD) poprzez odpowiednie zapytania. 

## Autoryzacja

Jest to prosta aplikacja i nie jest konieczna autoryzacja, aby korzystać z API

## Dokumentacja API
Pełny adres: 
https://flask-rest-api-crud-app.herokuapp.com
| Adres | Metoda | Opis |
| :--- | :--- | :--- |
| `/api/employees` | `GET` |Zwraca wszystkich pracowników|
| `/api/employees/<employee_id>` | `GET` |Zwraca pracownika o danym id|
| `/api/employees` | `POST` |Tworzy nowego pracownika|
| `/api/employees/<employee_id>` | `PUT` |Nadpisuje pracownika o danym id|
| `/api/employees/<employee_id>` | `DELETE` |Usuwa pracownika o danym id|

## JSON wymagany dla metod POST i PUT:
```javascript
{
    "birth_day "    : timestamp,
    "email"         : varchar(255) not null,
    "name"          : varchar(50) not null,
    "phone_number"  : varchar(255)
}
```
## JSON zwracany w metodach GET:
```javascript
[
    {
        "id"            : integer,
        "birth_day"     : timestamp,
        "email"         : string,
        "name"          : string,
        "phone_number"  : string
    }
]
```
## User stories użyte przy tworzeniu aplikacji
- User can create new employee
- User can read all employees
- User can read employee by employee_id
- User can update employee (by employee id)
  - User will see 400 status code if cannot update employee
- User can delete employee (by id)
  - User will see 400 status code if cannot delete employee

## Statusy aplikacji
| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 201 | `CREATED` |
| 400 | `BAD REQUEST` |
| 404 | `NOT FOUND` |
| 500 | `INTERNAL SERVER ERROR` |

## Użyte technologie
- Flask
- Relacyjna baza danych
- Serwer Heroku
- Serwer Azure (baza danych)

## Diagram architektury całej aplikacji

![Diagram](https://github.com/kozyraP/Flask_REST_API_CRUD/blob/main/Untitled%20Diagram.svg)

