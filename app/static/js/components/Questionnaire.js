import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Card, Form, Button, ProgressBar } from 'react-bootstrap';
import axios from 'axios';

function Questionnaire() {
  const [questionnaire, setQuestionnaire] = useState(null);
  const [currentCategory, setCurrentCategory] = useState(0);
  const [currentSubcategory, setCurrentSubcategory] = useState(0);
  const [responses, setResponses] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchQuestionnaire();
  }, []);

  const fetchQuestionnaire = async () => {
    try {
      const response = await axios.get('/api/questionnaire');
      setQuestionnaire(response.data);
      setLoading(false);
    } catch (err) {
      setError('Failed to load questionnaire');
      setLoading(false);
    }
  };

  const handleResponse = (question, value) => {
    setResponses(prev => ({
      ...prev,
      [question]: value
    }));
  };

  const handleNext = () => {
    if (currentSubcategory < Object.keys(questionnaire[Object.keys(questionnaire)[currentCategory]]).length - 1) {
      setCurrentSubcategory(prev => prev + 1);
    } else if (currentCategory < Object.keys(questionnaire).length - 1) {
      setCurrentCategory(prev => prev + 1);
      setCurrentSubcategory(0);
    } else {
      handleSubmit();
    }
  };

  const handleSubmit = async () => {
    try {
      await axios.post('/api/responses', responses);
      // Handle successful submission
    } catch (err) {
      setError('Failed to submit responses');
    }
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>{error}</div>;
  if (!questionnaire) return <div>No questionnaire available</div>;

  const categories = Object.keys(questionnaire);
  const currentCategoryName = categories[currentCategory];
  const subcategories = Object.keys(questionnaire[currentCategoryName]);
  const currentSubcategoryName = subcategories[currentSubcategory];
  const questions = questionnaire[currentCategoryName][currentSubcategoryName];

  const progress = ((currentCategory * 100) / categories.length) +
    ((currentSubcategory * 100) / (subcategories.length * categories.length));

  return (
    <Container className="py-5">
      <Row className="justify-content-center">
        <Col md={8}>
          <Card className="shadow">
            <Card.Body>
              <ProgressBar now={progress} className="mb-4" />
              <h2 className="mb-4">{currentCategoryName}</h2>
              <h4 className="mb-4">{currentSubcategoryName}</h4>
              <Form>
                {questions.map((question, index) => (
                  <Form.Group key={index} className="mb-4">
                    <Form.Label>{question}</Form.Label>
                    <Form.Control
                      as="textarea"
                      rows={3}
                      value={responses[question] || ''}
                      onChange={(e) => handleResponse(question, e.target.value)}
                    />
                  </Form.Group>
                ))}
                <Button variant="primary" onClick={handleNext}>
                  {currentCategory === categories.length - 1 && 
                   currentSubcategory === subcategories.length - 1 
                   ? 'Submit' 
                   : 'Next'}
                </Button>
              </Form>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
}

export default Questionnaire; 