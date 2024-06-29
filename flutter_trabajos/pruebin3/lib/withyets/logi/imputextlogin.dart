import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:pruebin3/withyets/logi/loginform.dart';
import 'package:pruebin3/withyets/logi/wel.dart';

class Imputextlogin extends StatelessWidget {
  //final String iconPhat;
  final String placehoplder;
  const Imputextlogin({super.key,
  /*required this.iconPhat,*/
    required this.placehoplder
  });

  @override
  Widget build(BuildContext context) {
    return CupertinoTextField(
        padding:  EdgeInsets.symmetric(vertical: 10,horizontal: 10),
        prefix: Container(
          width: 20,
          height: 30,
          padding: EdgeInsets.all(5) ,
//child: SvgPicture.asset(assetName),
        ),
        placeholder: this.placehoplder,
        decoration:  BoxDecoration(
          border:  Border(
            bottom: BorderSide(
              width: 1,
              color: Color(0xffdddddd),
            ),
          ),
        ),
      );
  }
}
