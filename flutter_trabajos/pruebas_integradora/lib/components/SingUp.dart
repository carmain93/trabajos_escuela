import 'package:flutter/material.dart';

class App extends StatefulWidget {
  const App({super.key});

  @override
  State<App> createState() => _AppState();
}

class _AppState extends State<App> {
  final _formKey = GlobalKey<FormState>();
  final _vimController = TextEditingController();

  @override
  void dispose() {
    _vimController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Mi AppBar'),
          actions: <Widget>[
            IconButton(
              icon: Icon(Icons.settings),
              onPressed: () {
                // Acción al presionar el botón
                print('Botón de ajustes presionado');
              },
            ),
          ],
        ),
        body: Container(
          margin: const EdgeInsets.all(16.0),
          child: Form(
            key: _formKey,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: <Widget>[
                Row(
                  children: <Widget>[
                    Text("Introduce el VIM del vehículo"),
                    SizedBox(width: 8),
                    Icon(Icons.ac_unit_sharp),
                  ],
                ),
                TextFormField(
                  controller: _vimController,
                  decoration: InputDecoration(
                    labelText: 'VIM',
                    hintText: 'Introduce el VIM del vehículo',
                  ),
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Por favor, introduce el VIM';
                    }
                    return null;
                  },
                ),
                Padding(
                  padding: const EdgeInsets.symmetric(vertical: 16.0),
                  child: ElevatedButton(
                    onPressed: () {
                      // Validar el formulario
                      if (_formKey.currentState!.validate()) {
                        // Si el formulario es válido, mostrar un snackbar
                        ScaffoldMessenger.of(context).showSnackBar(
                          SnackBar(content: Text('Procesando datos')),
                        );
                      }
                    },
                    child: Text('Enviar'),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}


