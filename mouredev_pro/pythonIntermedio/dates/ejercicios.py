from datetime import datetime, date, time, timedelta

# 1. Crea una variable con la fecha y hora actual.
fecha_hora_actual = datetime.now()
print("1. Fecha y hora actual:", fecha_hora_actual)

# 2. Imprime solo el año, mes y día de la fecha actual.
fecha_actual = fecha_hora_actual.date()
print("2. Año, mes y día actual:", fecha_actual.year, fecha_actual.month, fecha_actual.day)

# 3. Crea una fecha específica: 25 de diciembre de 2025 y muéstrala.
fecha_navidad = date(2025, 12, 25)
print("3. Fecha específica (Navidad 2025):", fecha_navidad)

# 4. Muestra solo la hora, los minutos y los segundos de un objeto time.
hora_actual = fecha_hora_actual.time()
print("4. Hora, minutos y segundos actuales:", hora_actual.hour, hora_actual.minute, hora_actual.second)

# 5. Calcula cuántos días faltan para el 1 de enero del año siguiente.
hoy = date.today()
proximo_ano = hoy.year + 1
primero_enero = date(proximo_ano, 1, 1)
dias_restantes = (primero_enero - hoy).days
print("5. Días hasta 1 de enero del próximo año:", dias_restantes)

# 6. Crea una función que reciba una fecha y devuelva su timestamp.
def fecha_a_timestamp(fecha):
    return datetime.timestamp(datetime.combine(fecha, time()))
    
print("6. Timestamp de hoy:", fecha_a_timestamp(hoy))

# 7. Suma 30 días a la fecha actual usando timedelta.
fecha_mas_30 = hoy + timedelta(days=30)
print("7. Fecha actual + 30 días:", fecha_mas_30)

# 8. Crea una fecha y añade 1 mes (simplificado como 30 días).
fecha_inicial = date(2025, 3, 15)
fecha_mas_1_mes = fecha_inicial + timedelta(days=30)
print("8. Fecha inicial + 1 mes (30 días):", fecha_mas_1_mes)

# 9. Compara dos fechas y muestra cuál es anterior.
fecha1 = date(2025, 5, 10)
fecha2 = date(2025, 6, 15)
if fecha1 < fecha2:
    print(f"9. {fecha1} es anterior a {fecha2}")
else:
    print(f"9. {fecha2} es anterior a {fecha1}")

# 10. Crea una lista con varias fechas y ordénalas cronológicamente.
fechas = [
    date(2025, 7, 20),
    date(2025, 3, 15),
    date(2025, 1, 1),
    date(2025, 12, 31),
    date(2025, 6, 10)
]
fechas_ordenadas = sorted(fechas)
print("10. Fechas ordenadas:")
for fecha in fechas_ordenadas:
    print(fecha)