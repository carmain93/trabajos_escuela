import 'package:args/args.dart';

import 'heroe.dart';



void main(List<String> arguments) {
  heroe alice= heroe();
  //heroe deadpool=heroe( _nombre: "deadpool", _poder: "cool regenerador");
  //heroe babypoool= heroe.Copia(deadpool);
  //print(babypoool);
  Map<String,String> h = {"batman":"dinero"};
  heroe batman = heroe.fromMap(h);
}

class heroe{
  String? _nombre, _poder;
  //forma 1
//heroe(String nombre, String poder):this.nombre=nombre,this.poder=poder;
//forma 2
//heroe({this._nombre="spiderman",this._poder="aracnido"});
heroe(){

}
heroe.Copia(heroe copia){
  _nombre= copia._nombre;
  _poder=copia._poder;
}
heroe.fromMap(Map<String,String>mapa){
  _nombre = mapa.keys.first;
  _poder = mapa[_nombre];
}


set setNombre(String nombre){
   _nombre=nombre;
}
String? get getNombre{
  return _nombre;
}
@override
  String toString() {

    return "nombre: ${_nombre}, poder: ${_poder}";
  }
}
