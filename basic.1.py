
from mctools import RCONClient  # Import the RCONClient
import sys

HOST = '192.168.0.199'  # Haryun's world. Experiment world
#HOST = 'localhost'  # this computer
PORT = 25575    # Port number of the RCON server
PASSWORD = "password"    # password we set like "rcon.password={password}" in server.properties file 

# Create the RbCONClient:
rcon = RCONClient(HOST, port=PORT)

# Login to RCON:
if not rcon.login(PASSWORD):
    print('wrong password')
    sys.exit()

# Send command to RCON - broadcast message to all players:
# https://www.pcgamesn.com/minecraft/minecraft-console-commands-and-cheats
# https://minecraft.gamepedia.com/Commands/teleport
rconcommand = "broadcast Hello RCON!"
rconcommand = "help"
rconcommand = "help teleport"
rconcommand = "help weather"
rconcommand = "weather thunder 30"  # 30 = 30 seconds
rconcommand = "weather rain 30"  
# rconcommand = "weather snow 30" 
rconcommand = "weather clear"  
rconcommand = "time set 18000" # set the time to midnight
rconcommand = "time set 0" # set the time to dawn
rconcommand = "gamemode creative"
rconcommand = "gamemode survival"
rconcommand = "gamerule doDaylightCycle false" # the sun stops moving 
rconcommand = "gamerule doDaylightCycle true" # the sun starts moving 
rconcommand = "op Danjang403"   # made Danjang403 a server operator. don't need Danjang403 being logged in
rconcommand = "gamemode creative Danjang403"
# rconcommand = "summon spider 222 100 222" # 222 100 222 = tower coordinates of our initial position
# # /tp 222 100 222  transport to just above the base camp in the test server (199)
# rconcommand = "fill 222 120 222 242 120 242 minecraft:gold_block replace" 
# rconcommand = "fill 222 120 222 242 120 242 air replace" 
# # /tp 205 125 -218  transport to East construction field, just above Ryan statue head 
# rconcommand = "fill 205 150 -218 205 150 -218 minecraft:gold_block replace" 
# rconcommand = "broadcast Hello RCON!"
rconcommand = "teleport Dain503 0 10 -1000"
# rconcommand = "difficulty easy" # peaceful(mobs will disappear instantly), easy, normal, and hard
# rconcommand = "locate village"  # https://minecraft.gamepedia.com/Commands/locate   for building type
# rconcommand = "locate desert_pyramid" 
# rconcommand = "locatebiome river"  # https://minecraft.gamepedia.com/Biome/ID
# rconcommand = "tell Dain503 안녕"　　＃ whisper to single player
# rconcommand = "team add engteam" # creating team. we can change the chat color and some properties
# rconcommand = "team join engteam Dain503" 
# rconcommand = "team list engteam" 
rconcommand = "data get block 4 4 77"
    # sign : 4, 4, 77 has the following block data: {Color: "black", x: 4, Text4: '{"text":""}', y: 4, Text3: '{"text":""}', z: 77, Text2: '{"text":""}', id: "minecraft:sign", Text1: '{"text":"aa"}'}
rconcommand = "data get entity @e[limit=1, nbt={TileX:4,TileY:4,TileZ:77}]"
# rconcommand = "data get block 5 4 77"
# rconcommand = "execute as Danjang403 at @s run execute as @e[type=armor_stand,distance=..10] run data get entity @s Pos"

#
rcon.stop()


