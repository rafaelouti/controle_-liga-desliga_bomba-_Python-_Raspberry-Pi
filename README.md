# Controle de Liga/Desliga de Bomba com Raspberry Pi e Python

Este projeto utiliza um Raspberry Pi para controlar o liga/desliga de uma bomba de água com base no nível de água detectado por um sensor. O código é escrito em Python e utiliza a biblioteca RPi.GPIO para interagir com os pinos GPIO do Raspberry Pi.

## Componentes Necessários

- Raspberry Pi (qualquer modelo com GPIO)
- Sensor de nível de água
- Relé para controlar a bomba
- Bomba de água
- Jumpers e fios de conexão
- Fonte de alimentação para a bomba

## Configuração do Hardware

1. **Conecte o Sensor de Nível de Água**:
   - Pino de sinal do sensor -> Pino GPIO 17 do Raspberry Pi
   - Pino de alimentação (VCC) do sensor -> Pino de 3.3V do Raspberry Pi
   - Pino de terra (GND) do sensor -> Pino GND do Raspberry Pi

2. **Conecte o Relé**:
   - Pino de controle do relé -> Pino GPIO 27 do Raspberry Pi
   - Pino de alimentação (VCC) do relé -> Pino de 5V do Raspberry Pi
   - Pino de terra (GND) do relé -> Pino GND do Raspberry Pi
   - Conecte a bomba de água ao relé conforme as instruções do fabricante

## Instalação do Software

1. **Instale a Biblioteca GPIO**:
   ```bash
   sudo apt-get update
   sudo apt-get install python3-rpi.gpio


clone 
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio


