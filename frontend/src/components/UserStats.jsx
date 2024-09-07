export default function UserStats({user, address, balance, pnl, value, sent, approved}) {
    return(
        <div className="flex flex-col gap-6 w-full justify-between">
            <div>
                <p>You: {user}</p>
            </div>
            <div>
                <p>Wallet address: {address}</p>
            </div>
            <div>
                <p>Wallet balance: {balance}</p>
            </div>
            <div>
                <p>Average PNL: {pnl}</p>
            </div>
            <div>
                <p>Average value: {value}</p>
            </div>
            <div>
                <p>Bundles sent: {sent}</p>
            </div>
            <div>
                <p>Bunldes approved: {approved}</p>
            </div>
        </div>
    )
}