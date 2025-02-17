import os

# Add your stuff here
API_KEY = os.getenv("API_KEY", "")
# Your Octopus Energy account number. Starts with A-
ACC_NUMBER = os.getenv("ACC_NUMBER", "")
BASE_URL = os.getenv("BASE_URL", "https://api.octopus.energy/v1")
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")
OCTOPUS_LOGIN_EMAIL = os.getenv("OCTOPUS_LOGIN_EMAIL", "")
OCTOPUS_LOGIN_PASSWD = os.getenv("OCTOPUS_LOGIN_PASSWD", "")
EXECUTION_TIME = os.getenv("EXECUTION_TIME", "23:00")

# Whether to just run immediately and exit
ONE_OFF_RUN = os.getenv("ONE_OFF", "false") in ["true", "True", "1"]
# Will only report the results and not change tarrif
DRY_RUN = os.getenv("DRY_RUN", "false") in ["true", "True", "1"]
