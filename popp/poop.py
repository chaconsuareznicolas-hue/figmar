class CuentaBancaria:
     # Método constructor (__init__): Inicializa el estado del objeto al ser creado #  self representa la instancia actual de una clase. 
     def __init__(self, titular: str, saldo_inicial: float): 
     # # Atributos del objeto 
        self.titular = titular 
        self.saldo = saldo_inicial 

cuenta1 = CuentaBancaria("Carlos Pérez", 150000.0) 
cuenta2 = CuentaBancaria("María Gómez", 500000.0) 

print(f"Cuenta 1 - Titular: {cuenta1.titular}, Saldo: ${cuenta1.saldo}") 
print(f"Cuenta 2 - Titular: {cuenta2.titular}, Saldo: ${cuenta2.saldo}")

class CuentaBancaria: 
    def __init__(self, titular: str, saldo_inicial: float): 
       self.titular = titular 
       self.saldo = saldo_inicial 

def depositar(self, monto: float): 
    if monto > 0: 
        self.saldo += monto 
        print(f"Depósito exitoso de ${monto}. Nuevo saldo: ${self.saldo}") 
    else: 
        print("El monto a depositar debe ser mayor a cero.") 

def retirar(self, monto: float) -> bool: 
    if 0 < monto <= self.saldo: 
        self.saldo -= monto 
        print(f"Retiro exitoso de ${monto}. Saldo restante: ${self.saldo}") 
        return True 
    else: 
        print("Fondos insuficientes o monto inválido.") 
        return False    

mi_cuenta = CuentaBancaria("Ana Torres", 200000.0)

mi_cuenta.depositar(50000.0)  # Saldo sube a 250000 
mi_cuenta.retirar(100000.0)   # Saldo baja a 150000 
mi_cuenta.retirar(300000.0)   # Intento con saldo insuficiente 

class CuentaBancaria: 
    def __init__(self, titular: str, saldo_inicial: float): 
        self.titular = titular 
        self.__saldo = saldo_inicial if saldo_inicial >= 0 else 0.0

    def get_saldo(self) -> float: return self.__saldo 

    def set_saldo(self, nuevo_saldo: float): 
        if nuevo_saldo >= 0: 
            self.__saldo = nuevo_saldo 
        else: print("Error: El saldo no puede ser negativo.") 
        def depositar(self, monto: float): 
            if monto > 0: 
                self.__saldo += monto 

cuenta = CuentaBancaria("Juan", 100.0)

print(f"Saldo actual: ${cuenta.get_saldo()}")

cuenta.set_saldo(-50.0)  # Muestra mensaje de error 
cuenta.set_saldo(200.0)  #  Modificación válida 
print(f"Saldo actualizado: ${cuenta.get_saldo()}")

class CuentaBancaria: 
    def __init__(self, titular: str, saldo: float): 
        self.titular = titular 
        self._saldo = saldo  # Usamos protegido (_) para permitir acceso en las clases hijas 
        def obtener_saldo(self): 
            return self._saldo

class CuentaAhorros(CuentaBancaria): 
    def __init__(self, titular: str, saldo: float, tasa_interes: float):
        super().__init__(titular, saldo) 
        self.tasa_interes = tasa_interes 
    def aplicar_interes(self): 
        interes = self._saldo * self.tasa_interes 
        self._saldo += interes 
        print(f"Interés aplicado: ${interes}. Nuevo saldo: ${self._saldo}")

class CuentaCorriente(CuentaBancaria): 
    def __init__(self, titular: str, saldo: float, limite_sobregiro: float): 
        super().__init__(titular, saldo) 
        self.limite_sobregiro = limite_sobregiro 
    def retirar(self, monto: float):

        if monto <= (self._saldo + self.limite_sobregiro): 
            self._saldo -= monto 
            print(f"Retiro exitoso de ${monto}. Saldo restante: ${self._saldo}") 
        else: 
            print("Retiro excede el límite de sobregiro permitido.")

ahorros = CuentaAhorros("Laura", 1000000.0, 0.02)  # 2% interés 
ahorros.aplicar_interes() 
corriente = CuentaCorriente("Pedro", 200000.0, 500000.0) 
corriente.retirar(400000.0)  # Retira usando sobregiro 

class CuentaBancaria: 
    def __init__(self, titular: str, saldo: float): 
        self.titular = titular 
        self.saldo = saldo 

    def generar_extracto(self): 
        return f"Extracto General - Titular: {self.titular} | Saldo: ${self.saldo}" 
    
class CuentaAhorros(CuentaBancaria): 
    def generar_extracto(self): # Sobrescritura de método 
        return f"[CUENTA DE AHORROS] Titular: {self.titular} | Saldo Disponible: ${self.saldo}" 
    class CuentaCorriente(CuentaBancaria): 
        def __init__(self, titular: str, saldo: float, sobregiro: float): 
            super().__init__(titular, saldo) 
            self.sobregiro = sobregiro 
        def generar_extracto(self): # Sobrescritura de método 
            return f"[CUENTA CORRIENTE] Titular: {self.titular} | Saldo: ${self.saldo} | Cupo Sobregiro: ${self.sobregiro}"

cuentas = [ 
    CuentaAhorros("Andrés", 300000.0), 
    CuentaCorriente("Beatriz", 150000.0, 200000.0), 
    CuentaAhorros("Camilo", 800000.0) ]

print("--- EXTRACTOS BANCARIOS ---") 
for c in cuentas:
    print(c.generar_extracto())                