import asyncio
import json

from selenium.webdriver.common.by import By

from FortniteAssistant.savetheworld.swapper import Swapper
from FortniteAssistant.util.bearer import Bearer
from FortniteAssistant.util.squads import Squads
from FortniteAssistant.util.webdriver import Webdriver


async def main():
    try:
        driver = Webdriver(headless=True).create_webdriver()
    except Exception as ex:
        print(ex)
        print(
            "CANNOT CREATE A WEBDRIVER! Are you running the latest browser version? Check the configured browser for any updates!\nPress any key to exit...")
        input()
        exit()

    driver.get("https://www.epicgames.com/id/api/redirect?clientId=ec684b8c687f479fadea3cb2ad83f5c6&responseType=code")

    auth_code = json.loads(driver.find_elements(By.TAG_NAME, "body")[0].text)["authorizationCode"]

    bearer_data = await Bearer(auth_code).get_bearer_token()
    BEARER_TOKEN = bearer_data["access_token"]
    print(BEARER_TOKEN)
    ACCOUNT_ID = bearer_data["account_id"]

    starting_sq, squads = await Squads(BEARER_TOKEN, ACCOUNT_ID).get_squads_data()

    swaps = int(input("How many swaps: "))

    await Swapper(BEARER_TOKEN, ACCOUNT_ID).swap(starting_sq, squads, swaps)


if __name__ == "__main__":
    asyncio.run(main())
