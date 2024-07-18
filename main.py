import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")
PASSWORD = os.getenv("PASSWORD")

import discord
from discord import app_commands
from discord.ext import commands
from embeds import *
import email.message

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix="!")

@bot.event
async def on_ready():
    print(f"{bot.user} is now online, ID: {bot.user.id}")
    
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as err:
        print(err)
        
@bot.tree.command(name="sendemail", description="Send a message to the receiver email")
@app_commands.describe(sender = "Valid sender gmail", receiver = "Valid receiver gmail/email", subject = "Subject of the message", body = "What simple message you gonna send")
async def sendemail(interaction: discord.Interaction, sender: str, receiver: str, subject: str, body: str):
    message = email.message.Message()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    message.set_payload(body)
    formatted_message = message.as_string()
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    
    embed = send_content_embed(sender=sender, receiver=receiver, subject=subject, body=body)
    try:
        server.login(user=sender, password=PASSWORD)
        print("Logged in...")
        server.sendmail(from_addr=sender, to_addrs=receiver, msg=formatted_message)
        print("Email has been sent")
    except smtplib.SMTPAuthenticationError:
        print("Need app password from your gmail account")
        
    await interaction.response.send_message(embed=embed)
    
bot.run(token=TOKEN)