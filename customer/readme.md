### 1 - Insert a new customer

##### 1.1 - Description:

```text
Insert a new customer and return customer id.
```
##### 1.2 - Method and Url:

```http
  POST  /api/v1/customer/
```

##### 1.3 - Fields:

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `name` | `string` | Name of the customer |

##### 1.4 - Json example:

```json
{
    "name": "Gabriel"
}
```

### 2 - Update customer

##### 2.1 - Description:

```text
Update the customer and return customer id.
```
##### 2.2 - Method and Url:

```http
  PUT  /api/v1/customer/
```

##### 2.3 - Fields:

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `name` | `string` | Name of the customer. |

##### 2.4 - Json example:

```json
{
    "id": "valid_uuid4",
    "name": "Gabriel"
}
```