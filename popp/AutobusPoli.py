class Transformer:
    def transformarse(self) -> str:
        return "El Transformer adopta su forma genérica."

class AutobotCoche(Transformer):
    def transformarse(self) -> str: 
        return "¡Se convierte en un deportivo a 300 km/h!"

class AutobotAvion(Transformer):
    def transformarse(self) -> str
        return "¡Despliega las alas y vuela a velocidad supersónica!"

class AutobotDinosaurio(Transformer):
    def transformarse(self) -> str: 
        return "¡Se transforma en un T-Rex robótico!"


transformers = [
    AutobotCoche(),
    AutobotAvion(),
    AutobotDinosaurio()
]

print("--- EJÉRCITO DE TRANSFORMERS ---")

for t in transformers:
    print(t.transformarse())
