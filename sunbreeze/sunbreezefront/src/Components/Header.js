import React from 'react'
import headerData from '../Data/headerData'
import "./header.css"
import { Link } from "react-router-dom";

function Header() {

    const handleLogout = () => {
        localStorage.removeItem('token');
    };
    return (
            <div  className="header_Top">
            <div className="header_place">
            <div class="flex flex-col items-center ml-40" className="header_Logo">
            </div>
            <div class="flex ml-64" className="menu_Items">
            { headerData.map((item) =>{
                return(
              <div className="menu_Item" key={item.title}>
           <Link to={item.path}>
               <div>
                <h3 className="menu_item">{item.title}</h3>
                </div>
           </Link>
             </div>
            )
            })
            } 

            <button className="button">CALL NOW</button>   
            <button className="button" onClick={handleLogout}>Log Out</button>          
       
            </div>
           </div>
        </div>
    )
}

export default Header
