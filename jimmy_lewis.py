# Import Discord.py commands
from discord.ext import commands

# Import discord-py-slash-commands slash commands
from discord_slash import SlashCommand, SlashContext

# Import config.py with the bot_token string
from config import bot_token

# Create the bot object and set the command prefix for any non-slash commands
bot = commands.Bot(command_prefix=".")

# Create the Slash Commands object and add the bot
slash = SlashCommand(bot, sync_commands=True)


# On ready event to run after the bot has started
@bot.event
async def on_ready():
    print("Jimmy Lewis is alive...")


# On message received event.
@bot.event
async def on_message(ctx):

    # Process all the commands first before reading the message
    await bot.process_commands(ctx)

    # If a bot sends a message disregard it.
    if ctx.author.bot:
        return

    """
    Every time Drake sends a message it will add the :drake: emoji
    Drake ID - 200391739113078785
    :drake: ID - <:drake:821463946284367902>
    """
    if ctx.author.id == 200391739113078785:
        drake_react = "<:drake:821463946284367902>"
        await ctx.add_reaction(drake_react)


# Slash Command to ping the bot
@slash.slash(name="ping", description="Check that the bot is connected and running.")
async def ping(ctx):
    await ctx.send(f"Pong! ({bot.latency*1000}ms)")


# Start the bot
bot.run(bot_token)
