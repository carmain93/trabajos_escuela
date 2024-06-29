import 'planta_energia.dart';
import '../confi/config.dart';

class nuclear extends PLanteEnergia{
double? temeperatura;


  nuclear({ ktipo=plantaTipo.nuclear,required tEnergia,this.temeperatura}):super(tEnergia,plantaTipo.nuclear);
  @override
  void consumoeEnergia(double cantidad) {
    if(tEnergia! < cantidad){
      throw Exception("no se puede entregar esa cantidad de energia");
    }
    tEnergia= tEnergia!-cantidad;
  }
  @override
  String toString() {

    return 'nuclear{temperatura: $temeperatura total: $tEnergia tipo: $tipo}';
  }
}

