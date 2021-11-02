
import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'
import Categories from './components/Categories';

function App() {
  const [status, setStatus] = useState();

  const [dashes, setDashes] = useState();

  const [categories, setCategories] = useState([]);

  useEffect(()=>{
    axios.get('http://localhost:5000').then(response => {
      console.log("SUCCESS", response)
      setStatus(response.status);
      setDashes(response.data.dashes);
      setCategories(response.data.categories)
      loadInputs(response.data.dashes);
      
    }).catch(error => {
      console.log(error)
    })
  }, []);

  const loadInputs = (dashes) => {
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>Hangman</p>
        <div>
          {
            status === 200 
            ? 
            <div>
              <div>
                {dashes}
              </div>
              <div className="btn-group">
                <Categories categories={categories}/>
              </div>
            </div>
            :
            <h3>LOADING</h3>
          }
          
        </div>
      </header>
    </div>
  );
}

export default App;