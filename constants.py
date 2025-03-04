import os
import json
import random

# Pokèmon
SAFARI = set([
    "",
])

NEST_BALL = set([
    "",
])

REPEAT_BALL = set([
 "Venusaur", "Charizard", "Blastoise", "Beedrill", "Alakazam", "Slowbro",
 "Mewtwo", "Aerodactyl", "Ampharos", "Steelix", "Scizor",
 "Sceptile", "Blaziken", "Swampert", "Gardevoir", "Sableye", "Mawile",
 "Aggron", "Medicham", "Manectric", "Sharpedo", "Camerupt", "Altaria", "Banette", "Absol", "Glalie",
 "Metagross", "Lucario", "Abomasnow", "Gallade", "Audino",
 "Blacephalon", "Buzzwole", "Cobalion", "Cosmog", "Cosmoem", "Deoxys", "Diancie", "Dialga", 
 "Eternatus", "Genesect", "Giratina", "Glastrier", "Groudon", "Ho-oh", "Hoopa", "Jirachi", 
 "Kartana", "Keldeo", "Kubfu", "Kyogre", "Kyurem", "Landorus", "Lugia", "Magearna", "Marshadow", 
 "Mewtwo", "Necrozma", "Palkia", "Pheromosa", "Rayquaza", "Regieleki", "Regigigas", "Reshiram", 
 "Shaymin", "Spectrier", "Terrakion", "Victini", "Virizion", "Xerneas", "Yveltal", "Zacian", 
 "Zamazenta", "Zekrom", "Zeraora", "Zygarde"
])

ULTRA_BALL = set([
 "",
])

GREAT_BALL = set([
 "",
])

REGULAR_BALL = set([
 "",
])

# owner username and bot version 
OWNER_NAME = "Ace"
BOT_VERSION = "1.0"

# Commands
PING_COMMAND_REGEX = r'^\.ping$'
ALIVE_COMMAND_REGEX = r'^\.alive$'
HELP_COMMAND_REGEX = r'^\.help$'
EVAL_COMMAND_REGEX = r'^\.eval (.+)'
GUESSER_COMMAND_REGEX = r'^\.guess (on|off|stats)$'
HUNTER_COMMAND_REGEX = r'^\.hunt (on|off|stats)$'

# AFK Commands
AFK_COMMAND_REGEX = r'^\.afk(?: |$)(.*)'  # Matches `.afk` or `.afk <message>`
UNAFK_COMMAND_REGEX = r'^\.unafk$'  # Matches `.unafk`

COOLDOWN = lambda: random.randint(3, 6)
PERIODICALLY_GUESS_SECONDS = 120
PERIODICALLY_HUNT_SECONDS = 300
HEXA_BOT_ID = 572621020

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
SESSION = os.getenv('SESSION')

CHAT_ID = int(os.getenv('CHAT_ID'))

with open('pokemon.json', 'r') as f:
    POKEMON = json.load(f)

__version__ = '1.0.0'
