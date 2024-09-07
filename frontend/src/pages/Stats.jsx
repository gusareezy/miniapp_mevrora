import UserStats from "../components/UserStats"
import { useInitData } from "@telegram-apps/sdk-react"

export default function Stats() {
    const initData = useInitData()
    return(
        <div className="flex flex-col gap-4 px-10 justify-between">
            <UserStats user={`${initData.user.firstName}`} address="123" balance="123" pnl="123" value="213" sent="213" approved="123"/>
        </div>
    )
}