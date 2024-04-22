import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import Form from 'react-bootstrap/Form';
import GestorOrdenes from '../Gestor';

function Orden() {
  const [show, setShow] = useState(false);
  const [ordenes, setOrdenes] = useState([]);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const handleChangePizza = (e) => { /* Lógica de cambio de pizza */ };
  const handleChangeEspagueti = (e) => { /* Lógica de cambio de espagueti */ };
  const handleChangeBoneless = (e) => { /* Lógica de cambio de boneless */ };
  const handleChangePapasFritas = (e) => { /* Lógica de cambio de papas fritas */ };
  const handleChangeEnsalada = (e) => { /* Lógica de cambio de ensalada */ };
  const handleChangeBebida = (e) => { /* Lógica de cambio de bebida */ };

  const handleGuardarOrden = () => {
    const nuevaOrden = {
      pizza: {}, espagueti: {}, boneless: {}, papasFritas: {}, ensalada: {}, bebida: {}
    };
    // Llenar nuevaOrden con los datos seleccionados
    // ...
    // Agregar la nueva orden al estado ordenes
    setOrdenes([...ordenes, nuevaOrden]);
    handleClose();
  }

  return (
    <>
      <Button variant="success" onClick={handleShow}>
        Meseros
      </Button>

      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Registrar Orden</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form>
            {/* Agregar selectores de platillos aquí */}
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Cancelar
          </Button>
          <Button variant="primary" onClick={handleGuardarOrden}>
            Guardar
          </Button>
        </Modal.Footer>
      </Modal>
      {show && <GestorOrdenes ordenes={ordenes} />}
    </>
  );
}

export default Orden;



