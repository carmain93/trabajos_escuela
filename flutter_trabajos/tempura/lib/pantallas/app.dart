import 'package:flutter/material.dart';
import 'package:tempura/pantallas/home.dart';

class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.deepPurple,
        primaryColor: Colors.blueGrey,
        useMaterial3: true
      ),
      home: Home(),
    );
  }
}
