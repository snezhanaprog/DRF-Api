import { useEffect, useState } from 'react'
import axios from 'axios'
const Home = () => {
    const [persons, setPersons] = useState([])


    let getData = async () => {
        let response = await axios.get("http://127.0.0.1:8000/persons/")
        console.log('RESPONSE:', response)
        setPersons(response.data)
    }

    useEffect(() => {
        getData()
    }, [])

    return (
        <div>
            <h1>Home page</h1>
            <div>
                {
                    persons.map((person, index) => (
                    <div key={index}>
                        <strong>{person.name}</strong>
                    </div>
                ))
                }
            </div>
        </div>
    )
}

export default Home