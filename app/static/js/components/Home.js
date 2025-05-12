import React from 'react';
import { Container, Row, Col, Card, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <Container className="py-5">
      <Row className="justify-content-center">
        <Col md={8}>
          <Card className="shadow">
            <Card.Body className="text-center">
              <h1 className="mb-4">Welcome to Personal Assessment</h1>
              <p className="lead mb-4">
                Take our comprehensive assessment to get personalized insights and recommendations
                for your physical and mental well-being.
              </p>
              <div className="d-grid gap-3">
                <Link to="/questionnaire">
                  <Button variant="primary" size="lg">
                    Start Assessment
                  </Button>
                </Link>
                <Link to="/login">
                  <Button variant="outline-primary" size="lg">
                    Login
                  </Button>
                </Link>
              </div>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
}

export default Home; 