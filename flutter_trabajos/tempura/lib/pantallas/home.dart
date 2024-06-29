import 'dart:async';

import 'package:after_layout/after_layout.dart';
import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';

import '../api/api.dart';
class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> with AfterLayoutMixin<Home> {
  bool visible=false;
  double tem=0, hum=0;
  void get() async{
    try{
      String temp=await Api.get("temperatura");
      String hume= await Api.get("humidity");
      if(temp.contains("Error")|| hume.contains("Error")){
        debugPrint("se genero un error");
    }else{
        tem=double.parse(temp);
        hum=double.parse(hume);
        setState(() {
          visible=true;
        });
      }
    }catch(e){
      debugPrint("segenero un error");
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("esp32 wifi"),

      ),
      body: ,
    );

  }

  @override
  FutureOr<void> afterFirstLayout(BuildContext context) {
    // TODO: implement afterFirstLayout
    throw UnimplementedError();
  }
  
}
