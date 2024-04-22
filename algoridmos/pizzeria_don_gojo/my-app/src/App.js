import React, { useState } from 'react';
import Orden from './comp_mes/formu.jsx'; // Importa el componente Orden
import Orden2 from './comp_mes/VerRegistro.jsx'; // Importa el componente Orden2
import './App.css';
import lo from './imagenes/logo.jpg';
import Carru from './com_prin/carro.jsx';
import Promos from './com_prin/promo.jsx';
import Selecion from './com_prin/quest.jsx';
import CheckInlineExample from './com_prin/pizza.jsx';
import TodoApp from './com_prin/prueba.jsx';

function Navegar() {
  const [showOrden, setShowOrden] = useState(false);
  const [showOrden2, setShowOrden2] = useState(false);

  const handleShowOrden = () => {
    setShowOrden(true);
    setShowOrden2(false); // Aseguramos que el modal de Orden2 esté cerrado al abrir el modal de Orden
  };

  const handleShowOrden2 = () => {
    setShowOrden(false); // Aseguramos que el modal de Orden esté cerrado al abrir el modal de Orden2
    setShowOrden2(true);
  };

  const handleCloseOrden = () => setShowOrden(false);
  const handleCloseOrden2 = () => setShowOrden2(false);

  console.log("showOrden:", showOrden); // Agrega console.log para verificar el estado
  console.log("showOrden2:", showOrden2); // Agrega console.log para verificar el estado

  return (
    <>
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container-fluid">
          <a className="navbar-brand" href="#">
            <img src={lo} width="40" height="34" alt="Logo" />
          </a>
          <a className="navbar-brand" href="#">Pizzeria don gojo</a>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div className="navbar-nav">
              <a className="nav-link active" aria-current="page" href="#">Inicio</a>
              <a className="nav-link" href="#">Productos</a>
              <a className="nav-link" href="#">Sobre nosotros</a>
              <button className="btn btn-warning" onClick={handleShowOrden}>Registrar Orden</button>
              <button className="btn btn-info" onClick={handleShowOrden2}>Ver Órdenes</button>
            </div>
          </div>
        </div>
      </nav>

      <Orden show={showOrden} handleClose={handleCloseOrden} />
      <Orden2 show={showOrden2} handleClose={handleCloseOrden2} />
    </>
  );
}



function App() {
 
  return (
    <div className="App">
      <script src="https://cdn.jsdelivr.net/npm/react/umd/react.production.min.js" crossorigin></script>

<script
  src="https://cdn.jsdelivr.net/npm/react-dom/umd/react-dom.production.min.js"
  crossorigin></script>

<script
  src="https://cdn.jsdelivr.net/npm/react-bootstrap@next/dist/react-bootstrap.min.js"
  crossorigin></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous"></link>
      <Navegar></Navegar>
      <br></br>
      <Carru></Carru>
      <br></br>
      <h3>Mira nuestra diversas promociones</h3>
      <div class="row row-cols-1 row-cols-md-3 g-4">
      <Promos
      Im={1}
      title={'Servicio al mayoreo'}
      cuerp={'Para aquellos que tienen grandes planes'}
      ></Promos> 
      <Promos
      Im={2}
      title={'Paquetes'}
      cuerp={'Disfruta de los distintos paquetes que podemos ofrecer'}
      ></Promos> 
      <Promos
      Im={3}
      title={'Ornedes rapidas y faciles '}
      cuerp={'Ordena ya de forma facil y rapida'}
      ></Promos> 
      
      </div>
      <br></br>
      <h2 center>Ordene aqui</h2>
      <br></br>
      <CheckInlineExample></CheckInlineExample>
      <Selecion></Selecion>
      <br></br>
      <TodoApp></TodoApp>
      <br></br>
      
      
    </div>
  );
}

export default App;
