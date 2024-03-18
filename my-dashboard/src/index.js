import React from 'react';
import ReactDOM from 'react-dom/client';
import FinancialChart from './FinancialChart'; // Assurez-vous que le chemin est correct
import './index.css'; // Si vous avez un fichier CSS global

const container = document.getElementById('root');
const root = ReactDOM.createRoot(container);

root.render(
  <React.StrictMode>
    <FinancialChart />
  </React.StrictMode>
);
