import discord
from discord.ext.commands import bot

import config


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_raw_reaction_add(self, payload):
        if payload.message_id == config.Message_ID:
            try:
                user = payload.member
                role = discord.utils.get(user.guild.roles, name=config.RolesToAdd[config.Roles[payload.emoji.name]])
                await user.add_roles(role)
                print('User: {0} added reaction: {1} and received role: {2}'.format(payload.member, payload.emoji,
                                                                                    config.RolesToAdd[config.Roles[
                                                                                        payload.emoji.name]]))
            except Exception as e:
                print(e)

    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == config.Message_ID:
            try:
                guild_id = payload.guild_id
                guild = client.get_guild(guild_id)
                role = discord.utils.get(guild.roles, name=config.RolesToAdd[config.Roles[payload.emoji.name]])
                member = await (await client.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
                await member.remove_roles(role)
                print('User: {0} added reaction: {1} and removed role: {2}'.format(member, payload.emoji,
                                                                                   config.RolesToAdd[config.Roles[
                                                                                       payload.emoji.name]]))
            except Exception as e:
                print(e)


client = MyClient()
client.run(config.Token)
