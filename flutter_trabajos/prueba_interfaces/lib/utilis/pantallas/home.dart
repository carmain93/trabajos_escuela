import 'package:flutter/material.dart';
String? usr;
class Home extends StatelessWidget {
  const Home({super.key});

  @override
  Widget build(BuildContext context) {

    return Scaffold(appBar: AppBar(
      title: Text("Inicio pruebas"),
      actions: <Widget>[
        IconButton(onPressed: (){Navigator.pushNamed(context, "Login");}, icon: Icon(Icons.co_present)),
        IconButton(onPressed: (){Navigator.pushNamed(context, "Nosotros");}, icon: Icon(Icons.code_sharp))
      ],
    ),

    );
  }
}
