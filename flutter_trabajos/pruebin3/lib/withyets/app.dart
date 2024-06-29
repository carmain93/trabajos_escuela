import 'package:flutter/material.dart';
import 'package:pruebin3/withyets/logi/login.dart';
class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'flutter Demo',
      debugShowCheckedModeBanner: false,
      theme:  ThemeData(
        primaryColor: Colors.blue,
      ),
      home: Login(),
    );
  }
}
