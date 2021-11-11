
import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'
import Categories from './components/Categories';

function App() {
  const [status, setStatus] = useState();

  const [dashes, setDashes] = useState();

  const [categories, setCategories] = useState([]);

  const [target, setTarget] = useState('');

  const [category, setCategory] = useState('');

  const [showCategory, setShowCategory] = useState(false);

  const localhost = 'http://127.0.0.1:5000';

  useEffect(()=>{
    axios.get(localhost).then(response => {
      console.log("SUCCESS", response)
      setStatus(response.status);
      setCategories(response.data.categories);
    }).catch(error => {
      console.log(error)
    });
  }, []);

  const handleInput = (e) => {
    let keyPress = e.target.value;
    axios.post(`${localhost}/keypress`, {
      keyPress: keyPress
    })
    .then((response) => {
      console.log(response)
      setDashes(response.data.dashes)
    })
  };

  const showAndPostDashesAndInput = (category) => {
    axios.post(`${localhost}/${category}`, {
        chosenCategory: category
    })
    .then((response) => {
        console.log(response);
        setShowCategory(true);
        setDashes(response.data.dashes);
        setTarget(response.data.target);
    })
    .catch(error => {
        console.log(error)
    });
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
              <div className="btn-group">
                <Categories 
                  categories={categories} 
                  showAndPostDashesAndInput={showAndPostDashesAndInput}
                  setCategory={setCategory}
                />
              </div>
              {
                showCategory ? 
                  <div>
                    <div>{target}</div>
                    <div>Your chosen category is {category}</div>
                    <div>{dashes}</div>
                    <form action='/'>
                      <label htmlFor='letterInput'>Type a letter here:</label>
                      <input id='letterInput' maxLength='1' size='1' type='text' onKeyUp={handleInput}/>
                    </form>
                  </div> : 
                  null
              }
              
              
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