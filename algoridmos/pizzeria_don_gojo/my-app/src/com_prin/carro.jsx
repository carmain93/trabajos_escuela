import Im1 from '../imagenes/promo1.jpg';
import Im2 from '../imagenes/promo2.jpg';
import React from 'react';
import { Carousel } from 'react-bootstrap';

function Carru() {
    return (
        <Carousel>
            <Carousel.Item>
                <img
                    className="d-block w-100"
                    src={Im1}
                    alt="de la debo"
                    style={{ maxWidth: '80%', maxHeight: '50%', display: 'block', margin: 'auto', height: 'auto' }}
                />
            </Carousel.Item>
            <Carousel.Item>
                <img
                    className="d-block w-100"
                    src={Im2}
                    alt="se la debo joven"
                    style={{ maxWidth: '80%', maxHeight: '50%', display: 'block', margin: 'auto', height: 'auto' }}
                />
            </Carousel.Item>
        </Carousel>
    );
}

export default Carru;
