
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

  const [message, setMessage] = useState('');

  const [showCategory, setShowCategory] = useState(false);

  const localhost = 'http://127.0.0.1:5000';

  const [inputValue, setInputValue] = useState('');

  const [guessed, setGuessed] = useState([]);

  const [alphabet, setAlphabet] = useState('abcdefghijklmnopqrstuvwxyz');

  useEffect(() => {
    axios.get(localhost).then(response => {
      console.log("SUCCESS", response)
      setStatus(response.status);
      setCategories(response.data.categories);
    }).catch(error => {
      console.log(error)
    });
  }, []);

  const handleKeyUp = (e) => {
    let keyUp = e.target.value;
    axios.post(`${localhost}/keyup`, {
      keyUp: keyUp
    })
      .then((response) => {
        console.log(response);
        setDashes(response.data.dashes);
        setMessage(response.data.message);
        setGuessed(response.data.guessed);
      });
  };

  const handleKeyDown = (e) => {
    let keyDown = e.key;
    setInputValue(keyDown);
  }

  const showAndPostDashesAndInput = (category) => {
    axios.post(`${localhost}/${category}`, {
      chosenCategory: category
    })
      .then((response) => {
        console.log(response);
        setShowCategory(true);
        setDashes(response.data.dashes);
        setTarget(response.data.target);
        setInputValue('');
      })
      .catch(error => {
        console.log(error)
      });
  };

  useEffect(() => {
    let al = 'abcdefghijklmnopqrstuvwxyz';
    al.split('').map((char, index) => {
      if (guessed.includes(char)) {
        al = al.substr(0, index) + al[index].toUpperCase() + al.substr(index + 1);
      }
      return null
    })
    setAlphabet(al);
  }, [guessed]);

  const sortAlphabets = (inp) => {
    return inp.sort().join('');
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
                    setAlphabet={setAlphabet}
                    setGuessed={setGuessed}
                  />
                </div>
                {
                  showCategory ?
                    <div>
                      <div>{target}</div>
                      <div>{alphabet}</div>
                      <div>Your chosen category is {category}</div>
                      <div>{dashes}</div>
                      <div>{message}</div>
                      <div>You have guessed {sortAlphabets(guessed)}</div>
                      <form action='/'>
                        <label htmlFor='letterInput'>Type a letter here:</label>
                        <input
                          id='letterInput'
                          maxLength='1'
                          size='1'
                          type='text'
                          defaultValue={inputValue}
                          onKeyUp={handleKeyUp}
                          onKeyDown={handleKeyDown} />
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