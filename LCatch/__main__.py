from LCatch import *
import importlib
import logging
from LCatch.modules import ALL_MODULES


def main() -> None:
    for module_name in ALL_MODULES:
        imported_module = importlib.import_module("LCatch.modules." + module_name)
    LOGGER("LCatch.modules").info("Aʟʟ ғᴇᴀᴛᴜʀᴇs ᴀʀᴇ ʟᴏᴀᴅᴇᴅ ᴅᴇᴀʀ sʜᴀᴅᴏᴡ🥂🤭🥀...")

    LC.start()
    application.run_polling(drop_pending_updates=True)
    LOGGER("LCatch").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ☠︎︎MADE BY LCatch☠︎︎\n╚═════ஜ۩۞۩ஜ════╝"
    )
    send_start_message()
    

if __name__ == "__main__":
    main()
    
    
