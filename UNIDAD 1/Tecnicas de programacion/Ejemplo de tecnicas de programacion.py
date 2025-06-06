from abc import ABC, abstractmethod
# Abstracción: definimos una clase abstracta para un sistema de pagos
class MetodoPago(ABC):
    @abstractmethod
    def pagar(self, monto):
        pass

# Herencia y Polimorfismo: diferentes métodos de pago heredan de MetodoPago
class TarjetaCredito(MetodoPago):
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self._saldo = saldo  # Encapsulación: saldo protegido

    def pagar(self, monto):
        if monto <= self._saldo:
            self._saldo -= monto
            print(f"Pago de ${monto} realizado con tarjeta de {self.titular}. Saldo restante: ${self._saldo}")
        else:
            print(f"No hay suficiente saldo en la tarjeta de {self.titular}.")

class Paypal(MetodoPago):
    def __init__(self, usuario, saldo):
        self.usuario = usuario
        self.__saldo = saldo  # Encapsulación: saldo privado

    def pagar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Pago de ${monto} realizado con Paypal de {self.usuario}. Saldo restante: ${self.__saldo}")
        else:
            print(f"No hay suficiente saldo en la cuenta Paypal de {self.usuario}.")

# Otra clase que utiliza métodos de pago
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pagos = []

    def procesar_pago(self, metodo_pago: MetodoPago, monto):
        print(f"Procesando pago en {self.nombre}...")
        metodo_pago.pagar(monto)
        self.pagos.append((metodo_pago, monto))

# Pruebas completas
tarjeta = TarjetaCredito("1234-5678-9012-3456", "Ana López", 500)
paypal = Paypal("ana@email.com", 200)

tienda = Tienda("Librería Central")
tienda.procesar_pago(tarjeta, 150)    # Pago con tarjeta
tienda.procesar_pago(paypal, 50)      # Pago con Paypal
tienda.procesar_pago(tarjeta, 400)    # Intento de pago excediendo el saldo

# Acceso seguro a atributos encapsulados
# print(paypal.__saldo)  # Esto generaría un error por encapsulación
