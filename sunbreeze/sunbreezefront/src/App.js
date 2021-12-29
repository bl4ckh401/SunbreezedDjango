import './App.css';
import React, {useEffect, useState} from 'react'
import Footer from './Components/Footer';
import Header from './Components/Header';
import Home from './Pages/Home';
import { BrowserRouter as Router, Switch, Route, Redirect} from "react-router-dom";
import Cart from './Pages/Cart';
import Login from './Pages/login';

function App() {

  const [isLoggedIn, setIsLoggedIn] = useState(false)

  useEffect(() => {
    try {
      if(localStorage.getItem('token') !== null ){
       // history.push("/products")
       setIsLoggedIn(true)
      }
      else{
        //window.location.replace("http://127.0.0.1:3000/Login")
        setIsLoggedIn(false)
        console.log("Token doesn't exist")
      }
    } catch (error) {
      console.log(error)
    }
  }, [])

  return (
    <div className="App">
      <Router>
        <Header />
        {
          isLoggedIn ?
          <Redirect to="/products"/>
          :
          <Redirect to="/products"/>
        }
          <Switch>
          <Route path="/login" component={ Login } />

          </Switch>
        <Footer />
      </Router>
    </div>
  );
}

export default App;
