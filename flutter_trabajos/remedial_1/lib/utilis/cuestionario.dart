import 'package:flutter/material.dart';
class Cuestionario extends StatefulWidget {
  const Cuestionario({super.key});

  @override
  State<Cuestionario> createState() => _CuestionarioState();
}

class _CuestionarioState extends State<Cuestionario> {
  bool? isChecked = false;

  @override
  Widget build(BuildContext context) {
    return Form(
     // key: _formKey,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[
          Center(
            child: Column(
              children: [
                TextFormField(
                  decoration: const InputDecoration(
                    hintText: 'Enter your email',
                  ),
                  validator: (String? email) {
                    if (email == null || email.isEmpty) {
                      return 'Please enter some text';
                    }
                    return null;
                  },
                ),
              ],
            ),
          ),
          TextFormField(
            decoration: const InputDecoration(
              hintText: 'Tu nombre',
            ),
            validator: (String? nombre) {
              if (nombre == null || nombre.isEmpty) {
                return 'Please enter some text';
              }
              return nombre;
            },
          ),
          Checkbox.adaptive(
          checkColor: Colors.white,
          value: isChecked,
          onChanged: (bool? value) {
          setState(() {
          isChecked = value!;
           });
          },
          ),
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 16.0),
            child: ElevatedButton(
              onPressed: () {
                //print(nombre);
                // Validate will return true if the form is valid, or false if
                // the form is invalid.
                //if (_formKey.currentState!.validate()) {
                  // Process data.
                //}
              },
              child: const Text('Submit'),
            ),
          ),
        ],
      ),
    );
  }
}

class CheckboxWithTitle extends StatefulWidget {
  final String title;

  CheckboxWithTitle({required this.title});

  @override
  _CheckboxWithTitleState createState() => _CheckboxWithTitleState();
}

class _CheckboxWithTitleState extends State<CheckboxWithTitle> {
  bool isChecked = false;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.all(8.0),
      decoration: BoxDecoration(
        border: Border.all(color: Colors.blue, width: 2.0),
        borderRadius: BorderRadius.circular(5.0),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Checkbox.adaptive(
            checkColor: Colors.white,
            value: isChecked,
            onChanged: (bool? value) {
              setState(() {
                isChecked = value!;
              });
            },
          ),
          Text(widget.title, style: TextStyle(fontSize: 16.0)),
        ],
      ),
    );
  }
}
