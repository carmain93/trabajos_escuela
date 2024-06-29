import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  const Home({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(
      title: Text("Home"),
      actions: <Widget>[
        IconButton(onPressed: (){
          Navigator.pushNamed(context, "dash");// forma de mover la pantalla
        }, icon: Icon(Icons.account_tree_outlined))
      ],
    ),
    );
  }
}
