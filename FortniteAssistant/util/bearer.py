import aiohttp


class Bearer:
    def __init__(self, auth_code) -> None:
        self.auth_code = auth_code
        self.url = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token"
        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "basic ZWM2ODRiOGM2ODdmNDc5ZmFkZWEzY2IyYWQ4M2Y1YzY6ZTFmMzFjMjExZjI4NDEzMTg2MjYyZDM3YTEzZmM4NGQ="
        }
        self.body = {
            "grant_type": "authorization_code",
            "code": self.auth_code
        }

    async def get_bearer_token(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, headers=self.headers, data=self.body) as resp:
                response = await resp.json()
                return response
