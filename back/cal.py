import time
import math


def calcular(masa, fuerza, ue, ud, inclinacion):

    if masa == '' or fuerza == '':
        return "error se necesita mas datos pruebe a llenar los campos masa y fuerza como minimo"

    masa = float(masa)
    fuerza = float(fuerza)

    print(
        "masa:", masa,
        "\nfuerza:", fuerza,
        "\nue:", ue,
        "\nud", ud,
        "\ninclinacion", inclinacion)

    g = 9.8
    fx = fuerza
    pesoy = masa*g

    if inclinacion != '':
        inclinacion = float(inclinacion)

        if inclinacion > 90 or inclinacion < 0:
            return "La inclinacion tiene que estar entre 0 y 90 grados"

        fx = fx + masa * g * math.sin(inclinacion*math.pi/180)

        pesoy = masa * g * math.cos(inclinacion*math.pi/180)
    print("se llego hasta linea 33")

    if ud != '' and ue != '':

        ud = float(ud)
        ue = float(ue)

        ffe = ue*pesoy
        ffd = ud*pesoy
        fuerzaNeta = fx-ffd

        if ffe > abs(fx):
            return (f"Fuerza Aplicada: {fuerza} Newton\nFuerza de Friccion Estatica:{ffe} Newton\nEste objeto no se mueve porque la friccion entre los cuerpos es muy grande")
        else:
            a = fuerzaNeta/masa

    else:
        a = fx/masa
        if a == 0:
            return "Este objeto no se mueve"

    return f"El objeto tiene una aceleracion de {a} m/s^2 (Valor positivo: movimiento -> Valor negativo: <-)"
