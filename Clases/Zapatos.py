import datetime; 
from Clases import Marcas

class Zapatos:
    id: int = 0;
    
    def GetId(self) -> int:
        return self.id;
    def SetId(self, value: int) -> None:
        self.id = value;
        
    modelo: str = None;

    def GetModelo(self) -> str:
        return self.modelo;
    def SetModelo(self, value: str) -> None:
        self.modelo = value;
        
    talla: int = None;
    
    def GetTalla(self) -> int:
        return self.talla;
    def SetTalla(self, value: int) -> None:
        self.talla = value;
        
    fecha_fabricacion: datetime = None;
    
    def GetFecha_fabricacion(self) -> datetime:
        return self.fecha_fabricacion;
    def SetFecha_fabricacion(self, value: datetime) -> None:
        self.fecha_fabricacion = value;
        
    disponibilidad: bool = None;
    
    def GetDisponibilidad(self) -> int:
        return self.disponibilidad;
    def SetDisponibilidad(self, value: int) -> None:
        self.disponibilidad = value;
        
    id_marca: int = None;
    
    def GetIdMarca(self) -> int:
        return self.id_marca;
    def SetIdMarca(self, value: int) -> None:
        self.id_marca = value;
        
    marca: Marcas = None;
    
    def GetMarca(self) -> Marcas:
        return self._estado;
    def SetMarca(self, value: Marcas) -> None:
        self._estado = value;