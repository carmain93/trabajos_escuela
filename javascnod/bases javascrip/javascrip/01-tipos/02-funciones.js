//funcion normal
function sumar(a){

    return console.log(a+100);
    }

a=1;
b=1;
sumar(a);

// funciones anonimas no hosting
// se tienen que guardar en variables
let saludo = function(nombre){
    return console.log("hola "+ nombre);
}
saludo("david");
// funcion felcha que tambien es anonima
let saludo2 = (nombre, trabajo)=>'como has estado ' + nombre + 'en tu trabajo como '+trabajo;

console.log(saludo2("hector","programador"));