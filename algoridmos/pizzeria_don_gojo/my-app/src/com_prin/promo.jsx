import Card from 'react-bootstrap/Card';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Im3 from '../imagenes/promo3.jpeg';
import Im2 from '../imagenes/promo2.jpg';
import Im1 from '../imagenes/SvLu92pfoLXdLHK55-1200-1200.webp';
function Promos({ title, cuerp, Im }) {
    if(Im === 1){
        Im=Im1;
       }
   if (Im === 2) {
    Im = Im2;
   }
   if(Im === 3){
    Im=Im3;
   }
    return (
        <div className="col">
            <div className="card h-100">
            <img src={Im} className="card-img-top" alt="..." />
                <div className="card-body">
                    <h5 className="card-title">{title}</h5>
                    <p className="card-text">{cuerp}</p>
                </div>
            </div>
        </div>
    );
}
export default Promos;