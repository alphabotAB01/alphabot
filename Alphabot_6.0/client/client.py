"""********* IMPORTIAMO LE LIBRERIE *********"""
import requests
import pandas as pd
import time
import ast
""" ***************************************** """

"""********* SETTIAMO LE COSTANTI e LE VARIABILI GLOBALI ************"""
OSTACOLO_RILEVATO = 0
INDRIZZO_IP = "http://192.168.0.125:5000"
TEMPO_90_GRADI = 700
TEMPO_MOVIMENTO = 200
PWM_DEFAULT = 5
PWM_CURVA = 30
eInMovimento = True
primavolta = True
""" ***************************************************************** """

"""********* CODICE DI CONTROLLO *********"""
#funzione per andare avanti
requests.post(f"{INDRIZZO_IP}/comando", data={'avanti':'avanti', 'altro_comando':""})
while True:
    #leggiamo se il robot ha rilevato ostacoli
    dict_ostacoli = ast.literal_eval((requests.get(f"{INDRIZZO_IP}/api/v1/sensor/obstacles")).text)

    #Se li ha rilevati entrambi ed è la prima volta si ferma e gira di 90 gradi circa a sinistra
    #mentre se non è la prima volta gira di pochi gradi a destra
    if dict_ostacoli["Left"] == OSTACOLO_RILEVATO and dict_ostacoli["Right"] == OSTACOLO_RILEVATO:
        if eInMovimento:
            requests.post(f"{INDRIZZO_IP}/comando", data={'fermo':'fermo', 'altro_comando':""})
            eInMovimento = False
        if primavolta:        
            requests.get(f"{INDRIZZO_IP}/api/v1/motors/left", params={"pwm":PWM_CURVA, "time":TEMPO_90_GRADI})
            primavolta = False
        requests.get(f"{INDRIZZO_IP}/api/v1/motors/right", params={"pwm":PWM_CURVA, "time":TEMPO_MOVIMENTO})
    
    #Se ha rilevato l'ostacolo di sinistra (si ferma nel caso sia la prima volta) e gira di pochi gradi a destra
    elif dict_ostacoli["Left"] == OSTACOLO_RILEVATO:
        if eInMovimento:
            requests.post(f"{INDRIZZO_IP}/comando", data={'fermo':'fermo', 'altro_comando':""})
            eInMovimento = False
        requests.get(f"{INDRIZZO_IP}/api/v1/motors/right", params={"pwm":PWM_CURVA, "time":TEMPO_MOVIMENTO})
    
    #Se ha rilevato l'ostacolo di destra (si ferma nel caso sia la prima volta) e gira di pochi gradi a sinistra
    elif dict_ostacoli["Right"] == OSTACOLO_RILEVATO:
        if eInMovimento:
            requests.post(f"{INDRIZZO_IP}/comando", data={'fermo':'fermo', 'altro_comando':""})
            eInMovimento = False        
        requests.get(f"{INDRIZZO_IP}/api/v1/motors/left", params={"pwm":PWM_CURVA, "time":TEMPO_MOVIMENTO})

    #Se non ha rilevato ostacoli va avanti
    else:
        if not eInMovimento:
            requests.get("http://192.168.0.125:5000/api/v1/motors/both", params={"pwmL":PWM_DEFAULT, "pwmR":PWM_DEFAULT})
            requests.post(f"{INDRIZZO_IP}/comando", data={'avanti':'avanti', 'altro_comando':""})
            eInMovimento = True
            primavolta = True


""" ***************************************** """
