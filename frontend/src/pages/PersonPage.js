import React, {useEffect} from 'react'
import { useParams } from 'react-router-dom'
import axios from "axios";
const PersonPage = () => {
    const params = useParams()
    const name = params.name


    return (
        <div>
            <h1>Person page {name} </h1>
        </div>
    )
}

export default PersonPage