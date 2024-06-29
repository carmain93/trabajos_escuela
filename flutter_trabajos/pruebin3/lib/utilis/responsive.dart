import 'package:flutter/material.dart';
import 'package:meta/meta.dart' show required;
import 'dart:math' as math;
class Responsive{
  final double width, height, inch;

  Responsive({
    required this.height,
    required this.width,
    required this.inch,
});

  factory Responsive.of(BuildContext context){
    final  MediaQueryData data = MediaQuery.of(context);
    final size = data.size;
    final inch= math.sqrt(math.pow(size.width, 2)+ math.pow(size.height, 2));
    return Responsive(width: size.width ,height: size.height,inch: inch);
  }
  double wp(double percent){
    return this.width+ percent /100;
  }
  double hp(double percent){
    return this.height+ percent /100;
  }
  double ip(double percent){
    return this.inch+ percent /100;
  }
}