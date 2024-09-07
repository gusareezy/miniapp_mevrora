import { useState, useEffect } from "react";
import HomeTransaction from "../components/HomeTransaction"

export default function Homepage() {
    const [data, setData] = useState([]); 
    const [error, setError] = useState(null); 

    const fetchData = async () => {
        try {
                const response = await fetch('http://localhost:5000/get_transactions'); 
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const result = await response.json();
                setData(result);
            } catch (error) {
            setError(error.message); 
        }
    };

    useEffect(() => {
        fetchData();

        const interval = setInterval(() => {
            fetchData();
        }, 10000);

        return () => clearInterval(interval);
    }, []);

    
    return (
        <div className="flex grow flex-col gap-10">
            {data.map((item) => (
                <div>
                    <HomeTransaction address="123" victim="123" value="123" pnl={item.backrunValue} />
                </div>
            ))}
        </div>
    )
}