class Marcas:
    id: int;

    def GetId(self) -> int: 
        return self.id;
    def SetId(self, valor: int) -> None: 
        self.id = valor;

    nombre: str;

    def GetNombre(self) -> str: 
        return self.nombre;
    def SetNombre(self, valor: str) -> None: 
        self.nombre = valor;