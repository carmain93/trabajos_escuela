import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:pruebin3/withyets/logi/imputextlogin.dart';
class Loginform extends StatelessWidget {
  const Loginform({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 330,
      child: Column(
        children: <Widget>[
          Imputextlogin(
            placehoplder: "Email adress",
          ),
          SizedBox(
            height: 20,
          ),
          Imputextlogin(
            placehoplder: "password",
          ),
          SizedBox(
            height: 200,
          ),
        ],
      ),
    );
  }
}
