import discord
from discord.ext import commands
import os
import asyncio
import random
import urllib
from bs4 import BeautifulSoup
from urllib.request import Request
from urllib import parse
import bs4
import time


client = discord.Client()

owner = ['724769557759393837']
@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))

@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))

@client.event
async def on_member_join(member):

    if message.content == '*보안시작':
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="봇이랑 등록중", value="잠시만 기다려주세요 잘 되고 있거든요 ! 봇이 등록하는데는 몇 분이 걸려요.그리고 봇이 없어도 등록이 됩니다 !  ", inline=True)
                embed.set_footer(text=f"{message.author}, 인증안됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
                time.sleep(90)
                await message.delete()
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="봇 보안 등록이 완료되었습니다.", value="봇 보안 기능이 되는데는 1시간 종도 걸립니다.!", inline=True)
                await message.channel.send(embed=embed)
        

client.run('NzMyMjE2Njg0NTE2OTk5MTk4.XwxX7Q.aAxk7065OCZLSIlCCKIOT7Et-3E')
