import 'planta_energia.dart';
import '../confi/config.dart';
class Solar implements PLanteEnergia{
  double? paneles;


  @override
  double? tEnergia;
  Solar(this.tEnergia,this.paneles);
  @override
  late plantaTipo? tipo= plantaTipo.solar;

  @override
  void consumoeEnergia(double cantidad) {
    if(tEnergia! < cantidad){
      throw Exception("no se puede entregar esa cantidad de energia");
    }
    tEnergia= tEnergia!-cantidad;
  }
  @override
  String toString() {

    return 'nuclear{paneles: $paneles total: $tEnergia tipo: $tipo}';
  }
}