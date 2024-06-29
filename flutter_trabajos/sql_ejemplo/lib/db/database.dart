import 'package:sqflite/sqflite.dart' as sqlite;
import 'package:path/path.dart';
import 'package:sql_ejemplo/planetas/planetas.dart';

class DB{
  //conexion base de datos y creacion de tablas
  //corrutinas
  static Future<sqlite.Database> db() async{
    String ruta = await sqlite.getDatabasesPath();
    return sqlite.openDatabase(join(ruta,"solarsystem.db"),version: 1,singleInstance:  true,onCreate: (db,version)async{
      await create(db);
    });
}

  static Future<void> create(sqlite.Database db) async {//el future  es una forma de mandarlo a un ilo distinto

    const String sql= """
    CREATE TABLE planeta (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre TEXT NOT NULL,
    radio REAL NOT NULL,
    distancia REAL NOT NULL,
    createAt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
    """;
    await db.execute(sql);
  }
  static Future<List<Planetas>> consulta()async{
    //abrir la base de datos
    final sqlite.Database db= await DB.db();
    List<Planetas>planetario=[];
    final List<Map<String, dynamic>> m= await db.query("planeta");//extraen los datos de la tabla guardados en una lista de un mapa
    //como un jodido json
    planetario = m.map(
      (e) {
        return Planetas.deMapa(e);
      },
    ).toList();
    //db.close();
    return planetario;
  }

  static Future<int> insertar (List<Planetas> planetario) async{
    final sqlite.Database db= await DB.db();
    int value=0;
    for(Planetas planeta in planetario){
      value = await db.insert("planeta", planeta.mapeador(), conflictAlgorithm: sqlite.ConflictAlgorithm.replace);

    }
    db.close();

    return value;
  }

  static Future<void> borrar (int id) async{
    final sqlite.Database db= await DB.db();
    await db.delete("planeta", where: "id = ?", whereArgs: [id]);

    //db.close();

  }
}
