import React from 'react';
import { Button } from 'react-bootstrap';
import './Login.css';


export const LoginPage = () => {
  return (
    <>
      <text className="textfield">
            Bitte nutzen Sie den Login des HPI openID Connect.
      </text>
      <Button variant="primary" size="lg" href="https://test.de">
            Einloggen
      </Button>
    </>
  );
};
