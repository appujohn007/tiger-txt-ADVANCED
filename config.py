import os

API_ID = 10471716

API_HASH = os.environ.get("API_HASH", "f8a1b21a13af154596e2ff5bed164860")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6916875347:AAEVxR4cO_sIBB6V57ANA92pHKxzw9G3yX0")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6883997969))

LOG = -1002161395379

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6883997969").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


