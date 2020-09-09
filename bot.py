import random
import discord
from discord.ext import commands

# Основная важная информация
PREFIX = '! '
TOKEN = 'NzUxNzgyODYxMzEyNDkxNjIw.X1OGWQ.sq7Br6uS9gcHAFUEkgdOa4yiq4M'

# Разные списки

bot = commands.Bot(command_prefix=PREFIX)
bot.remove_command('help')

# instruction for online
@bot.event
async def on_ready():
    activity = discord.Game(name="Казино")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print('BOT IS ONLINE')

# help
@bot.command(pass_context=True)
async def help(ctx):
    emb = discord.Embed(title = 'Вот что я могу:', colour=discord.Color.blue())
    emb.add_field(name ='{}nick'.format(PREFIX), value = 'Сменить ник')
    emb.add_field(name ='{}kick'.format(PREFIX), value = 'Кик с сервера (Только Админ)')
    emb.add_field(name ='{}ban'.format(PREFIX), value = 'Бан на сервере (Только Админ)')
    emb.add_field(name ='{}unban'.format(PREFIX), value = 'Снятие Бана (Только Админ)')
    await ctx.channel.purge(limit = 1)
    await ctx.send(embed = emb)
# kick
@bot.command(pass_context = True)
@commands.has_any_role("Bot Father")
async def kick(ctx, member: discord.Member, nick, *, reason = None):
    await ctx.channel.purge(limit = 1)
    await member.kick(reason=reason)
    await ctx.send(f'Лось под именем "**{nick}**" кикнут с сервера')

# ban
@bot.command(pass_context = True)
@commands.has_any_role("Bot Father")
async def ban(ctx, member : discord.Member, nick, *, reason=None):
    await ctx.channel.purge(limit = 1)
    await member.ban(reason=reason)
    await ctx.send(f'Лось под именем "**{nick}**" забанен на неопределенный срок')

# unban
@bot.command(pass_context = True)
@commands.has_any_role('Bot Father')
async def unban(ctx, nick):
    emb = discord.Embed(title = 'Разбан!', colour=discord.Color.blue())

    emb.set_author(name = bot.user.name, icon_url = bot.user.avatar_url)
    emb.set_footer(text= 'command by ' + ctx.author.name, icon_url= ctx.author.avatar_url)

    await ctx.send(embed = emb)

# rename
@bot.command(pass_context=True)
async def nick(ctx, member: discord.Member, nick):
    await ctx.channel.purge(limit = 1)
    await member.edit(nick=nick)
    await ctx.send(f'Никнейм был изменён для пользователя {member.mention} ')



@bot.event
async def on_message(message):
    await bot.process_commands(message)
    # msg = message.content.lower()
    # author = message.author.name


# run
bot.run(TOKEN)
