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
    
    self.conexion = None;
    
  def OpenConnectionDB(self) -> None:  
    try:
      self.conexion = pyodbc.connect(self.strConnection);
      print("Conexión a la Base de Datos Exitosa");
    except Exception as e:
      print("Conexión a la Base de Datos Fallida: "+str(e));
        
  def CloseConnectionDB(self) -> None:  
    try:
      self.conexion.close();
      print("Cierre de la Base de Datos Exitosa");
    except Exception as e:
      print("Cierre de la Base de Datos Fallida: "+str(e));

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
    cursor.execute("COMMIT;");
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
    
  def ConsultarMarcas(self) -> None:  

    #EJECUCIÓN DEL PROCEDURE
    consulta: str = """{CALL proc_select_marcas();}""";
    cursor = self.conexion.cursor();
    cursor.execute(consulta);

    #RECORRIDO DEL RESULTADO PARA TRABAJAR CON OBJETOS
    ls_marcas: list = [];
    for elemento in cursor:
      marca = Marcas.Marcas();
      marca.SetId(elemento[0]);
      marca.SetNombre(elemento[1]);
      
      ls_marcas.append(marca);
    
    #CIERRE DE TRANSACCIÓN
    cursor.execute("COMMIT;");
    cursor.close();
    
    #IMPRESIÓN DE LA CONSULTA CON OBJETOS
    for marca in ls_marcas:
      print(  str(marca.GetId()) + " - " + 
              marca.GetNombre());
      
  def EjecutarSP(self, nombreSp: str, parametros: list)-> None:

    #GENERAMOS LOS MARCADORES PARA LOS ATRIBUTOS DEL SP
    marcadores: list = ','.join(["'%s'" for _ in parametros]);
    
    #CONSTRUCCIÓN DEL QUERY
    consulta = f"CALL {nombreSp}({marcadores}, @p_resultado);";

    try:
      #EJECUCIÓN PROCEDURE
      cursor = self.conexion.cursor();
      cursor.execute(consulta % parametros);
      
      #SELECCIÓN DE RESULTADO
      cursor.execute("SELECT @p_resultado;");
      resultado = cursor.fetchone()[0];
      
    except Exception as Error:
      resultado = str(Error);
    
    print("Resultado:", resultado);

    #CIERRE DE TRANSACCIÓN
    cursor.execute("COMMIT;");
    cursor.close();