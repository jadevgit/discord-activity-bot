import discord
from discord.ext import commands
from datetime import datetime
from zoneinfo import ZoneInfo

# Time format
def getTime():
    return datetime.now(ZoneInfo("Europe/London"))
def format_seconds_to_hms(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h}:{m}:{s}"

class Client(commands.Bot):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")




intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

GUILD_ID = discord.Object(id=849185187262889985)




class ShiftView(discord.ui.View):
    @discord.ui.button(label="Start Shift", style=discord.ButtonStyle.green)
    async def shiftStart_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        
        # Send the message with the current time whether the user has clocked in or out
        await button.response.send_message(f"You have clocked on at **[{datetime.now(ZoneInfo('Europe/London')).strftime('%H:%M:%S')}]**.")
        global timeOn 
        timeOn = getTime()
    @discord.ui.button(label="End Shift",style=discord.ButtonStyle.red )
    async def shiftEnd_callback(self,button:discord.ui.button, interaction: discord.Interaction):
        timeOff = getTime()
        CHANNEL_ID = 1371883132340670474
        channel = client.get_channel(CHANNEL_ID)
        user = button.user
        
        diff = timeOff-timeOn


        await button.response.send_message(f"You have clocked out at **[{datetime.now(ZoneInfo('Europe/London')).strftime('%H:%M:%S')}]**.")
        await channel.send(f"{user} has spent spent {format_seconds_to_hms(int(diff.total_seconds()))} on duty. (H:M:S)")

# /shift command with embed and attached button
@client.tree.command(name="shift", description="Use this command to manage being clocked into the game.", guild=GUILD_ID)
async def shift(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Manage your shift", 
        url="https://www.roblox.com/games/82864632268577/Alpine-Border-Coastal-Castle", 
        description="", 
        colour=discord.Colour.dark_green()
    )
    embed.set_thumbnail(url="https://tr.rbxcdn.com/180DAY-3cc4aea963906cced4c5cf4c8e6a6ad4/150/150/Image/Webp/noFilter")
    embed.add_field(name="Clock On", value="You must press the \"Clock On\" button to clock in.", inline=False)
    embed.add_field(name="Clock Off", value="You must press the \"Clock Off\" button to clock out.", inline=False)
    embed.set_footer(text="DEV BUILD DEV BUILD DEV BUILD")
    embed.set_author(name=interaction.user.name, icon_url="https://tr.rbxcdn.com/180DAY-ba170723373bd8c557e278ebe3f33322/150/150/Image/Webp/noFilter")

    # Send the embed with the button attached
    await interaction.response.send_message(embed=embed, view=ShiftView())

client.run('api_key')


