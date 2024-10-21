import RPi.GPIO as GPIO
import time

# Configuração do modo de numeração dos pinos
GPIO.setmode(GPIO.BCM)

# Definindo o pino GPIO para o relé
RELE_PIN = 18  # Escolha um pino GPIO que esteja livre

# Configura o pino como saída
GPIO.setup(RELE_PIN, GPIO.OUT)

def ligar_bomba():
    GPIO.output(RELE_PIN, GPIO.HIGH)  # Liga o relé (e a bomba)
    print("Bomba Ligada")

def desligar_bomba():
    GPIO.output(RELE_PIN, GPIO.LOW)  # Desliga o relé (e a bomba)
    print("Bomba Desligada")

try:
    while True:
        comando = input("Digite 'on' para ligar e 'off' para desligar a bomba: ").strip().lower()
        
        if comando == 'on':
            ligar_bomba()
        elif comando == 'off':
            desligar_bomba()
        else:
            print("Comando inválido. Digite 'on' ou 'off'.")
            
        time.sleep(1)

except KeyboardInterrupt:
    print("Programa interrompido pelo usuário.")

finally:
    GPIO.cleanup()  # Limpa os pinos GPIO configurados
