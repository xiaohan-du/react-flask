
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
    axios.get('http://127.0.0.1:5000/').then(response => {
      console.log("SUCCESS", response)
      setStatus(response.status);
      setDashes(response.data.dashes);
      setCategories(response.data.categories);
    }).catch(error => {
      console.log(error)
    });
  }, []);

  const handleInput = (e) => {
    let keyPress = e.target.value;
    axios.post('http://127.0.0.1:5000', {
      keyPress: keyPress
    })
    .then((response) => {
      console.log(response)
    })
  };

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
              <form action='/'>
                <label for='letterInput'>Type a letter here:</label>
                <input id='letterInput' maxLength='1' size='1' type='text' onKeyUp={handleInput}/>
              </form>
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