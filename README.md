# grupo2_DAIC_2020
## Table of contents
* [Project name](#Project_name)
* [Description](#Description)
* [Installation](#Installation)
* [Usage](#Usage)
* [Contributing](#Contributing)
## Project name
SISTEMA INTELIGENTE DE MONITOREO Y CONTEO DE PERSONAS
	
## Description
Se ha diseñado un sistema que simula el monitoreo de aforo de un local cuya entrada y salida de personas se produce desde una única entrada.

La detección de acceso de una persona se realiza mediante un sensor ultrasonidos HC04. La detección de salida de una persona se realiza mediante la simulación de una pulsación de un boton fisico.

El bloqueo o apertura de la cerradura se simula mediante un servo controlodo electronicamente.

La cerradura de la puerta se bloquea cuando se llega al límite máximo de ocupación y no permite su apertura hasta que el numero de personas sea inferior al limite preestablecido.

Un sensor de CO2 permite calcular la calidad de aire del local.

El aforo es ajustable dependiendo de las restricciones impuestas y se configura automáticamente teniendo en cuenta el número máximo de personas permitidas en el local con el aforo al 100%. De esta manera, este sistema se puede usar en distintas circunstancias.

Esta información la podrá ver también el usuario mediante notificaciones ya que esta se guarda en una base de datos. 

Se envía la información del aforo calculado a una base de datos para que la gente tenga en cuenta como está la situación antes de ir.

Por seguridad se dispone de un sistema que habilita la apertura de la cerradura en caso de una emergencia
	
## Installation

Lista de Pines utilizados:

Pines Digitales:

	GPIO_5  -> Sensor Ultrasonidos HC04

	GPIO_16 -> Pulsador de Emergencia

	GPIO_17 -> Servo Motor 

	GPIO_18 -> Boton Simulador Salida 
	
Pines Analógicos:

	A0 -> Sensor CO2
## Usage
## Contributing:
