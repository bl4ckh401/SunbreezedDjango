import React, {useState} from 'react'
import { Redirect } from 'react-router-dom';


function Login() {

    const [userName, setuserName] = useState("")
    const [password, setpassWord] = useState("")
    const [isLoggedIn, setIsLoggedIn] = useState("")

    const handleLogin = (event) =>{
        event.preventDefault();
        const RequestData = {
            method:"POST",
            headers: { 'Content-Type': "application/json"},
            body: JSON.stringify({
                    username : userName,
                    password : password
            })
        }
        fetch('http://127.0.0.1:8000/api/token-auth/', RequestData)
        .then(response => response.json())
        .then((response) => {
            localStorage.setItem('token', response.token);
            console.log(response)

        })
        setIsLoggedIn(true);
        console.log(isLoggedIn)
        }

    const handleLogout = () => {
        localStorage.removeItem('token');
        setIsLoggedIn(false)
        Redirect('/Login')
    };
    console.log(isLoggedIn)


    const handleChangeUserName = (event) =>{
        event.preventDefault();
        setuserName(event.target.value)
        console.log(userName)
    }

    const handleChangePassword = (event) =>{
        event.preventDefault();
        setpassWord(event.target.value)
        console.log(password)
    }
    return (
        <div>
            <div>
                <input type="text" placeholder='username' name="username" onChange={ handleChangeUserName }></input><br />
                <input type="password" placeholder='password' name="password" onChange={ handleChangePassword }></input><br />
                <button type="submit" onClick={handleLogin}>Login</button>
                <button type="submit" onClick={handleLogout}>Log Out</button>
            </div>
        </div>
    )
}

export default Login
