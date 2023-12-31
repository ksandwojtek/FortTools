import json

import aiohttp


class Squads:
    def __init__(self, bearer, account_id) -> None:
        self.bearer = bearer
        self.account_id = account_id
        self.url = f"https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/" \
                   f"{self.account_id}/client/QueryProfile?profileId=campaign"
        self.headers = {
            "Authorization": f"Bearer {self.bearer}",
            "Content-Type": "application/json"
        }
        self.body = "{}"

    async def get_squads_data(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, headers=self.headers, data=self.body) as resp:
                response = await resp.json()
                profile = response["profileChanges"][0]["profile"]
                with open("data.json", "w") as f:
                    f.write(json.dumps(profile["items"]))
                return self.get_grandparent_keys(profile["items"],
                                                 profile["stats"]["attributes"]["selected_hero_loadout"],
                                                 "loadout_index")

    def get_grandparent_keys(self, json_dict, curr, selected_key):
        grandparent_keys = []

        def find_grandparent_keys(json_obj, parent_key='', grandparent_key=''):
            if isinstance(json_obj, dict):
                for key, value in json_obj.items():
                    if key == selected_key:
                        grandparent_keys.append(grandparent_key)
                    find_grandparent_keys(value, key, parent_key)
            elif isinstance(json_obj, list):
                for item in json_obj:
                    find_grandparent_keys(item, parent_key, grandparent_key)

        find_grandparent_keys(json_dict)
        return curr, grandparent_keys
