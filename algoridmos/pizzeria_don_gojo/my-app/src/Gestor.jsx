import React, { Component } from 'react';

class GestorOrdenes extends Component {
  constructor(props) {
    super(props);
    this.state = {
      ordenes: [],
      nuevaOrden: {
        cliente: '',
        platillos: []
      }
    };
  }

  handleChange = (e) => {
    const { nuevaOrden } = this.state;
    this.setState({
      nuevaOrden: {
        ...nuevaOrden,
        [e.target.name]: e.target.value
      }
    });
  }

  handlePlatilloChange = (index, e) => {
    const { nuevaOrden } = this.state;
    const nuevosPlatillos = [...nuevaOrden.platillos];
    nuevosPlatillos[index][e.target.name] = e.target.value;
    this.setState({
      nuevaOrden: {
        ...nuevaOrden,
        platillos: nuevosPlatillos
      }
    });
  }

  handleAgregarPlatillo = () => {
    const { nuevaOrden } = this.state;
    this.setState({
      nuevaOrden: {
        ...nuevaOrden,
        platillos: [...nuevaOrden.platillos, { nombre: '', precio: '' }]
      }
    });
  }

  handleEliminarPlatillo = (index) => {
    const { nuevaOrden } = this.state;
    const nuevosPlatillos = nuevaOrden.platillos.filter((_, i) => i !== index);
    this.setState({
      nuevaOrden: {
        ...nuevaOrden,
        platillos: nuevosPlatillos
      }
    });
  }

  handleSubmitOrden = (e) => {
    e.preventDefault();
    const { nuevaOrden, ordenes } = this.state;
    if (!nuevaOrden.cliente || nuevaOrden.platillos.length === 0) {
      alert('Por favor ingresa todos los detalles de la orden.');
      return;
    }
    this.setState({
      ordenes: [...ordenes, nuevaOrden],
      nuevaOrden: {
        cliente: '',
        platillos: []
      }
    });
  }

  handleVerOrdenes = () => {
    const { ordenes } = this.state;
    if (ordenes.length === 0) {
      alert('No hay órdenes registradas.');
      return;
    }
    console.log(ordenes);
  }

  handleEliminarOrden = (index) => {
    const { ordenes } = this.state;
    const nuevasOrdenes = ordenes.filter((_, i) => i !== index);
    this.setState({ ordenes: nuevasOrdenes });
  }

  render() {
    const { nuevaOrden, ordenes } = this.state;

    return (
      <div>
        <h2>Gestor de Órdenes</h2>
        <form onSubmit={this.handleSubmitOrden}>
          <div>
            <label>Cliente:</label>
            <input type="text" name="cliente" value={nuevaOrden.cliente} onChange={this.handleChange} />
          </div>
          <h3>Platillos</h3>
          {nuevaOrden.platillos.map((platillo, index) => (
            <div key={index}>
              <label>Nombre:</label>
              <input type="text" name="nombre" value={platillo.nombre} onChange={(e) => this.handlePlatilloChange(index, e)} />
              <label>Precio:</label>
              <input type="text" name="precio" value={platillo.precio} onChange={(e) => this.handlePlatilloChange(index, e)} />
              <button type="button" onClick={() => this.handleEliminarPlatillo(index)}>Eliminar Platillo</button>
            </div>
          ))}
          <button type="button" onClick={this.handleAgregarPlatillo}>Agregar Platillo</button>
          <button type="submit">Registrar Orden</button>
        </form>
        <div>
          <h3>Órdenes Registradas</h3>
          {ordenes.map((orden, index) => (
            <div key={index}>
              <p><strong>Cliente:</strong> {orden.cliente}</p>
              <p><strong>Platillos:</strong></p>
              <ul>
                {orden.platillos.map((platillo, i) => (
                  <li key={i}>
                    <strong>Nombre:</strong> {platillo.nombre}, <strong>Precio:</strong> {platillo.precio}
                  </li>
                ))}
              </ul>
              <button type="button" onClick={() => this.handleEliminarOrden(index)}>Eliminar Orden</button>
            </div>
          ))}
          <button type="button" onClick={this.handleVerOrdenes}>Ver Órdenes</button>
        </div>
      </div>
    );
  }
}

export default GestorOrdenes;