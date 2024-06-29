import 'package:flutter/material.dart';
class Dash extends StatelessWidget {
  const Dash({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(appBar: AppBar(
      title: Text("dash"),
      elevation: 3,
    ),
    body: Center(
      child: ElevatedButton(
        child: Text("back"
        ),
        onPressed: (){
          Navigator.pop(context);
        },
        autofocus: true,)
      ,)
      ,);
  }
}
