import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import SignUp from './pages/SignUp';

function App() {
  return (
    <div className="">
      <Router>
            <Routes>
                <Route path='/signup' element={<SignUp />} />
            </Routes>
        </Router>
    </div>
  );
}

export default App;