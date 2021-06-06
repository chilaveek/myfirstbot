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
async def kick(ctx, member: discord.Member, *, reason = None):
    await ctx.channel.purge(limit = 1)
    await member.kick(reason=reason)
    emb = discord.Embed(title = '! kick', colour=discord.Color.blue())

    emb.set_author(name = bot.user.name, icon_url = bot.user.avatar_url)
    emb.add_field(name= 'Кикнут участник', value='Кикнут Лось под именем {}'.format(member.mention) + ' И это не только из-за АХАХАХА, у нас нормальный отбор.')

    await ctx.send(embed = emb)

# ban
@bot.command(pass_context = True)
@commands.has_any_role("Bot Father")
async def ban(ctx, member : discord.Member, nick, *, reason=None):
    await ctx.channel.purge(limit = 1)
    await member.ban(reason=reason)
    
    emb = discord.Embed(title = '! ban', colour=discord.Color.blue())

    emb.set_author(name = bot.user.name, icon_url = bot.user.avatar_url)
    emb.add_field(name = 'Смена Ника', value= 'Лось под именем {}'.format(member.mention) + ' забанен. Такие дела.')
    emb.set_footer(text= 'command by ' + ctx.author.name, icon_url= ctx.author.avatar_url)

    await ctx.send(embed = emb)

# unban
@bot.command(pass_context = True)
@commands.has_any_role('Bot Father')
async def unban(ctx, nick):
    emb = discord.Embed(title = '! unban', colour=discord.Color.blue())

    emb.set_author(name = bot.user.name, icon_url = bot.user.avatar_url)
    emb.set_footer(text= 'command by ' + ctx.author.name, icon_url= ctx.author.avatar_url)

    await ctx.send(embed = emb)

# rename
@bot.command(pass_context=True)
async def nick(ctx, member: discord.Member, nick):
    await ctx.channel.purge(limit = 1)
    await member.edit(nick=nick)

    emb = discord.Embed(title = '! nick', colour=discord.Color.blue())

    emb.set_author(name = bot.user.name, icon_url = bot.user.avatar_url)
    emb.add_field(name = 'Смена Ника', value= 'Ник пользователя {}'.format(member.mention) + ' сменён. Зачем вам эта информация? Не знаю, просто мне нравится всё бесполезное.')
    emb.set_footer(text= 'command by ' + ctx.author.name, icon_url= ctx.author.avatar_url)

    await ctx.send(embed = emb)



@bot.event
async def on_message(message):
    await bot.process_commands(message)
    # msg = message.content.lower()
    # author = message.author.name


# run
bot.run(TOKEN)
