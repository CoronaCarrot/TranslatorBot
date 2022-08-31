# -----------------------------------------------------------
# a simple discord translation bot
# using the DeepL API
#
# (C) 2021 CoronaCarrot
# Released under GNU Public License (GPL)
# email wae375@outlook.com
# -----------------------------------------------------------


from distutils.command.config import config
import discord
import requests
import demoji
from discord.ext import commands
from requests.structures import CaseInsensitiveDict
import os
import json


# checks if config file exists and is configured
if not os.path.isfile("config.json"):
    print("config.json not found... creating file.\nPlease configure it and restart the bot.")
    with open("config.json", "w") as f:
        f.write('{\n\t"token": "TOKEN",\n\t"DeepL_Auth_Key": "AUTHKEY"\n}')
    exit()
else:
    config = json.load(open("config.json"))
    # if token is not set in config file, exit
    if config["token"] == "TOKEN":
        print("token not set in config file... exiting.")
        exit()
    # if DeepL_Auth_Key is not set in config file, exit
    if config["DeepL_Auth_Key"] == "AUTHKEY":
        print("DeepL_Auth_Key not set in config file... exiting.")
        exit()


# define bot intents
intents = discord.Intents.all()


bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


# check for 🏴󠁧󠁢󠁥󠁮󠁧󠁿 flag emoji being added to reaction
@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    # bulgarian flag emoji
    if payload.emoji.name == "🇧🇬":
        # checks if the message was not sent by a bot
        if not payload.member.bot:
            # remove the reaction
            await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
            # get message content
            message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

            url = "https://api-free.deepl.com/v2/translate"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=BG"

            resp = requests.post(url, headers=headers, data=data)

            # translated message embed
            embed = discord.Embed(title="Translated message", description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
            embed.set_footer(text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ BG", icon_url=payload.member.display_avatar)
            await message.reply(embed=embed, mention_author=False)
    # Czech flag emoji
    elif payload.emoji.name == "🇨🇿":
        # checks if the message was not sent by a bot
        if not payload.member.bot:
            # remove the reaction
            await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
            # get message content
            message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

            url = "https://api-free.deepl.com/v2/translate"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=CS"

            resp = requests.post(url, headers=headers, data=data)

            # translated message embed
            embed = discord.Embed(title="Translated message",
                                    description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
            embed.set_footer(
                text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ CS",
                icon_url=payload.member.display_avatar)
            await message.reply(embed=embed, mention_author=False)
    # Danish flag emoji
    elif payload.emoji.name == "🇩🇰":
        # checks if the message was not sent by a bot
        if not payload.member.bot:
            # remove the reaction
            await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
            # get message content
            message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

            url = "https://api-free.deepl.com/v2/translate"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=DA"

            resp = requests.post(url, headers=headers, data=data)

            # translated message embed
            embed = discord.Embed(title="Translated message",
                                    description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
            embed.set_footer(
                text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ DA",
                icon_url=payload.member.display_avatar)
            await message.reply(embed=embed, mention_author=False)
    # German flag emoji
    elif payload.emoji.name == "🇩🇪":
        # checks if the message was not sent by a bot
        if not payload.member.bot:
            # remove the reaction
            await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
            # get message content
            message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

            url = "https://api-free.deepl.com/v2/translate"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=DE"

            resp = requests.post(url, headers=headers, data=data)

            # translated message embed
            embed = discord.Embed(title="Translated message",
                                    description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
            embed.set_footer(
                text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ DE",
                icon_url=payload.member.display_avatar)
            await message.reply(embed=embed, mention_author=False)
    # greek flag emoji
    elif payload.emoji.name == "🇬🇷":
        # checks if the message was not sent by a bot
        if not payload.member.bot:
            # remove the reaction
            await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
            # get message content
            message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

            url = "https://api-free.deepl.com/v2/translate"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=EL"

            resp = requests.post(url, headers=headers, data=data)

            # translated message embed
            embed = discord.Embed(title="Translated message",
                                    description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
            embed.set_footer(
                text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ EL",
                icon_url=payload.member.display_avatar)
            await message.reply(embed=embed, mention_author=False)
    # english flag emoji
    elif payload.emoji.name == "🇬🇧":
        # checks if the message was not sent by a bot
        if not payload.member.bot:
            # remove the reaction
            await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
            # get message content
            message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

            url = "https://api-free.deepl.com/v2/translate"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=EN"

            resp = requests.post(url, headers=headers, data=data)

            # translated message embed
            embed = discord.Embed(title="Translated message",
                                    description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
            embed.set_footer(
                text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ EN",
                icon_url=payload.member.display_avatar)
            await message.reply(embed=embed, mention_author=False)
    # spanish flag emoji
    elif payload.emoji.name == "🇪🇸":
        # checks if the message was not sent by a bot
        if not payload.member.bot:
            # remove the reaction
            await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
            # get message content
            message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

            url = "https://api-free.deepl.com/v2/translate"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=ES"

            resp = requests.post(url, headers=headers, data=data)

            # translated message embed
            embed = discord.Embed(title="Translated message",
                                    description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
            embed.set_footer(
                text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ ES",
                icon_url=payload.member.display_avatar)
            await message.reply(embed=embed, mention_author=False)
    # estonian flag emoji
    elif payload.emoji.name == "🇪🇪":
        # checks if the message was not sent by a bot
        if not payload.member.bot:
            # remove the reaction
            await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
            # get message content
            message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

            url = "https://api-free.deepl.com/v2/translate"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=ET"

            resp = requests.post(url, headers=headers, data=data)

            # translated message embed
            embed = discord.Embed(title="Translated message",
                                    description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
            embed.set_footer(
                text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ ET",
                icon_url=payload.member.display_avatar)
            await message.reply(embed=embed, mention_author=False)
    # finnish flag emoji
    elif payload.emoji.name == "🇫🇮":
        # checks if the message was not sent by a bot
            if not payload.member.bot:
                # remove the reaction
                await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
                # get message content
                message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

                url = "https://api-free.deepl.com/v2/translate"

                headers = CaseInsensitiveDict()
                headers["Content-Type"] = "application/x-www-form-urlencoded"

                data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=FI"

                resp = requests.post(url, headers=headers, data=data)

                # translated message embed
                embed = discord.Embed(title="Translated message",
                                        description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
                embed.set_footer(
                    text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ FI",
                    icon_url=payload.member.display_avatar)
                await message.reply(embed=embed, mention_author=False)
    # french flag emoji
    elif payload.emoji.name == "🇫🇷":
        # checks if the message was not sent by a bot
        if not payload.member.bot:
            # remove the reaction
            await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
            # get message content
            message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

            url = "https://api-free.deepl.com/v2/translate"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=FR"

            resp = requests.post(url, headers=headers, data=data)

            # translated message embed
            embed = discord.Embed(title="Translated message",
                                    description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
            embed.set_footer(
                text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ FR",
                icon_url=payload.member.display_avatar)
            await message.reply(embed=embed, mention_author=False)
    # hungarian flag emoji
    elif payload.emoji.name == "🇭🇺":
        # checks if the message was not sent by a bot
        if not payload.member.bot:
            # remove the reaction
            await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
            # get message content
            message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

            url = "https://api-free.deepl.com/v2/translate"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=HU"

            resp = requests.post(url, headers=headers, data=data)

            # translated message embed
            embed = discord.Embed(title="Translated message",
                                    description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
            embed.set_footer(
                text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ HU",
                icon_url=payload.member.display_avatar)
            await message.reply(embed=embed, mention_author=False)
    # italian flag emoji
    elif payload.emoji.name == "🇮🇹":
        # checks if the message was not sent by a bot
        if not payload.member.bot:
            # remove the reaction
            await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
            # get message content
            message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

            url = "https://api-free.deepl.com/v2/translate"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=IT"

            resp = requests.post(url, headers=headers, data=data)

            # translated message embed
            embed = discord.Embed(title="Translated message",
                                    description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
            embed.set_footer(
                text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ IT",
                icon_url=payload.member.display_avatar)
            await message.reply(embed=embed, mention_author=False)
    # japanese flag emoji
    elif payload.emoji.name == "🇯🇵":
        # checks if the message was not sent by a bot
        if not payload.member.bot:
            # remove the reaction
            await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
            # get message content
            message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

            url = "https://api-free.deepl.com/v2/translate"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=JA"

            resp = requests.post(url, headers=headers, data=data)

            # translated message embed
            embed = discord.Embed(title="Translated message",
                                    description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
            embed.set_footer(
                text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ JA",
                icon_url=payload.member.display_avatar)
            await message.reply(embed=embed, mention_author=False)
    # lithuanian flag emoji
    elif payload.emoji.name == "🇱🇹":
        # checks if the message was not sent by a bot
        if not payload.member.bot:
            # remove the reaction
            await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
            # get message content
            message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

            url = "https://api-free.deepl.com/v2/translate"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=LT"

            resp = requests.post(url, headers=headers, data=data)

            # translated message embed
            embed = discord.Embed(title="Translated message",
                                    description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
            embed.set_footer(
                text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ LT",
                icon_url=payload.member.display_avatar)
            await message.reply(embed=embed, mention_author=False)
    # latvian flag emoji
    elif payload.emoji.name == "🇱🇻":
        # checks if the message was not sent by a bot
        if not payload.member.bot:
            # remove the reaction
            await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
            # get message content
            message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

            url = "https://api-free.deepl.com/v2/translate"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=LV"

            resp = requests.post(url, headers=headers, data=data)

            # translated message embed
            embed = discord.Embed(title="Translated message",
                                    description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
            embed.set_footer(
                text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ LV",
                icon_url=payload.member.display_avatar)
            await message.reply(embed=embed, mention_author=False)
    # dutch flag emoji
    elif payload.emoji.name == "🇳🇱":
        # checks if the message was not sent by a bot
        if not payload.member.bot:
            # remove the reaction
            await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
            # get message content
            message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

            url = "https://api-free.deepl.com/v2/translate"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=NL"

            resp = requests.post(url, headers=headers, data=data)

            # translated message embed
            embed = discord.Embed(title="Translated message",
                                    description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
            embed.set_footer(
                text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ NL",
                icon_url=payload.member.display_avatar)
            await message.reply(embed=embed, mention_author=False)
    # polish flag emoji
    elif payload.emoji.name == "🇵🇱":
        # checks if the message was not sent by a bot
        if not payload.member.bot:
            # remove the reaction
            await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
            # get message content
            message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

            url = "https://api-free.deepl.com/v2/translate"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=PL"

            resp = requests.post(url, headers=headers, data=data)

            # translated message embed
            embed = discord.Embed(title="Translated message",
                                    description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
            embed.set_footer(
                text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ PL",
                icon_url=payload.member.display_avatar)
            await message.reply(embed=embed, mention_author=False)
    # portuguese flag emoji
    elif payload.emoji.name == "🇵🇹":
        # checks if the message was not sent by a bot
        if not payload.member.bot:
            # remove the reaction
            await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
            # get message content
            message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

            url = "https://api-free.deepl.com/v2/translate"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=PT"

            resp = requests.post(url, headers=headers, data=data)

            # translated message embed
            embed = discord.Embed(title="Translated message",
                                    description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
            embed.set_footer(
                text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ PT",
                icon_url=payload.member.display_avatar)
            await message.reply(embed=embed, mention_author=False)
    # romanian flag emoji
    elif payload.emoji.name == "🇷🇴":
        # checks if the message was not sent by a bot
        if not payload.member.bot:
            # remove the reaction
            await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
            # get message content
            message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

            url = "https://api-free.deepl.com/v2/translate"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=RO"

            resp = requests.post(url, headers=headers, data=data)

            # translated message embed
            embed = discord.Embed(title="Translated message",
                                    description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
            embed.set_footer(
                text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ RO",
                icon_url=payload.member.display_avatar)
            await message.reply(embed=embed, mention_author=False)
    # russian flag emoji
    elif payload.emoji.name == "🇷🇺":
        # checks if the message was not sent by a bot
        if not payload.member.bot:
            # remove the reaction
            await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
            # get message content
            message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

            url = "https://api-free.deepl.com/v2/translate"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=RU"

            resp = requests.post(url, headers=headers, data=data)

            # translated message embed
            embed = discord.Embed(title="Translated message",
                                    description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
            embed.set_footer(
                text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ RU",
                icon_url=payload.member.display_avatar)
            await message.reply(embed=embed, mention_author=False)
    # slovak flag emoji
    elif payload.emoji.name == "🇸🇰":
        # checks if the message was not sent by a bot
        if not payload.member.bot:
            # remove the reaction
            await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
            # get message content
            message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

            url = "https://api-free.deepl.com/v2/translate"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=SK"

            resp = requests.post(url, headers=headers, data=data)

            # translated message embed
            embed = discord.Embed(title="Translated message",
                                    description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
            embed.set_footer(
                text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ SK",
                icon_url=payload.member.display_avatar)
            await message.reply(embed=embed, mention_author=False)
    # slovenian flag emoji
    elif payload.emoji.name == "🇸🇮":
        # checks if the message was not sent by a bot
        if not payload.member.bot:
            # remove the reaction
            await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
            # get message content
            message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

            url = "https://api-free.deepl.com/v2/translate"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=SL"

            resp = requests.post(url, headers=headers, data=data)

            # translated message embed
            embed = discord.Embed(title="Translated message",
                                    description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
            embed.set_footer(
                text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ SL",
                icon_url=payload.member.display_avatar)
            await message.reply(embed=embed, mention_author=False)
    # swedish flag emoji
    elif payload.emoji.name == "🇸🇪":
        # checks if the message was not sent by a bot
        if not payload.member.bot:
            # remove the reaction
            await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
            # get message content
            message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

            url = "https://api-free.deepl.com/v2/translate"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=SV"

            resp = requests.post(url, headers=headers, data=data)

            # translated message embed
            embed = discord.Embed(title="Translated message",
                                    description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
            embed.set_footer(
                text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ SV",
                icon_url=payload.member.display_avatar)
            await message.reply(embed=embed, mention_author=False)
    # chinese flag emoji
    elif payload.emoji.name == "🇨🇳":
        # checks if the message was not sent by a bot
        if not payload.member.bot:
            # remove the reaction
            await bot.http.remove_reaction(payload.channel_id, payload.message_id, payload.emoji, payload.member.id)
            # get message content
            message = await bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

            url = "https://api-free.deepl.com/v2/translate"

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/x-www-form-urlencoded"

            data = f"auth_key={config['DeepL_Auth_Key']}&text={demoji.replace(message.content, '')}&target_lang=ZH"

            resp = requests.post(url, headers=headers, data=data)

            # translated message embed
            embed = discord.Embed(title="Translated message",
                                    description=f"> {resp.json()['translations'][0]['text']}", color=0xe04c45)
            embed.set_footer(
                text=f"Requested by {payload.member.display_name} ●  {resp.json()['translations'][0]['detected_source_language']} ⟶ ZH",
                icon_url=payload.member.display_avatar)
            await message.reply(embed=embed, mention_author=False)

# start the bot
bot.run(config["token"])
