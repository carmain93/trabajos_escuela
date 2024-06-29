import 'package:flutter/material.dart';

class Index extends StatefulWidget {
  const Index({super.key});
//clase donde se detecta los clis o interacciones
  @override
  State<Index> createState() => _IndexState();
}

class _IndexState extends State<Index> {
  int c=0;
  final TextStyle font30=TextStyle(fontSize:30);
  @override
  //clase donde se pintanto dotos los clis
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        elevation: 3,
        title: Text("Index"),
      ),
      body: Center(
        child: Text("Contador: $c", style: font30),
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.centerDocked,
      floatingActionButton: FloatingActionButton(
        onPressed: (){//cuando se presiona el boton
          debugPrint("clikeado: $c",);
          setState(() {//repinta le widget que se esta presionando
            c++;
          });
        },
        child: Icon(Icons.add),
      ),
    );
  }
}
