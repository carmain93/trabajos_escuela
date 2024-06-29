import 'package:flutter/material.dart';
List<List> Im=[


];
class Nosotros extends StatelessWidget {
  const Nosotros({super.key});
final nos="Nosotros nos especialisamos en vidersas herramientas de desarrollo como parte de nuestra formacions\n"+
    "por ende nos complace informar que estos osn nuestros primeros pasos en flutter";
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Sobre nosotros"),
        elevation: 3,
      ),
      body: Center(
        child: Column(
          children: [
            Icon(Icons.savings_sharp),
            Text("somos unos desarrolladores primerisos enfocados en el desarrollo mobil y web que siguen"
                " buscando nuevas herrramientas para poder mejorar\n A su ves nos interesa optener nueva sideas para"
                "desarrollar, que nos permitan mejorar de forma constante"),

          ],
        ),
      )

    );
  }
}
