import 'dart:io';

import 'package:flutter/material.dart';
import 'package:sqflite_common_ffi/sqflite_ffi.dart';
import 'pantallas/app.dart';
void main() {
  if(Platform.isWindows || Platform.isLinux || Platform.isMacOS){
    sqfliteFfiInit();
  }
  databaseFactory= databaseFactoryFfi;
  runApp(const App());
}


