import json
import asyncio
import aiohttp


class Swapper:
    def __init__(self, bearer, account_id):
        self.bearer = bearer
        self.account_id = account_id
        self.url = f"https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/" \
                   f"{self.account_id}/client/SetActiveHeroLoadout?profileId=campaign"
        self.headers = {
            "Authorization": f"Bearer {self.bearer}",
            "Content-Type": "application/json"
        }
        self.session = None

    async def swap(self, starting_sq: str, loadouts: list[str], swaps: int):
        async def send_request(session, body):
            async with session.post(self.url, headers=self.headers, data=json.dumps(body)):
                await asyncio.sleep(0.01)

        if self.session is None:
            connector = aiohttp.TCPConnector(limit=1000)
            self.session = aiohttp.ClientSession(connector=connector)

        tasks = []
        for i in range(swaps):
            for j, uuid in enumerate(loadouts):
                body = {"selectedLoadout": uuid}
                task = asyncio.create_task(send_request(self.session, body))
                tasks.append(task)
                if uuid == starting_sq and (i + 1) % len(loadouts) == 0:
                    break
        await asyncio.gather(*tasks)
        await self.close()

    async def close(self):
        if self.session is not None:
            await self.session.close()
            self.session = None
