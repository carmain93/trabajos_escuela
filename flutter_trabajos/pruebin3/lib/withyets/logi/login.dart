import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:pruebin3/withyets/logi/loginform.dart';
import 'package:pruebin3/withyets/logi/wel.dart';
class Login extends StatefulWidget {
  const Login({super.key});

  @override
  State<Login> createState() => _LoginState();
}

class _LoginState extends State<Login> {

  void initState(){
    super.initState();
    SystemChrome.setSystemUIOverlayStyle(SystemUiOverlayStyle.dark);

  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        width: double.infinity,
        height: double.infinity,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: <Widget>[
            Welcome(),
            Loginform(),
          ],
        ),
      ),

    );
  }
}
