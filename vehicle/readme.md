### 1 - Insert a new vehicle

#### 1.1 - Description:

```text
Insert a new vehicle and return vehicle id.
```
#### 1.2 - Method and Url:

```http
  POST  /api/v1/vehicle/
```

#### 1.3 - Fields:

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `customer_id` | `uuid4` | Id from customer. |
| `plate` | `string` | Plate of the vehicle. |
| `kind` | `number` | Type of the vehicle. (1=moto, 2=carro) |

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
Update the vehicle and return id.
```
#### 2.2 - Method and Url:

```http
  PUT  /api/v1/vehicle/
```

#### 2.3 - Fields:

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `id` | `uuid4` | Id from vehicle. |
| `customer_id` | `uuid4` | Id from customer. |
| `plate` | `string` | Plate of the vehicle. |
| `kind` | `number` | Type of the vehicle. (1=moto, 2=carro) |

##### 2.4 - Json example:

```json
{
    "id": "valid_uuid"
    "customer_id": "valid_uuid4",
    "plate": "Gabriel",
    "kind": 1
}
```