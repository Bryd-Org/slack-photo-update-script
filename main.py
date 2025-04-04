import asyncio

import typer

from core.update_photo import update_user_photo_processor
from utils.config import settings as s, log
from utils.csv_manager import CSVInstructionManager
from utils.slack_connector import SlackConnectionManager

app = typer.Typer()


@app.command(name="update-user-photos")
def change_user_emails():
    slack_data_manager = SlackConnectionManager(s.SLACK_USER_TOKEN)
    instructions = CSVInstructionManager(
        filename="instructions/update_user_photos.csv",
    )

    asyncio.run(
        update_user_photo_processor(
            slack_data_manager=slack_data_manager,
            instructions=instructions,
        )
    )


async def selftest():
    log.info("Script self test is working. Sleeping 5 seconds")
    await asyncio.sleep(5)
    log.info("Script self test finished")


@app.command(name="test")
def container_test():
    instructions_files = [
        "instructions/update_user_photos.csv",
    ]

    for instruction in instructions_files:
        try:
            f = open(instruction)
            f.close()
            log.info(f"File '{instruction}' found")
        except FileNotFoundError:
            log.error(f"File '{instruction}' not found!")

    asyncio.run(selftest())


if __name__ == "__main__":
    log.info("Script starting")
    app()
