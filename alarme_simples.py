from datetime import datetime
from sys import path
from time import sleep
from playsound import playsound 
import os.path

def validaHorario(alarm_time):
    if (len(alarm_time) > 7):
        return ('Formato incorreto!')
        input()
    else:
        if(int(alarm_time[0:2]) > 24):
            return "HORA inválida!"
            input()
        elif(int(alarm_time[3:5]) > 59):
            return "MINUTO inválido!"
            input()
        else:
            return 'Ok'


alarm_time = input("Digite o horário em 'HH:MM': ")
validate = validaHorario(alarm_time)

if(validate != 'Ok'):
    print(validate)
else:
    print(f'Alarme configurado para {alarm_time}!')
    
    while True:
        sleep(5)
        # alarme cortado
        hora = alarm_time[0:2]
        min = alarm_time[3:5]
        
        # hora atual
        now = datetime.now()

        # hora atual cortada
        hora_ = now.strftime('%I')
        min_ = now.strftime('%M')
            
        if hora_ == hora:
            if min_ == min:
                while True:
                    print('Acorda, campeão!')
                    playsound('i\'m waking up.mp3')
                    
                    
                    