import pyodbc;
import datetime;
from Clases import Zapatos
from Clases import Marcas

class Database:
  
  def __init__(self):
    self.strConnection: str = """
        Driver={MySQL ODBC 9.0 Unicode Driver};
        Server=localhost;
        Database=db_zapatos;
        PORT=3306;
        user=user_ptyhon;
        password=Clas3s1Nt2024_!""";
    
    self.conexion = None
    
  def OpenConnectionDB(self) -> None:  
    try:
      self.conexion = pyodbc.connect(self.strConnection);
      print("Conexión a la Base de Datos Exitosa")
    except Exception as e:
      print("Conexión a la Base de Datos Fallida: "+str(e))
        
  def CloseConnectionDB(self) -> None:  
    try:
      self.conexion.close();
      print("Cierre de la Base de Datos Exitosa")
    except Exception as e:
      print("Cierre de la Base de Datos Fallida: "+str(e))

  def ConsultarZapatos(self) -> None:  

    #EJECUCIÓN DEL PROCEDURE
    consulta: str = """{CALL proc_select_zapatos();}""";
    cursor = self.conexion.cursor();
    cursor.execute(consulta);

    #RECORRIDO DEL RESULTADO PARA TRABAJAR CON OBJETOS
    ls_zapatos: list = [];
    for elemento in cursor:
      zapato = Zapatos.Zapatos();
      zapato.SetId(elemento[0]);
      zapato.SetModelo(elemento[1]);
      zapato.SetTalla(elemento[2]);
      zapato.SetFecha_fabricacion(elemento[3]);
      zapato.SetDisponibilidad(elemento[4]);
      zapato.SetIdMarca(elemento[5]);

      marca = Marcas.Marcas();
      marca.SetId(elemento[5]);
      marca.SetNombre(elemento[6]);
      zapato.SetMarca(marca);
          
      ls_zapatos.append(zapato);
    
    #CIERRE DE TRANSACCIÓN
    cursor.execute("COMMIT;")
    cursor.close();
    
    #IMPRESIÓN DE LA CONSULTA CON OBJETOS
    for zapato in ls_zapatos:
      print(  str(zapato.GetId()) + " - " + 
              zapato.GetModelo() + " - " + 
              str(zapato.GetTalla()) + " - " + 
              str(zapato.GetFecha_fabricacion()) + " - " + 
              str(zapato.GetDisponibilidad()) + " - " + 
              str(zapato.GetIdMarca()) + " - " + 
              zapato.GetMarca().GetNombre());
      
  def InsertarZapato(self):

    #PARAMETROS DEL INSERT
    modelo = "Prueba"
    talla = 35
    fecha_fabricacion = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    disponibilidad = 1
    id_marca = 5
    
    #CONSTRUCCIÓN DEL QUERY
    consulta: str = "{"+"CALL proc_insertar_zapato('{}',{},'{}',{},{},@p_resultado);".format(modelo,
                                                                                        str(talla),
                                                                                        fecha_fabricacion,
                                                                                        str(disponibilidad),
                                                                                        str(id_marca))+"}"
    #EJECUCIÓN PROCEDURE
    cursor = self.conexion.cursor();
    cursor.execute(consulta)
    
    #SELECCIÓN DE RESULTADO
    cursor.execute("SELECT @p_resultado;")
    resultado = cursor.fetchone()[0]

    print("Resultado:", resultado)

    #CIERRE DE TRANSACCIÓN
    cursor.execute("COMMIT;")
    cursor.close()