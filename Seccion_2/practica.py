#La practica es esta: tú trabajas en una empresa donde los vendedores reciben comisiones
#del 13% por sus ventas totales, y tu jefe quiere que ayudes a los vendedores a calcular sus
#comisiones creando un programa que les pregunte su nombre y cuánto han vendido en este
#mes. Tu programa le va a responder con una frase que incluya su nombre y el monto que le
#corresponde por las comisiones. 

nombre = input('Dime tu nombre : ');
saldo = int(input('Dime tu salrio :'));
comision = round(saldo*13/100.2);

print(f'Hola {nombre} tu comisión este mes es {comision}€');