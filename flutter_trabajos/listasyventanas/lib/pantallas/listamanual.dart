import 'config.dart';
class Listamanual extends StatelessWidget {
  const Listamanual({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("lista manual"),
      ),
      body: ListView(
          prototypeItem: ListTile(
            title: Text("megaman"),
            subtitle: Text("Lanza guisantes"),
            trailing: IconButton(
              onPressed: (){},
              icon: Icon(Icons.navigate_next)
            ),
          ),
              children: <Widget>[ListView(
                  prototypeItem: ListTile(
                    title: Text("megaman"),
                    subtitle: Text("Lanza guisantes"),
                    trailing: IconButton(
                        onPressed: (){},
                        icon: Icon(Icons.navigate_next),
                    ),
                  )
              )],
      ),

    );
  }
}
