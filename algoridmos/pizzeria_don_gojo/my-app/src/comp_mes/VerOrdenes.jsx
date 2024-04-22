import React from 'react';
import Modal from 'react-bootstrap/Modal';
import Button from 'react-bootstrap/Button';

function VerOrdenes({ ordenes, show, handleClose }) {
  return (
    <Modal show={show} onHide={handleClose}>
      <Modal.Header closeButton>
        <Modal.Title>Órdenes Registradas</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        {ordenes.map((orden, index) => (
          <div key={index}>
            <p><strong>Orden {index + 1}:</strong></p>
            <p>Pizza: {orden.pizza.nombre} - Precio: {orden.pizza.precio}</p>
            <p>Espagueti: {orden.espagueti.nombre} - Precio: {orden.espagueti.precio}</p>
            <p>Boneless: {orden.boneless.nombre} - Precio: {orden.boneless.precio}</p>
            <p>Papas Fritas: {orden.papasFritas.nombre} - Precio: {orden.papasFritas.precio}</p>
            <p>Ensalada: {orden.ensalada.nombre} - Precio: {orden.ensalada.precio}</p>
            <p>Bebida: {orden.bebida.nombre} - Precio: {orden.bebida.precio}</p>
            <hr />
          </div>
        ))}
      </Modal.Body>
      <Modal.Footer>
        <Button variant="secondary" onClick={handleClose}>
          Cerrar
        </Button>
      </Modal.Footer>
    </Modal>
  );
}

export default VerOrdenes;