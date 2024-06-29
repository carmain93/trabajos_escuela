import 'package:flutter/material.dart';
import 'home.dart';
import 'dash.dart';
class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: "pantallas",
      //home: Home(),
      initialRoute: "home",//rutas 1.0
      routes: {//se colocan todas las rutas
        "home": (context)=>Home(),
        "dash": (context)=>Dash(),
      },
    );
  }
}
