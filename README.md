#TalanaKombatJRPG

## Introducción

TalanaKombatJRPG es un sencillo juego de simulación de lucha basado en texto entre dos jugadores, Tonyn Stallone y Arnaldor Shuatseneguer.

## Levantar el proyecto(pasos)

- Copiar o renombrar el archivo .env.example a .env
- Ejecutar los siguientes comandos:
    - make build
    - make up-d
    - make migrate

## Cómo utilizar el método `kombat`

Para simular una batalla entre dos jugadores, puedes utilizar el método "kombat" proporcionado en el script. Así es como puedes usarlo:

### Llamando el método

El método `kombat` toma un diccionario como entrada, que representa el estado inicial de los jugadores. La estructura del diccionario debe ser la siguiente:

```python
from core.utils import kombat

datos = {
     'player1': {
         'movimientos': ['DSDP', 'SDK', 'P', 'K', 'W', 'S', 'A', 'D'],
         'golpes': ['P', 'K', 'W', 'S']
     },
     'player2': {
         'movimientos': ['SAK', 'ASAP', 'P', 'K', 'W', 'S', 'A', 'D'],
         'golpes': ['P', 'K', 'W', 'S']
     }
}

kombat_result = kombat(datos)
```

### LLamando al command Kombat

```
docker compose exec web python manage.py kombat --kombat_json='{"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},"player2":{"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}}'
```

### Utilizando la endpoint

```
curl --location 'http://0.0.0.0:8000/api/v1/core/kombat' \
--header 'Content-Type: application/json' \
--data '{
    "player1": {
        "movimientos": [
            "D",
            "DSD",
            "S",
            "DSD",
            "SD"
        ],
        "golpes": [
            "K",
            "P",
            "",
            "K",
            "P"
        ]
    },
    "player2": {
        "movimientos": [
            "SA",
            "SA",
            "SA",
            "ASA",
            "SA"
        ],
        "golpes": [
            "K",
            "",
            "K",
            "P",
            "P"
        ]
    }
}'
```

Hecho con ❤️ por [AleHdzDev](https://alehdzdev.github.io/) 🧑‍💻
