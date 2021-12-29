import axios from 'axios'


export const authAxios = axios.create({
    baseURL:"http://127.0.0.8000/api/",
    headers:{
        Authorization: `Token ${localStorage.getItem('token')}`
    }
});
