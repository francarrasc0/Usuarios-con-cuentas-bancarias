class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre =  nombre
        self.apellido = apellido
        self.cuenta = CuentaBancaria(tasa_interes = 0.02, balance = 0)
    
    def hacer_deposito (self, amount):
        self.cuenta.deposito(amount)
    
    def hacer_retiro (self, amount):
        self.cuenta.retiro(amount)
    
    def mostrar_balance_usuario (self):
        print (f'{self.nombre} {self.apellido}, Balance: {self.cuenta.balance}')
    
    def transferir_dinero(self, otro_usuario, amount):
        if self.cuenta.balance >= amount:
            self.cuenta.retiro(amount)
            otro_usuario.cuenta.deposito(amount)
            print(f'{self.nombre} ha transferido {amount} a {otro_usuario.nombre}')
        else:
            print('Saldo insuficiente para realizar la transferencia.')

class CuentaBancaria:

    cuentas = []

    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes 
        self.balance = balance
        CuentaBancaria.cuentas.append(self)

    def deposito(self, amount):
        self.balance += amount
        return self
        
    def retiro(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        return self

    def mostrar_info_cuenta(self):
        print(f'Balance: ${self.balance}')
        return self
        
    def generar_interes(self):
        if self.balance > 0:
            interes_generado = self.balance * self.tasa_interes
            self.balance += interes_generado
        return self

    @classmethod
    def mostrar_todas_las_cuentas(cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info_cuenta()
