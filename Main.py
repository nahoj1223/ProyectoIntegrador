import datetime
from Clases import Database
from Clases import Marcas
from Clases import Zapatos

objDatabase: Database = Database.Database();

objDatabase.OpenConnectionDB();
#objDatabase.InsertarZapato();
objDatabase.ConsultarZapatos();
objDatabase.CloseConnectionDB();