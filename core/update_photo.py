from utils.config import log
from utils.csv_manager import CSVInstructionManager
from utils.slack_connector import SlackConnectionManager


async def update_user_photo_processor(
    slack_data_manager: SlackConnectionManager,
    instructions: CSVInstructionManager,
):

    for csv_entry in instructions.yield_assign_photo_instructions():
        log.info(f"Working on {csv_entry.user_email}")
        try:
            user = await slack_data_manager.search_user(csv_entry.user_email)
        except ValueError as e:
            log.exception(f"Failed to search user '{csv_entry.user_email}': {e}")
            continue
        except Exception:
            log.exception(f"Failed to search user '{csv_entry.user_email}'")
            continue

        if not user:
            log.error(f"User '{csv_entry.user_email}' not found in Slack")
            continue

        try:
            await slack_data_manager.update_photo(
                user_id=user["id"],
                photo_url=csv_entry.photo_url,
            )
        except Exception as e:
            log.exception(
                f"Failed to update photo for user '{csv_entry.user_email}': {e}"
            )
