import './Login.css';
import {React, useState} from 'react';
import Servis from './Servicions';
import Usuarios from './usuarios';
export default function Login(){
    var [v,setInterval]= useState("abraham");
    var chek;
    const array =[ 6,34,65,23,7,4];
    const datos =array.map(value=><li>{value}</li>);
    const json=[
        {nombre:"juan",apellido:"perez",edad:25},
        {nombre:"israel",apellido:"lopez",edad:25},
        {nombre:"elena",apellido:"cabalerra",edad:25}
    ];

    const usr=json.map(u=><li>{u.nombre} {u.apellido}</li>)

    if(v==json[1].nombre){
        chek=<Servis/>
    }else{
        chek=<Usuarios/>
    }
    return(
        <div>
            <h1>Bienvenido</h1>
            <h2>{v}</h2>
            <ul>{usr}</ul>
            <div>
                <input type="text" value={v} onChange={(e)=>setInterval(e.target.value)}></input>
            </div>
            {chek}
        </div>
        
    );
}
