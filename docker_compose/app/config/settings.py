from split_settings.tools import include


base_settings = [
    "components/common.py",
    "components/database.py",
    "components/logging.py"
]

include(*base_settings)
