import React from 'react'
import "../Components/cart.css"
import CSRFToken from '../Components/CSRFToken';

function Cart() {
    return (
            <div className="cart_main">
                <CSRFToken />
                        return(
                            <div className="cart_content">
                            <div className="cart_item_image">
                                <img src=""alt="img_product"></img>
                            </div>
                            <div className="product_desc">
                                <h3 className="">Cart Item</h3>
                                <h5 className="">7</h5>
                            </div>
                            <div className="btns_cart">
                                <button className="add_item" >+</button>
                                <button className="reduce_item" >-</button>
                                <button className="remove_item" >Remove Item</button>
                            </div>
                        </div>                        )
                <div className="last_btn">
                <button onClick="">Clear Cart</button>
                </div>
            </div>
    )
}

export default Cart
