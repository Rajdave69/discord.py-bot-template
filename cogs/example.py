import discord
from discord.ext import commands
from discord import app_commands

from backend import log, embed_template, error_template


class Example(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Use @command.Cog.listener() for an event-listener (on_message, on_ready, etc.)
    @commands.Cog.listener()
    async def on_ready(self):
        log.info("Cog: Example.py Loaded")

    @app_commands.command(name="ping")
    async def ping(self, interaction):
        await interaction.followup.send("pong")

    
async def setup(client):
    # Here, `Example` is the name of the class
    await client.add_cog(Example(client))
