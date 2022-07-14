import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import SignUp from './pages/SignUp';
import SignIn from './pages/SignIn';

function App() {
  return (
    <div className="">
      <Router>
            <Routes>
                <Route path='/signup' element={<SignUp />} />
                <Route path='/signin' element={<SignIn />} />
            </Routes>
        </Router>
    </div>
  );
}

export default App;