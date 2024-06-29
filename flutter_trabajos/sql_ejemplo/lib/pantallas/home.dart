import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import '../db/database.dart';
import '../planetas/planetas.dart';
class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  List<Planetas>? planetario;
  @override
  void initState() {

    super.initState();
    abrirDB();
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Builder(
        builder: (context){
          query();

          if (planetario==null){
            return CircularProgressIndicator(color: Colors.blueGrey,);
          }else{
            return ListView.builder(
                itemCount: planetario!.length,
                itemBuilder: (context, index){
                  return Card(
                    child: ListTile(
                      leading: Icon(Icons.blur_circular_rounded),
                      title: Text("nombre ${planetario![index].nombre}"),
                      subtitle: Text("radio ${planetario![index].radio}"),

                    ),
                  );
                }

            );
          }
          return Container();
        },
      ),
    );
  }

  void abrirDB() {
    DB.db().whenComplete( () async {
      await agregar();
    },
    );
  }

  Future<void> agregar() async {
    List<Planetas> planet = [
      Planetas(1, "mercurio", 3134, 342.6),
      Planetas(2, "venus", 4134, 442.6),
      Planetas(3, "tierra", 13134, 1342.6),
      Planetas(4, "marte", 23134, 2342.6),
    ];
    int a = 0;
    
    await DB.insertar(planet);

  }
  Future<void> query() async{
    planetario = await DB.consulta().whenComplete((){
      setState(() {

      });
    });
  }
}

