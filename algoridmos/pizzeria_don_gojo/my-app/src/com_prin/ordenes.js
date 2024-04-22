
class Orden {//inicio de la clase
    constructor(cliente, pedido=[{ 'id':null,'nombre':'','precio':null}]) {
      this.cliente = cliente;
      this.pedido = pedido;
    }
    vacio(){
        if (this.pedido.length === 0) {
            return "El pedido está vacío.";
          }
          if (this.pedido.length > 6) {
            return "El pedido no puede contener más de 6 productos.";
          }
          return "El pedido es válido.";
    }
    añadir(producto) {
        // Verificar si el pedido ya tiene 6 productos
        if (this.pedido.length >= 6) {
          return "No se pueden agregar más productos, el pedido ya tiene 6 productos.";
        }
        // Agregar el producto al pedido
        this.pedido.push(producto);
        return "Producto agregado al pedido correctamente.";
      }
      consultar() {
        let resultado = `Orden para ${this.cliente}:\n`;
        if (this.pedido.length === 0) {
          resultado += "El pedido está vacío.";
        } else {
          resultado += "Productos en el pedido:\n";
          this.pedido.forEach((producto, index) => {
            resultado += `${index + 1}. ${producto}\n`;
          });
        }
        return resultado;
      }
    //fin de la clase
  }