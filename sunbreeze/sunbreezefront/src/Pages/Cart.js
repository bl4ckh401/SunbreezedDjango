import React from 'react'
import { useCart } from "use-cart";
import "../Components/cart.css"

function Cart() {
const { items, addItem, removeItem, removeLineItem, clearCart } = useCart()
    return (
            <div className="cart_main">
                {
                    items.map((item) => {
                        return(
                            <div className="cart_content">
                            <div className="cart_item_image">
                                <img src={item.imgurl} alt="img_product"></img>
                            </div>
                            <div className="product_desc">
                                <h3 className="">{item.name}</h3>
                                <h5 className="">{item.quantity}</h5>
                            </div>
                            <div className="btns_cart">
                                <button className="add_item" >+</button>
                                <button className="reduce_item" >-</button>
                                <button className="remove_item" >Remove Item</button>
                            </div>
                        </div>                        )
                    })
                }
                <div className="last_btn">
                <button onClick={clearCart}>Clear Cart</button>
                </div>
            </div>
    )
}

export default Cart
