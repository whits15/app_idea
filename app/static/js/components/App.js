import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './Navbar';
import Home from './Home';
import Dashboard from './Dashboard';
import Questionnaire from './Questionnaire';
import Login from './Login';
import Register from './Register';
import { AuthProvider } from '../contexts/AuthContext';
import PrivateRoute from './PrivateRoute';

function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="App">
          <Navbar />
          <Switch>
            <Route exact path="/" component={Home} />
            <Route path="/login" component={Login} />
            <Route path="/register" component={Register} />
            <PrivateRoute path="/dashboard" component={Dashboard} />
            <PrivateRoute path="/questionnaire" component={Questionnaire} />
          </Switch>
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App; 