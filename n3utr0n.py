#! /usr/bin/python
# -*- coding: utf-8 -*-
# Barea's Code

# Módulos
import discord
import asyncio
import logging
import time
from datetime import datetime
import databot.configbot
# Constantes
tokenbot = databot.configbot.tokenbot
client = discord.Client()
logging.basicConfig(level=logging.INFO,
format='%(asctime)s | %(levelname)s | %(name)s: %(message)s')

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(
filename='n3utr0n-bot-last.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
'%(asctime)s > %(levelname)s > %(name)s > %(message)s\n'))
logger.addHandler(handler)

# Clases
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------
async def commandos_admin(message):
    if message.content.startswith('-kick'):
        print(time.asctime() + ' - ' + str(message.server) + ' - ' + str(message.author) + ' > -kick')

        usuario = message.content.strip('-kick ')
        member = discord.utils.find(lambda m: m.mention == usuario,
        message.channel.server.members)
        await client.kick(member)
        await client.send_message(message.channel,
        ':x: El usuario ' + usuario + ' ha sido expulsado.')

    if message.content.startswith('-ban'):
        print(time.asctime() + ' - ' + str(message.server) + ' - ' + str(message.author) + ' > -ban')

        usuario = message.content.strip('-ban ')
        member = discord.utils.find(lambda m: m.mention == usuario,
        message.cahnnel.server.members)
        await client.ban(member)
        await client.send_message(message.channel,
        ':x: :x: El usuario ' + usuario + ' ha sido baneado.')

    if message.content.startswith('-purge'):
        print(time.asctime() + ' - ' + str(message.server) + ' - ' + str(message.author) + ' > -purge')

        counter = 0
        await client.send_message(message.channel,
        'Borrando mensajes...')
        asyncio.sleep(5)
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.purge_from(channel=message.channel, limit=100)
        await client.send_message(message.channel,
        '**¡Borrado exitoso!** Se han borrado los {} últimos mensajes'.format(counter))

# ---------------------------------------- ACUERDATE DE ESTO
    if message.content.startswith('-hola'): # Prueba de parámetros/argumentos
        argumentos = message.content[5:]
        lista_argumentos = argumentos.split()
        if len(lista_argumentos) > 0:
            await client.send_message(message.channel, lista_argumentos[0])
            await client.send_message(message.channel, lista_argumentos[1])
        else:
            await client.send_message(message.channel, 'Faltan argumentos')

# ---------------------------------------------------------------------

@client.event
async def on_ready():
    if client.is_logged_in == True:
        print('\n¡BOT INICIADO CON EXITO!')
        print('        Fecha:', time.asctime())
        print('   Nombre bot:', client.user.name)
        print('     Nº serie:', '#' + client.user.discriminator)
        print('       ID bot:', client.user.id)
        print('  Versión API:', discord.__version__)
        print('--------------')
        print('  Server List:\nServidor: ' +
            '\nServidor: '.join(s.name + ' - Dueño: ' + str(s.owner) for s in client.servers))
        print('--------------')

tiempo_activo = time.strftime('**%d/%m/%Y %H:%M:%S**', time.gmtime())

@client.event
async def on_message(message):
    autor = message.author
    tiempo_init = datetime.now()

    await commandos_admin(message)

    if message.content.startswith('!help'):
        print(time.asctime() + ' - ' + str(message.server) + ' - ' + str(message.author) + ' > !help')

        await client.send_message(message.channel,
        'El prefijo de este bot es \'-\', un guión. Por ejemplo: `-ping`' +
        '\nPor lo tanto utiliza `-help` si quieres saber los comandos que hay disponibles :mag:')

    if message.content.startswith('-help'): # Comando ayuda
        print(time.asctime() + ' - ' + str(message.server) + ' - ' + str(message.author) + ' > -help')

        await client.send_message(message.channel,
        ':arrow_forward: COMANDOS:\n'
        '```Markdown'
        '\nEl prefijo de este bot es un guión \'-\''
        '\n-ping -- Devuelve el tiempo que tarda en enviar el mensaje'
        '\n-purge -- elimina un max de 100 mensajes de una vez'
        '\n-invitar -- Devuelve el link para añadir al bot en tu servidor'
        '\n-kick -- Puedes expulsar a un miembro del servidor usando la mención'
        '\n-ban -- Baneas a un miembro del servidor usando la mención'
        '```')

    if message.content.startswith('-ping'): # Dice la fecha de cuando se inicio el server
        print(time.asctime() + ' - ' + str(message.server) + ' - ' + str(message.author) + ' > -ping')

        msg = await client.send_message(message.channel,
        '**PONG!** Creado por **@Barea1396#5050**'
        '\n\nPing: ``')
        tiempo_fin = datetime.now()
        tiempo_total = tiempo_fin.microsecond - tiempo_init.microsecond
        tiempo_total = tiempo_total/10000
        await client.edit_message(msg,
        '**PONG!** Creado por **@Barea1396#5050**'
        '\n\nPing: `' + str(tiempo_total) + '` ms')

    if message.content.startswith('-invitar'): # Devuelve el link para añadir el bot
        print(time.asctime() + ' - ' + str(message.server) + ' - ' + str(message.author) + ' > -invitar')

        await client.send_message(message.channel,
        'Invitame a tu servidor! https://goo.gl/d4N8bS')

client.accept_invite('https://discord.gg/98HUzhj')
client.run(tokenbot)
