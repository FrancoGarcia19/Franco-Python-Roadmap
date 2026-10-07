# Repaso de lo visto ayer
nombre_usuario1 = input("¿Cúal es tu nombre? ")
study_hours_yesterday = float(input("¿Cuántas horas estudiaste ayer? "))
study_hours_today = float(input("¿Cuántas horas estudiarás hoy? "))

study_hours_total= study_hours_yesterday + study_hours_today

print ("Hola", nombre_usuario1)
print("Entre ayer y hoy estudiarás", study_hours_total, "horas.")


#Tema nuevo: Comparaciones
edad = 23

print(edad > 18)
print(edad < 18)
print(edad == 23)
print(edad != 23)
print(edad >= 23)

#If & Else

hours = 15

if study_hours_total >= 10:
    print("Excelente ritmo de estudio")
elif study_hours_total >= 5:
    print("Buen ritmo de estudio")
else:
    print("Puedes estudiar un poco más")