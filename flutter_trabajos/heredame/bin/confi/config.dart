library config.globals;
import '../plantas/planta_energia.dart';
enum plantaTipo{eolica, nuclear, hidroelectrica,solar}

void cargarLaptop(PLanteEnergia planta, double cantidad){
try{
  planta.consumoeEnergia(cantidad);
  print("lap cargada");
} catch(err){
  print("error");
  }

}


