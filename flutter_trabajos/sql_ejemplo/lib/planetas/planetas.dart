class Planetas{
  int? id;
 String? nombre;
 double? distancia;
 double? radio;

  Planetas(this.id,this.nombre,this.distancia,this.radio);
  //constructores
  Planetas.deMapa(Map<String, dynamic> mapa){
   id = mapa["id"];
   nombre=mapa["nombre"];
   distancia = mapa["distancia"];
   radio=mapa["radio"];
  }
  Map<String, dynamic> mapeador(){
    return{
      "id":id,
      "nombre":nombre,
      "distancia":distancia,
      "radio":radio
    };
  }
}