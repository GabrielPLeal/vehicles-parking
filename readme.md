
# Vehicles Parking

Api to handle the flow of cars and customers leaving and entering the parking lot

# Clone Project

```bash
  git clone git@github.com:GabrielPLeal/vehicles-parking.git
```

## Preparing Environment

```bash
  pip python3.10 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  python3 -m manage.py makemigrations
  python3 -m manage.py migrate
```

## Run Project

```bash
  python3 -m manage.py runsever
```

# Api Documentation

[customer-api](customer/readme.md)

[vehicle-api](vehicle/readme.md)

[park-movement-api](park_movement/readme.md)

```
