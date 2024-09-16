import pyodbc;
import datetime;
from Clases import Personas
from Clases import Estados

class Conexion:
    strConnection: str = """
        Driver={MySQL ODBC 9.0 Unicode Driver};
        Server=localhost;
        Database=db_personas;
        PORT=3306;
        user=user_ptyhon;
        password=Clas3s1Nt2024_!""";

    def ConnectionBasica(self) -> None:  
        conexion = pyodbc.connect(self.strConnection);
        
        consulta: str = """SELECT * FROM personas""";
        cursor = conexion.cursor();
        cursor.execute(consulta);

        for elemento in cursor:
            print(elemento);
            
        cursor.close();
        conexion.close();

    def ConnectionBasica1(self) -> None:  
        conexion = pyodbc.connect(self.strConnection);
        
        consulta: str = """SELECT * FROM estados""";
        cursor = conexion.cursor();
        cursor.execute(consulta);

        lista: list = [];
        for elemento in cursor:
          entidad = Estados.Estados();
          entidad.SetId(elemento[0]);
          entidad.SetNombre(elemento[1]);
          lista.append(entidad);
            
        cursor.close();
        conexion.close();

        for estado in lista:
            print(str(estado.GetId()) + " - " + estado.GetNombre());

    def ConnectionBasica2(self) -> None:  
        conexion = pyodbc.connect(self.strConnection);
        
        consulta: str = """
          SELECT p.id, 
                p.cedula, 
                p.nombre, 
                p.estado, 
                p.fecha, 
                p.activo, 
                e.id, 
                e.nombre
          FROM estados e
            INNER JOIN personas p ON e.id = p.estado""";
        cursor = conexion.cursor();
        cursor.execute(consulta);

        lista: list = [];
        for elemento in cursor:
          entidad = Personas.Personas();
          entidad.SetId(elemento[0]);
          entidad.SetCedula(elemento[1]);
          entidad.SetNombre(elemento[2]);
          entidad.SetEstado(elemento[3]);
          entidad.SetFecha(elemento[4]);
          entidad.SetActivo(elemento[5]);

          estado = Estados.Estados();
          estado.SetId(elemento[6]);
          estado.SetNombre(elemento[7]);
          entidad.Set_Estado(estado);
          
          lista.append(entidad);
            
        cursor.close();
        conexion.close();

        for entidad in lista:
            print(str(entidad.GetId()) + " - " + 
              entidad.GetCedula() + " - " + 
              entidad.GetNombre() + " - " + 
              entidad.Get_Estado().GetNombre() + " - " + 
              str(entidad.GetEstado()) + " - " + 
              str(entidad.GetFecha()) + " - " + 
              str(entidad.GetActivo()));

    def NonQueryBasico(self) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();

        cedula: str = "7532564";
        nombre: str = "Test Python";
        estado: int = 3;
        fecha: datetime = datetime.datetime.now();
        activo: bool = True;

        print(fecha.strftime("%Y-%m-%d %H:%M:%S"));

        consulta: str = "INSERT INTO `personas` (`cedula`, `nombre`, `estado`, `fecha`, `activo`) ";
        consulta += "VALUES ('" + cedula + "', '" + nombre + "', " + str(estado) + ",";
        consulta += "'" + fecha.strftime("%Y-%m-%d %H:%M:%S") + "', " + str(activo) + ")";

        cursor.execute(consulta);
        cursor.execute("SELECT LAST_INSERT_ID()");
        cursor.commit();       
                
        print("Response Inserted Objects: " + str(cursor.fetchone()[0]));
        cursor.close();
        conexion.close();