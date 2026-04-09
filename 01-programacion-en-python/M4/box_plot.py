import matplotlib.pyplot as plt

temperaturas_medias_mensuales: dict[str, dict[str, float]] = {
    "barranquilla": {
        "ene": 27.7,
        "feb": 28.0,
        "mar": 28.5,
        "abr": 29.0,
        "may": 29.4,
        "jun": 29.3,
        "jul": 29.3,
        "ago": 29.2,
        "sep": 28.9,
        "oct": 28.4,
        "nov": 28.5,
        "dic": 28.0,
    },
    "bogota": {
        "ene": 13.2,
        "feb": 13.6,
        "mar": 13.8,
        "abr": 14.1,
        "may": 14.1,
        "jun": 14.0,
        "jul": 13.4,
        "ago": 13.5,
        "sep": 13.5,
        "oct": 13.5,
        "nov": 13.5,
        "dic": 13.3,
    },
    "cali": {
        "ene": 26.3,
        "feb": 26.6,
        "mar": 26.7,
        "abr": 26.6,
        "may": 26.5,
        "jun": 26.3,
        "jul": 26.2,
        "ago": 26.0,
        "sep": 26.0,
        "oct": 25.8,
        "nov": 26.0,
        "dic": 26.1,
    },
    "cartagena": {
        "ene": 26.6,
        "feb": 26.7,
        "mar": 27.1,
        "abr": 27.6,
        "may": 28.1,
        "jun": 28.4,
        "jul": 28.1,
        "ago": 28.2,
        "sep": 28.1,
        "oct": 27.9,
        "nov": 27.8,
        "dic": 26.9,
    },
    "medellin": {
        "ene": 22.7,
        "feb": 23.2,
        "mar": 22.8,
        "abr": 22.7,
        "may": 22.8,
        "jun": 23.5,
        "jul": 23.7,
        "ago": 23.6,
        "sep": 22.9,
        "oct": 22.0,
        "nov": 21.8,
        "dic": 22.2,
    },
    "pereira": {
        "ene": 21.5,
        "feb": 21.7,
        "mar": 21.8,
        "abr": 21.6,
        "may": 21.3,
        "jun": 21.5,
        "jul": 21.4,
        "ago": 21.6,
        "sep": 21.1,
        "oct": 20.6,
        "nov": 20.7,
        "dic": 21.3,
    },
}

fig, ax = plt.subplots(figsize=(12, 5))

datos = [list(meses.values()) for meses in temperaturas_medias_mensuales.values()]
etiquetas = [ciudad.capitalize() for ciudad in temperaturas_medias_mensuales]

ax.boxplot(datos, labels=etiquetas)
ax.set_ylabel("Temperatura media mensual (°C)")
ax.set_xlabel("Distribución de temperaturas mensuales por ciudad")

plt.tight_layout()
plt.show()
