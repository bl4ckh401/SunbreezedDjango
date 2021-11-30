import React from 'react'
import { Link } from 'react-router-dom'
import headerData from '../Data/headerData'
import "./Footer.css"

function Footer() {
    return (
        <div className="FooterMain1">
            <div className="FooterMain">
            <section className="section" >
                <div className="all_menus">
                    <p className="heading">Quick links</p>
                    <div className="data">
                    {
                        headerData.map((item) => {
                            return(
                                <div className="menu_items" key={item.title}>
                                <Link to={item.path}>
                                <div className="menu_item">
                                <h3 className="menu_item" >{item.title}</h3>
                                </div>
                                </Link>

                              </div>   
                            )
                        })
                    }
                    </div>
                    </div>
                    <div className="get_intouch" >
                    <h1
                     className="heading">GET IN TOUCH</h1>
                    <div className="data2">
                        <p>Loren ipsum dolor sit amet, conect etur adipisching elit</p>
                    </div>
                    <div className="data2">
                        <p>+254 765 524 850</p>
                    </div>
                    <div className="data2">
                        <p>contact@example.com</p>
                    </div>                
                    </div>
            </section>
            <div className="copyrightMain">
            <div className="copyright">
                {//<AiOutlineCopyright className="copyright2" class="text-white"/>
                }
                <p className="copyright2" class="text-white">Copyright 2020. All right reserved</p>
            </div>
            </div>
        </div> 
        </div>
    )
}

export default Footer
