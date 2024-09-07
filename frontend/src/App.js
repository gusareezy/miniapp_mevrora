import './App.css';

import { Routes, Route } from 'react-router-dom';
import Stats from './pages/Stats';
import Tiers from './pages/Tiers';
import Homepage from './pages/Homepage';
import Layout from './components/Layout';

function App() {
  return (
    <>
      <Routes>
        <Route path='/' element={<Layout />}>
          <Route index element={<Homepage />} />
          <Route path='stats' element={<Stats />} />
          <Route path='tiers' element={<Tiers />} />
        </Route>
      </Routes>
    </>
  );
}

export default App;
