export default function CarouselSlide({tierLevel, sendMEV, honeyCheck, leaderboard, monitor, tokenCheck, api, info, swapStats, honeyLogs}) {
    const renderText = (text, miss) => (
        <p className={!text ? "line-through text-red-600" : "text-green-400"}>
            {text || miss}
        </p>
    );
    
    return(
        <div className="flex flex-col gap-6 w-full">
            <div className="self-center font-bold text-xl">
                TIER {tierLevel}
            </div>
            <div>
                {renderText(sendMEV, "Send MEV Bundles")}
            </div>
            <div>
                <p>{renderText(honeyCheck, "Honeypots Checker")}</p>
            </div>
            <div>
                <p>{renderText(leaderboard, "Access To Leaderboard")}</p>
            </div>
            <div>
                <p>{renderText(monitor, "Bundles Monitor")}</p>
            </div>
            <div>
                <p>{renderText(tokenCheck, "Token Scanner")}</p>
            </div>
            <div>
                <p>{renderText(api, "API")}</p>
            </div>
            <div>
                <p>{renderText(info, "Detailed Information on Leaderboard")}</p>
            </div>
            <div>
                <p>{renderText(swapStats, "Victim Swap Stats")}</p>
            </div>
            <div>
                <p>{renderText(honeyLogs, "Honeypot Logs")}</p>
            </div>
        </div>
    )
}