import '../confi/config.dart';
abstract class PLanteEnergia{
  double? tEnergia;
  late final plantaTipo? tipo;

  PLanteEnergia(this.tEnergia,this.tipo);
  void consumoeEnergia(double cantidad);

}

