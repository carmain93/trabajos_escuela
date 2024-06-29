import 'package:flutter/material.dart';
import 'home.dart';
import 'Login.dart';
import 'Nosotros.dart';
class App extends StatefulWidget {
  const App({super.key});

  @override
  State<App> createState() => _AppState();
}

class _AppState extends State<App> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        debugShowCheckedModeBanner: false,
      title: "pruebas",
      initialRoute: "home",
      routes: {
          "home": (context)=>Home(),
          "Login": (context)=>Login(),
          "Nosotros": (context)=>Nosotros(),
      },
    );
  }
}
