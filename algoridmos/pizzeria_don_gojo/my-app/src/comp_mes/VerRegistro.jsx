import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import Form from 'react-bootstrap/Form';
import GestorOrdenes from '../Gestor';
import VerOrdenes from './VerOrdenes'; // Importa el nuevo componente

function Orden2() {
  const [show, setShow] = useState(false);
  const [ordenes, setOrdenes] = useState([]); // Estado para almacenar las órdenes

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  // Resto de tu código...

  return (
    <>
      {/* Resto de tu JSX... */}
      <Button variant="primary" onClick={() => handleShow()}>
        Ver Órdenes Registradas
      </Button>
      <VerOrdenes ordenes={ordenes} show={show} handleClose={handleClose} />
    </>
  );
}

export default Orden2;
