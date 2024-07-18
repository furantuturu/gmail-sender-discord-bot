import discord

def send_content_embed(*, sender, receiver, subject, body):
    embed = discord.Embed(colour=discord.Colour.green(), title="Email has been sent!")
    
    embed.set_thumbnail(url="https://i.ibb.co/sJQk5qJ/mailapp.jpg")
    embed.add_field(
        name="From:",
        value=sender,
    )
    embed.add_field(
        name="To:",
        value=receiver,
        inline=False
    )
    embed.add_field(
        name="Subject:",
        value=subject,
        inline=False
    )
    embed.add_field(
        name="Message body:",
        value=body,
        inline=False   
    )
    
    return embed

def err_embed():
    embed = discord.Embed(colour=discord.Colour.red(), title="Unable to sent the message")

    return embed