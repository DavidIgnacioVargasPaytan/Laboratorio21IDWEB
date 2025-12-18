import json
equipos_futbol = [
    {
        "Nombre": "Real Madrid",
        "país": "Espana",
        "nivelAtaque": 95,
        "nivelDefensa": 90
    },
    {
        "Nombre": "Liverpool",
        "país": "Inglaterra",
        "nivelAtaque": 92,
        "nivelDefensa": 88
    },
    {
        "Nombre": "Barcelona",
        "país": "Espana",
        "nivelAtaque": 96,
        "nivelDefensa": 92
    }
]

cadena_json = json.dumps(equipos_futbol, indent=4)

print("Lista de Equipos convertida a Cadena JSON")
print(cadena_json)

archivo_json = "equipos.json"
with open(archivo_json, "w") as f:
    json.dump(equipos_futbol, f, indent=4) 

print(f"\nLa lista también se guardó en '{archivo_json}' con formato.")
