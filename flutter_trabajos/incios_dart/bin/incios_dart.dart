import 'package:args/args.dart';

const String version = '0.0.1';



void main(List<String> arguments) {
  List<String?>? texto=["iguana","perro","hamster","gato","camaleon","tarantula","tortuga","gato",null];
  Set<int> conjunto ={1,2,3,4};
  print(texto);
  //diciionario donde un valor es el indice del otro valor y los indices no pueden ser repetidos
  Map<int,String> alumno={1:"Rodolfo",2:"hoel",3:"milton",};// notacion json

  Map<String,dynamic> dina={"uno":[1,2,3],"dos":"tres","cuatro":true,"quinto":{1:"tortuga",2:"tarantula"}};
  print(texto[4]);
  print(texto.length);
  texto.add("pony");
  print(texto.length);
  print(alumno[2]);
  print(dina["quinto"][1]);
  Map<dynamic,dynamic> dinadina={"1":true,true:{1,2,3,4},2:{true,true,false}};
  print(texto.reversed);
  print(texto.first);
  //esta lista no jala no se porque
  //casting
  //final List<dynamic> listita= dinadina[2] as List<dynamic>;
  //print(listita.reversed);
  List<int> numeros=[1,2,3,4,5,6];
  print("la suma de 3 + 4 es= ${sumar(3,4)}");
  final mayores = numeros.where((num)=>num>=5);
  print(mayores);
  print("suma= ${suma(0,3)}");
}

//metodo nomarla que no regresa nada
void metodo(){

}
//crear una lamda
//final mayores = numeros.where((num)=>num>=5);

metodos(){//esto se considera un metodo dinamico por defecto
  if(true)
    return 1;
  else
    return "1";

}
//funcion nomral sin fat arrow
int suma([int? a=0, int? b=0]){
  b??=3;
  return a!+b!;
}
// notacion fat arrow (lambdas)
int sumar(int a,int b)=>a+b;
//notacion javasript
//final int sumarr=(int a,int b)=a+b;
//parametros con nombre

