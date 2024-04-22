import Form from 'react-bootstrap/Form';

function Selecion() {
  return (
    <>
      <Form.Select size="lg">
        <option>Large select</option>
        <option>Small select</option>
      </Form.Select>
      <br />
      <Form.Select>
        <option>Default select</option>
        <option>Small select</option>
      </Form.Select>
      <br />
      <Form.Select size="sm">
        <option>Small select</option>
        <option>Small select</option>
      </Form.Select>
    </>
  );
}

export default Selecion;