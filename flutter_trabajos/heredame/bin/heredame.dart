import 'package:heredame/heredame.dart' as heredame;
import 'plantas/nuclear.dart';
import 'plantas/solar.dart';
import 'confi/config.dart';
void main(List<String> arguments) {
  nuclear nuke = nuclear(tEnergia: 1000,temeperatura: 2000);


  Solar sunny= Solar(2000,1000);
  cargarLaptop(sunny,330);
  print(sunny);

}




//upcasting

