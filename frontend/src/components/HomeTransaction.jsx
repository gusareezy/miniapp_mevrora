import "./comp.css"
import { useState } from "react";

export default function HomeTransaction({address, victim, hash, value, pnl}) {
    const [expanded, setExpanded] = useState(false);

    const toggleExpand = () => {
        setExpanded(!expanded);
    };

    return (
        <div className={`flex justify-between items-center px-6 bg-[#111111] rounded-xl py-4 mx-2 ${expanded ? 'h-50' : 'h-35'}`}
            onClick={toggleExpand}>
            <div className="flex flex-col gap-4 justify-between items-center">
                <p className="address">Address: <a href={`https://etherscan.io/address/${address}`} target="_blank">{address}</a></p>
                <p className="address">Victim: <a href={`https://etherscan.io/address/${victim}`} target="_blank">{victim}</a></p>
                {expanded && (
                    <p className="address">
                        Tx Hash: <a href={`https://etherscan.io/tx/${hash}`} target="_blank" rel="noopener noreferrer">{hash}</a>
                    </p>
                )}
                {/* <p className={`address ${expanded ? 'inline-block' : 'hidden'}`}>Tx Hash: <a href={`https://etherscan.io/tx/${hash}`} target="_blank">{hash}</a></p> */}
            </div>

            <div className="flex flex-col gap-4 justify-between items-center">
                <p>Value: {value} Ξ</p>
                <p>PNL: {pnl}$</p>
            </div>
        </div>
    )
}