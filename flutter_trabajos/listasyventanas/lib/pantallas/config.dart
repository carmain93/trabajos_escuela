library config.globals;

import 'package:flutter/material.dart';
export 'package:flutter/material.dart';
import '../pantallas/pantallas.dart';
export '../pantallas/pantallas.dart';
import '../pantallas/home.dart';
export '../pantallas/home.dart';
import '../pantallas/listamanual.dart';
//export '../pantallas/listamanual.dart;

class Config{
  static Map<String, Widget Function(BuildContext context)> rutas={
    "home": (BuildContext context)=>Home(),
    "manuales": (BuildContext context)=>Listamanual(),
    "creadas": (BuildContext context)=>Listamanual(),
  };
}