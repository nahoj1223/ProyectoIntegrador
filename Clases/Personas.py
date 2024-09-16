import datetime; 
from Clases import Estados

class Personas:
    id: int = 0;
    
    def GetId(self) -> int:
        return self.id;
    def SetId(self, value: int) -> None:
        self.id = value;
        
    cedula: str = None;

    def GetCedula(self) -> str:
        return self.cedula;
    def SetCedula(self, value: str) -> None:
        self.cedula = value;
        
    nombre: str = None;

    def GetNombre(self) -> str:
        return self.nombre;
    def SetNombre(self, value: str) -> None:
        self.nombre = value;
        
    estado: int = None;
    
    def GetEstado(self) -> int:
        return self.estado;
    def SetEstado(self, value: int) -> None:
        self.estado = value;
        
    fecha: datetime = None;
    
    def GetFecha(self) -> datetime:
        return self.fecha;
    def SetFecha(self, value: datetime) -> None:
        self.fecha = value;
        
    activo: bool = None;
    
    def GetActivo(self) -> int:
        return self.activo;
    def SetActivo(self, value: int) -> None:
        self.activo = value;
        
    _estado: Estados = None;
    
    def Get_Estado(self) -> Estados:
        return self._estado;
    def Set_Estado(self, value: Estados) -> None:
        self._estado = value;