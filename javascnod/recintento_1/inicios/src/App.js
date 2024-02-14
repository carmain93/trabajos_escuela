import logo from './logo.svg';
import './App.css';
function bot(presion) {
  /*if (presion=== true) {
    return (
      <buton>hola</buton>
    )
  } else {
    return (
      <buton>adios</buton>
    )
  }*/
}
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>HOLA MUNDO DISCO</h1>
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      <body>
        <h1 style={{backgroundColor: "blue",}}>intento de boton</h1>
        <h1 className="titulo" >ejemplo estilo 2</h1>
        <h1>ahora si boton</h1>
        
      </body>
    </div>
  );
}

export default App;
