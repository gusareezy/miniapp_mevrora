import { Carousel, 
    CarouselContent,
    CarouselItem,
    CarouselNext,
    CarouselPrevious } from "../components/Carousel"
import { Card, CardContent } from "../components/Card"
import CarouselSlide from "../components/CarouselSlide"

export default function Tiers() {
    const tiers = [
      <CarouselSlide tierLevel="0" sendMEV="Send MEV Bundles" honeyCheck="Honeypots Checker" leaderboard="Access To Leaderboard" monitor="Bundles Monitor" tokenCheck="Token Scanner" />,
      <CarouselSlide tierLevel="1" sendMEV="Send MEV Bundles" honeyCheck="Honeypots Checker" leaderboard="Access To Leaderboard" monitor="Bundles Monitor" tokenCheck="Token Scanner" api="API" info="Detailed Information on Leaderboard" />,
      <CarouselSlide tierLevel="2" sendMEV="Send MEV Bundles" honeyCheck="Honeypots Checker" leaderboard="Access To Leaderboard" monitor="Bundles Monitor" tokenCheck="Token Scanner" api="API" info="Detailed Information on Leaderboard" swapStats="Victim Swap Stats" />,
      <CarouselSlide tierLevel="3" sendMEV="Send MEV Bundles" honeyCheck="Honeypots Checker" leaderboard="Access To Leaderboard" monitor="Bundles Monitor" tokenCheck="Token Scanner" api="API" info="Detailed Information on Leaderboard" swapStats="Victim Swap Stats" honeyLogs="Honeypot Logs"/>
    ]

    return (
        <Carousel className="w-full max-w-xs mx-auto">
          <CarouselContent>
            {tiers.map((item, index) => (
              <CarouselItem key={index}>
                <div className="p-1">
                  <Card>
                    <CardContent className="flex aspect-square items-center justify-center p-6">
                      {item}
                    </CardContent>
                  </Card>
                </div>
              </CarouselItem>
            ))}
          </CarouselContent>
        </Carousel>
      )
}