### 1 - Insert a new park movement

#### 1.1 - Description:

```text
Insert a new park movement and return park movement id.
```
#### 1.2 - Method and Url:

```http
  POST  /api/v1/movement
```

#### 1.3 - Fields:

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `plate` | `string` | Plate of the vehicler. |
| `vehicle_id` | `uuid4` | Id from vehicle. |

#### 1.4 - Json example:

```json
{
    "customer_id": "valid_uuid4",
    "plate": "Gabriel",
    "kind": 1
}
```

### 2 - Update vehicle

#### 2.1 - Description:

```text
Update others park movement fields
```
#### 2.2 - Method and Url:

```http
  PUT  /api/v1/movement
```

#### 2.3 - Fields:

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `uuid4` | Id from park movement. |
| `validate_date` | `date` | Validade date. |
| `value` | `decimal` | Pricing for the parking. |

##### 2.4 - Json example:

```json
{
    "id": "valid_uuid"
    "validate_date": "2022-06-15",
    "value": 10.00
}
```