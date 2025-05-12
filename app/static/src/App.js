import React, { useState } from 'react';
import Chat from './Chat';
import Questionnaire from './Questionnaire';

function App() {
  const [responses, setResponses] = useState({});
  const [submitted, setSubmitted] = useState(false);

  const handleTestData = async () => {
    try {
      const response = await fetch('/api/load_test_data');
      const data = await response.json();
      if (response.ok) {
        setResponses(data);
        setSubmitted(true);
      } else {
        console.error('Error:', data.error);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  if (submitted) {
    return <Chat userData={responses} />;
  }

  return (
    <div style={{ maxWidth: '800px', margin: '0 auto', padding: '20px' }}>
      <div style={{ 
        textAlign: 'center', 
        marginBottom: '30px',
        padding: '20px',
        backgroundColor: '#f8f9fa',
        borderRadius: '8px',
        boxShadow: '0 2px 4px rgba(0,0,0,0.1)'
      }}>
        <h1 style={{ marginBottom: '20px' }}>Personal Assessment Questionnaire</h1>
        <button
          onClick={handleTestData}
          style={{
            backgroundColor: '#28a745',
            color: 'white',
            padding: '12px 24px',
            border: 'none',
            borderRadius: '6px',
            cursor: 'pointer',
            fontSize: '16px',
            fontWeight: 'bold',
            boxShadow: '0 2px 4px rgba(0,0,0,0.2)',
            transition: 'all 0.3s ease'
          }}
          onMouseOver={(e) => e.target.style.backgroundColor = '#218838'}
          onMouseOut={(e) => e.target.style.backgroundColor = '#28a745'}
        >
          Use Test Data
        </button>
      </div>
      <Questionnaire onComplete={(data) => {
        setResponses(data);
        setSubmitted(true);
      }} />
    </div>
  );
}

export default App; 