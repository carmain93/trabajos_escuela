library config.globals;

import 'package:flutter/material.dart';
export 'package:flutter/material.dart';

import 'package:flutter/cupertino.dart';
export 'package:flutter/cupertino.dart' hide RefreshCallback;

import 'package:ya/screens/screens.dart';
export 'package:ya/screens/screens.dart';

import 'package:ya/widgets/widgets.dart';
export 'package:ya/widgets/widgets.dart';

class Config{
    static Color firstColor = const Color.fromRGBO(224, 221, 207, 1);
    static Color secondColor = const Color.fromRGBO(31, 1, 185, 1);
    static Color thirdColor = const Color.fromRGBO(153, 143, 199, 1);
    static Color fourthColor = const Color.fromRGBO(71, 68, 72, 1);
    static Color fifthColor = const Color.fromRGBO(186, 45, 11, 1);
    static Color sixColor = const Color.fromRGBO(32, 133, 69, 1);
}