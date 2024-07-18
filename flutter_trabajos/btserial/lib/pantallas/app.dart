import 'package:flutter/material.dart';

import 'home.dart';
class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner:  false,
      theme:  ThemeData(
          useMaterial3: true,
          primaryColor: Colors.purple,
          primarySwatch: Colors.deepPurple),
      home: Home(),
    );
  }
}
