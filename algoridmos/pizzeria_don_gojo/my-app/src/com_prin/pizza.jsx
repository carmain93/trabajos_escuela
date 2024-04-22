import Form from 'react-bootstrap/Form';
import Im1 from '../imagenes/logo.jpg';
function CheckInlineExample() {
  return (
    <Form>
      {['checkbox', 'radio'].map((type) => (
        <div key={`inline-${type}`} className="mb-3">
            <div className='card-group' >
            <img
                    className="d-block w-100"
                    src={Im1}
                    alt="de la debo"
                    style={{ maxWidth: '10%', maxHeight: '8%', display: 'block', margin: 'auto', height: 'auto' }}
                />
                <img
                    className="d-block w-100"
                    src={Im1}
                    alt="de la debo"
                    style={{ maxWidth: '10%', maxHeight: '8%', display: 'block', margin: 'auto', height: 'auto' }}
                />
                <img
                    className="d-block w-100"
                    src={Im1}
                    alt="de la debo"
                    style={{ maxWidth: '10%', maxHeight: '8%', display: 'block', margin: 'auto', height: 'auto' }}
                />
                <img
                    className="d-block w-100"
                    src={Im1}
                    alt="de la debo"
                    style={{ maxWidth: '10%', maxHeight: '8%', display: 'block', margin: 'auto', height: 'auto' }}
                />
            </div>
          <Form.Check
            inline
            label="1"
            name="group1"
            type={type}
            id={`inline-${type}-1`}
          />
          <Form.Check
            inline
            label="2"
            name="group1"
            type={type}
            id={`inline-${type}-2`}
          />
          <Form.Check
            inline
            label="3"
            name="group1"
            type={type}
            id={`inline-${type}-3`}
          />
        </div>
      ))}
    </Form>
  );
}

export default CheckInlineExample;