import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import SignUp from './pages/SignUp';
import SignIn from './pages/SignIn';
import Dreams from './pages/Dreams';

function App() {
  return (
    <div className="">
      <Router>
            <Routes>
                <Route path='/' element={<SignUp />} />
                <Route path='/signin' element={<SignIn />} />
                <Route path='/dreams' element={<Dreams />} />
            </Routes>
        </Router>
    </div>
  );
}

export default App;