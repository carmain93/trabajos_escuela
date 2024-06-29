import 'package:ya/config/config.dart';

class Datebox extends StatefulWidget {
  const Datebox({super.key});

  @override
  State<Datebox> createState() => _DateboxState();
}

class _DateboxState extends State<Datebox> {
  @override
  Widget build(BuildContext context) {
    return Card(
      shape: RoundedRectangleBorder(
        side: BorderSide(color: Colors.black, width: 1.0),
        borderRadius: BorderRadius.circular(5.0),
      ),
      child: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Column(

          children: [

            Row( children: [Text("Modelo"), SizedBox(width: 50,),Text("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")],),
            SizedBox(height: 20,),
            Row(children: [Text("Fabricante"),SizedBox(width: 50,),Text("xxxxxxxxxxxxxxxxxxxxxxxxxxxx")],),
            SizedBox(height: 20,),
            Row(children: [Text("Año"),SizedBox(width: 50,),Text("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")],),
            SizedBox(height: 20,),
            Row(children: [Text("VIM"),SizedBox(width: 50,),Text("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")],),

          ],
        ),
      ),
    );
  }
}
