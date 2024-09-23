import datetime
from Clases import Database

print("\n------------CONEXION BASE DE DATOS------------\n")

#OBJETO DE LA CLASE DATABSE
objDatabase: Database = Database.Database();

#APERTURA DE CONEXIÓN A LA BASE DE DATOS
objDatabase.OpenConnectionDB();

proceso: str = "x";

if(proceso == "marca"):
    print("\n------------PROCESO INSERTAR MARCA------------\n")
    
    #PARAMETROS PARA INSERTAR UNA MARCA
    nombre_m: str = "Marca_Prueba4";

    parametros: list = (nombre_m,);

    #LLAMADO DE LA FUNCION PARA INSERTAR UNA MARCA
    objDatabase.EjecutarSP("proc_insertar_marca", parametros);
    
    print("\n------------PROCESO CONSULTAR MARCAS------------\n")
    
    objDatabase.ConsultarMarcas();
else:
    print("\n------------PROCESO INSERTAR ZAPATO------------\n")
    #PARAMETROS PARA INSERTAR UN NUEVO ZAPATO
    modelo: str = "Prueba";
    talla: str = 35;
    fecha_fabricacion: str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S");
    disponibilidad: str = 'false';
    id_marca: str = 4;

    parametros: list = (modelo, talla, fecha_fabricacion, disponibilidad, id_marca)
    
    #LLAMADO DE LA FUNCION PARA INSERTAR UN ZAPATO
    objDatabase.EjecutarSP("proc_insertar_zapato", parametros);
    
    print("\n------------PROCESO CONSULTAR ZAPATOS------------\n")
        
    #LLAMADO DE LA FUNCION CONSULTAR ZAPATO
    objDatabase.ConsultarZapatos();

print("\n------------CIERRE BASE DE DATOS------------\n")

#CIERRE DE CONEXIÓN A LA BASE DE DATOS
objDatabase.CloseConnectionDB();