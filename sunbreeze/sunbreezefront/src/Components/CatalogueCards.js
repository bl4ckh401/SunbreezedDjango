import React, {useEffect, useState} from 'react'
import "./Home.css"
import { authAxios } from '../utils';

function CatalogueCards() {
    const [data, setData] = useState([ ]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    const handleCart = slug =>{
        try {
            authAxios.post("http://127.0.0.1:8000/api/cart/", {slug})
            .then((response) => response.send(response.data))
            .then(console.log(data))
        } catch (error) {
            //console.log(error)5
        }
    }

    useEffect(() => {

            const RequestData = {
                method:"GET",
                headers: { 'Content-Type': "application/json"},
            }
            setLoading(true)
            fetch("http://127.0.0.1:8000/api/product/", RequestData)
            .then((data) => data.json()
            )
            .then((data) => {
                console.log(data)
                setData(
                    data
                )
                setLoading(false);
            })
     
    }, [])

    return (
        <div>
            {error}
            {
                loading ? 
                <h1>Loading</h1> : 
                    data.map((item) => {
                        return(
                        <div className="catalogue_card" key={item.id}>
                            <div className="catalogue_org">
                                            <div className="catalogue_main">
                                                <div className="catalogue_img">
                                                    <img className="catalogue_img" src={item.image} alt="JackDaniels" ></img>
                                                </div>
                                                <div className="item_desc">
                                                <div className="item_div">
                                                    <h3 className="item_name">Name: {item.title}</h3>
                                                </div>
                                                <div className="item_div">
                                                    <h3 className="item_name">Price: {item.price}</h3>
                                                </div>
                                                <div className="item_div">
                                                    <h3 className="item_name">In-Stock: {item.description}</h3>
                                                </div>
                                                <div className="item_button">
                                                <button className="add_to_cart" data={item.id} action="add" onClick={() =>handleCart(item.slug)}>Add To Cart</button>
                                                </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                )
                            })
                        }
                </div>
    )
}

export default CatalogueCards
