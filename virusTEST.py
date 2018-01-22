import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import pickle
import os
import requests
import json

Client = discord.Client()
bot_prefix= "p!"
client = commands.Bot(command_prefix=bot_prefix)

'''
EVENTS
'''
# TELLS YOU WHEN THE BOT IS READY
@client.event
async def on_ready():
    print("====================")
    print("Connected!")
    print("====================")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    print("====================")
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | '+str(len(client.servers))+' servers')
    await client.change_presence(game=discord.Game(name='Use p!help'))

# CLEVER BOT
CBuser = 'hTitan8XcqVKE5qt'
CBkey = 'jrUn80fYMmc1P6MTqqDwjCCoRo7yt5P5'
@client.event
async def on_message(message):
    if not message.author.bot and (message.server == None or client.user in message.mentions):
        await client.send_typing(message.channel)
        txt = message.content.replace(message.server.me.mention,'') if message.server else message.content
        r = json.loads(requests.post('https://cleverbot.io/1.0/ask', json={'user':CBuser, 'key':CBkey, 'nick':'Paradise', 'text':txt}).text)
        if r['status'] == 'success':
            await client.send_message(message.channel, r['response'] )
    else:
        await client.process_commands(message)

'''
COMMANDS
'''
# HELP COMMAND
client.remove_command('help')
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    footer_text = "Paradise ☁"
    embed1 = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
    embed1.set_author(name=str(author.name), icon_url=author.avatar_url)
    embed1.title = "COMMANDS FOR EVERYONE"
    embed1.add_field(name= "p!help", value= "Shows you this!", inline=True)
    embed1.add_field(name= "p!play", value= "plays the music in voice chat!", inline=True)
    embed1.add_field(name= "p!invite", value= "invites the bot", inline=True)
    embed1.add_field(name= "p!server", value= "invites to the paradise server!", inline=True)
    embed1.add_field(name= "p!ping", value= "Pings the bot!", inline=True)
    embed1.add_field(name= "p!serverinfo", value= "Gives you information about the server!", inline=True)
    embed1.add_field(name= "p!quote", value= "Gives you a random quote!", inline=True)
    embed1.add_field(name= "p!eightball (question)", value= "Ask the magic eightball a question!", inline=True)
    embed1.add_field(name= "p!suicide", value= "Gives you suicide fact!", inline=True)
    embed1.add_field(name= "p!heaven", value= "Gives you Heaven fact!", inline=True)
    embed1.add_field(name= "p!say (text)", value= "Forces the bot to say something!", inline=True)
    embed1.add_field(name= "p!profile (user)", value= "Shows you information about the mentioned user!", inline=True)
    embed1.set_footer(text=footer_text)

    author = ctx.message.author
    footer_text = "Paradise ☁"
    embed2 = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
    embed2.set_author(name=str(author.name), icon_url=author.avatar_url)
    embed2.title = "FUN COMMANDS"
    embed2.add_field(name= "p!retard", value= "Turns the mentioned user into a retard!", inline=True)
    embed2.add_field(name= "p!kill (user)", value= "Kills someone!", inline=True)
    embed2.add_field(name= "p!roast (user)", value= "Roasts someone!", inline=True)
    embed2.set_footer(text=footer_text)
     
    author = ctx.message.author
    footer_text = "Paradise ☁"
    embed3 = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
    embed3.set_author(name=str(author.name), icon_url=author.avatar_url)
    embed3.title = "MODERATION COMMANDS"
    embed3.add_field(name= "p!ban (user)", value= "Bans the mentioned user!", inline=True)
    embed3.add_field(name= "p!kick (user)", value= "Kicks the mentioned user!", inline=True)
    embed3.add_field(name= "p!prune (number)", value= "Deletes a number of messages!", inline=True)
    embed3.add_field(name= "p!unban (id)", value= "Unbans the user with the matching ID!", inline=True)
    embed3.add_field(name= "p!giverole (user) (role)", value= "Gives the mentioned user a specified role!", inline=True)
    embed3.add_field(name= "p!takerole (user) (role)", value= "Removes a specified role from the mentioned user!", inline=True)
    embed3.add_field(name= "p!rawsay (text)", value= "Forces the bot the say something without any formatting!", inline=True)
    embed3.set_footer(text=footer_text)

    author = ctx.message.author
    footer_text = "Paradise ☁"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
    msg.title = ""
    msg.set_author(name=str(author.name), icon_url=author.avatar_url)
    msg.add_field(name= ":incoming_envelope: ", value= "A list of commands is coming your way!\nCheck your DMs, {}!".format(author))
    msg.set_footer(text=footer_text)
    await client.say(embed=msg)
    await client.send_message(author, embed=embed1)
    await client.send_message(author, embed=embed2)
    await client.send_message(author, embed=embed3)

# PING COMMAND    
@client.command(pass_context=True)
async def ping(ctx):
    pingmsg = ["I'm here!", "Yes, I am here. You don't have to ping me!", "Hello?", "Oh, hi!", "Hey, how are you?", "Hello!", "Pong!"]
    author = ctx.message.author
    footer_text = "Paradise ☁"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
    msg.title = ""
    msg.set_author(name=str(author.name), icon_url=author.avatar_url)
    msg.add_field(name= ":satellite: Pinging...", value= "{}".format(random.choice(pingmsg)))
    msg.set_footer(text=footer_text)
    await client.say(embed=msg)
    print("============================================================")
    print("PING COMMAND")
    print("{}".format(author))
    print("============================================================")

# SERVER INFO COMMAND
@client.command(pass_context=True)
async def serverinfo(ctx):
    author = ctx.message.author
    footer_text = "Paradise ☁"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
    msg.title = ":page_with_curl: SERVER INFORMATION"
    msg.add_field(name="MEMBERS", value=(len(ctx.message.server.members)), inline=True)
    msg.add_field(name="CHANNELS", value=(len(ctx.message.server.channels)), inline=True)
    msg.add_field(name="EMOJIS", value=(len(ctx.message.server.emojis)), inline=True)
    msg.add_field(name="ID", value=(ctx.message.server.id), inline=True)
    msg.add_field(name="REGION", value=(ctx.message.server.region), inline=True)
    msg.add_field(name="ROLES", value=(len(ctx.message.server.roles)), inline=True)
    msg.add_field(name="OWNER", value=(ctx.message.server.owner), inline=True)
    msg.add_field(name="CREATED AT", value=(ctx.message.server.created_at), inline=True)
    msg.set_footer(text=footer_text)
    await client.say(embed=msg)
    print("============================================================")
    print("SERVERINFO COMMAND")
    print("{}".format(author))
    print("============================================================")

# p!retard (user) - TURNS PPL INTO RETARDS
@client.command(pass_context=True)
async def retard(context, userName: discord.User):
    footer_text = "Paradise ☁"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
    msg.title = ""
    msg.add_field(name= ":rofl: Retard Maker 3000", value= "`{} is now officially a retard!`\n`Research shows that most retards are good people!`".format(userName.display_name))
    msg.set_footer(text=footer_text)
    await client.say(embed=msg)
    print("============================================================")
    print("RETARD COMMAND")
    print("{}".format(context.message.author))
    print("============================================================")

# QUOTE COMMAND
@client.command(pass_context=True)
async def quote(ctx):
    quotes = ["If you want to achieve greatness stop asking for permission.",
              "Things work out best for those who make the best of how things work out.",
              "To live a creative life, we must lose our fear of being wrong.",
              "What hurts you, but doesn't kill you, makes you stronger.",
              " If you are not willing to risk the usual you will have to settle for the ordinary.",
              "Trust because you are willing to accept the risk, not because it’s safe or certain.",
              "Once you choose hope, anything is possible.",
              "A positive attitude gives you power over your circumstances instead of your circumstances having power over you.",
              "Character cannot be developed in ease and quiet. Only through experience of trial and suffering can the soul be strengthened, ambition inspired, and success achieved.",
              "Keep yourself busy if you want to avoid depression. For me, inactivity is the enemy.",
              "Sometimes, you gotta pretend everything is okay.",
              "It’s always worse than it seems.",
              "I get lost inside my mind”.",
              "All alone! Whether you like it or not, alone is something you'll be quite a lot!",
              "Twinkle, twinkle little star. Let me get hit by a car. Oh, how I really want to die, jump off the roof and try to fly. Twinkle, twinkle little knife, help me end this fucking life!",
              "There’s death all around us. Everywhere we look. 1.8 people kill themselves every second. We just don’t pay attention. Until we do.",
              "I guess that’s what saying good-bye is always like–like jumping off an edge. The worst part is making the choice to do it. Once you’re in the air, there’s nothing you can do but let go.",
              "The sun kept on with its slipping away, and I thought how many small good things in the world might be resting on the shoulders of something terrible.",
              "As the light begins to intensify, so does my misery, and I wonder how it is possible to hurt so much when nothing is wrong.",
              "But grief makes a monster out of us sometimes . . . and sometimes you say and do things to the people you love that you can’t forgive yourself for.",
              "Have you ever wondered what a human life is worth? That morning, my brother’s was worth a pocket watch.",
              "A lot of you cared, just not enough.",
              "Breathing is hard. When you cry so much, it makes you realize that breathing is hard.",
              "It's not I can or I can't, it's I want or I don't want!",
              "It’s raining in my heart like it’s raining in the city. What is this sadness that pierces my heart?",
              "At some point, you have to realize that some people can stay in your heart but not in your life.",
              "I forgive, but I don't forget.",
              "I hate getting flashbacks from things I don't want to remember.",
              "Do you know the feeling of drowning while everyone around you is breathing?",
              "Fake friends are like shadows. They follow you in the sun but leave you in the dark.",
              "You laugh, but you wanna cry. You talk, but you wanna be quiet. Yes, you're smiling, but inside, you're dying.",
              "This life is like a war, you either win with a scar or die trying.",
              "I'm fine.",
              "If I killed myself tonight, the sun will still rise, the stars would still appear, the Earth will still rotate, the seasons will still change... so why not?",
              "No amount of sleep can cure the tiredness I feel.",
              "Even the devil, was once an angel.",
              "I like my music so loud, I can't hear my thoughts.",
              "I smile all the time so that nobody knows how sad and lonely I really am.",
              "My mind was a mess, then I found a razor. Now my body is a mess too.",
              "I draw with silver and it becomes red. Magic!",
              "Why am I so different from everyone else?",
              "Emotionally: I'm done.  Mentally: I'm drained.  Spiritually: I'm dead.  Physically: I smile.",
              "It hurts when you smile just to stop the tears from falling.",
              "My blood is red. My wounds are wide. My heart hurts. I'm dead inside.",
              "I'm not totally useless. I can be used as a bad example.",
              "I'm pretending to be fine. So are they pretending to care?",
              "I'm slowly, but surely, giving up.",
              "People don't cry cause they are weak. They cry cause they were strong for too long.",
              "When I get angry, I don't yell, I don't hit, I don't show rage... I just think about ending it all.",
              "There is a hell, believe me, I've seen it.",
              "Everyone who hurt you, who left you, who didn't understand you, one day will regret it all.",
              "Walking with a friend in the dark is better than walking alone in the light.",
              "Remember, you are not alone. Darkness is and always will be with you.",
              "I don't care if I live or not.",
              "Stop trying to find a point or a meaning. There is no such thing.",
              "Not all scars show. Not all wounds heal. You can't always see the pain that others feel.",
              "We're scared to get close, cause everyone who promised they'll stay, turned their back and left.",
              "I don't like being too happy.",
              "I wanna sleep... forever.",
              "You shall not pass!",
              "You're adopted.",
              "Why should I apologize for being a monster? When no one apologized for turning me into one.",
              "You may not be my happy ending, but you are the best chapter of my life."]
    author = ctx.message.author
    footer_text = "Paradise ☁"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
    msg.title = ""
    msg.set_author(name=str(author.name), icon_url=author.avatar_url)
    msg.add_field(name= ":scroll: Scroll of quotes", value= "{}".format(random.choice(quotes)))
    msg.set_footer(text=footer_text)
    await client.say(embed=msg)
    print("============================================================")
    print("QUOTE COMMAND")
    print("{}".format(author))
    print("============================================================")

@client.command(pass_context=True)
async def invite(ctx):
    author = ctx.message.author
    footer_text = "Paradise ☁"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
    msg.title = "BOT INVITE :incoming_envelope:"
    msg.set_author(name=str(author.name), icon_url=author.avatar_url)
    msg.add_field(name= ":white_check_mark: ", value= "Your Bot invite have been send check your DMs, {}!".format(author))
    msg.set_footer(text=footer_text)
    await client.say(embed=msg)
    await client.send_message(ctx.message.author, "Heres Your invite link bot and the perfix is p!help enjoy and thanks for using it :) **NOTE:** to have moderation commands you should create role Paradise Bot with the caps on it and then give it to the bot role and ur self https://discordapp.com/api/oauth2/authorize?client_id=401419300096704525&permissions=0&scope=bot")

@client.command(pass_context=True)
async def server(ctx):
    author = ctx.message.author
    footer_text = "Paradise ☁"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
    msg.title = "SERVER INVITE :bulb: "
    msg.set_author(name=str(author.name), icon_url=author.avatar_url)
    msg.add_field(name= ":white_check_mark: ", value= "Your server invite have been send check your DMs, {}!".format(author))
    msg.set_footer(text=footer_text)
    await client.say(embed=msg)
    await client.send_message(ctx.message.author, "DISCORD LINK  https://discord.gg/Tk8RCer ")

# EIGHT BALL COMMAND
@client.command(pass_context=True)
async def eightball(ctx, *, args):
    answer = ["Yes!",
              "No!",
              "Probably!",
              "Most likely!",
              "Probably not!",
              "Definately!",
              "Definately not!",
              "Of course!",
              "Of course not!",
              "WTF no!",
              "Hell yeah!"]
    author = ctx.message.author
    footer_text = "Paradise ☁"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
    msg.title = "Magic Eight Ball"
    msg.set_author(name=str(author.name), icon_url=author.avatar_url)
    msg.add_field(name= ":grey_question: Question:", value= "{}".format(args), inline=True)
    msg.add_field(name= "\n:8ball: Eight Ball:", value="{}".format(random.choice(answer)), inline=True)
    msg.set_footer(text=footer_text)
    await client.say(embed=msg)
    print("============================================================")
    print("EIGHTBALL COMMAND")
    print("{}".format(author))
    print("============================================================")

# KILL COMMAND
@client.command(pass_context=True)
async def kill(context, userName: discord.User):
    killmsgs = ["died by getting beaten with a baseball bat covered with barbed wire!",
                "died by getting all their bones broken with chains!",
                "died from a nuclear explosion!",
                "died by getting shot in the head by an intruder!",
                "died by drowning in the ocean!",
                "died by getting eaten by a shark!",
                "got roasted so hard, they started burning and died!",
                "died by forgetting how to breathe!",
                "died by falling off the 30th floor!",
                "died by getting crushed by a meteor!",
                "died from radiation!",
                "died trying to fight an anaconda!",
                "died trying to fight darkness!",
                "died by aids!",
                "died from cancer!",
                "had a very stupid death, rather not tell what happened!",
                "died in a volcano!",
                "died by trying to leave the server! Do not try that, they were later revived in a more hell-ish version of their past life!",
                "died from not having memes to look at!",
                "died from a plane crash!",
                "were killed by an mysterious human-like figure!",
                "were killed cause they were a grammar nazi!",
                "were beaten to death by the bullies!",
                ", m8 u ded lol?",
                "died fro- lol jk u not die yet",
                "got their memes stolen and died from a heart attack!",
                "died?",
                "died! Only 2 players left!",
                "were killed in the hunger games!",
                "were killed before they even had a chance to live!",
                "died lmao get r3kt",
                "were killed... BY ME!",
                "tried to cheat on a math test, almost got away with it! Their body was found in a dumpster with a big F on their chest.",
                "was killed by a cute little bunny :3",
                "was killed by Lucifer!",
                "died by watching furry porn!",
                "died.. about time.. JK JK!!",
                "got killed by a true slav!",
                "died by not squating like a true slav!",
                "died by not using google!",
                "died by opening internet explorer!",
                "died from living!",
                "died from acid rain!",
                "got hit by lightning and died!",
                "was a good person! They had a nice family and a nice house, the whole world lived in harmony and peace... until the fire nation attacked!",
                "died by reading a book!",
                "died trying!",
                "died by watching the emoji movie!",
                "died by watching the bee movie!",
                "was killed lol",
                "left the game!",
                "died trying to do a backflip!",
                "got their heart ripped out!",
                "wasn't even born, what are you on about?",
                "can't die, they are already dead!",
                "died from looking at old memes!",
                "was killed by a fidget spinner!",
                "was killed by an attack helicopter!",
                "went inside a white van and never came out!",
                "got their head ripped off!",
                "starved in a supermarket while there was a zombie apocalypse!",
                "died while trying to steal Zero's chocolate!",
                "died by trying to hit a cat!",
                "died by trying to fly!",
                "died by getting hit with an anvil!",
                "died by setting their hair on fire!",
                "was killed by a kat!",
                "was last seen entering a white van!",
                "died by having no internet connection for more than 5 seconds!",
                "died by loosing their hentai stash!",
                "was killed after someone stole their memes!",
                "was killed by a retarded chicken!",
                "died by sun light!",
                "died after commiting suicide!",
                "died trying to perform a magic trick!",
                "left the game.",
                "was always the type of person who fights fire with fire... that didn't end well. They were a fireman!",
                "was killed by a bunneh!",
                "died before they had a chance to live!",
                "died... inside!",
                "had a boring death!",
                "died being a hero!"]
    
    footer_text = "Paradise ☁"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
    msg.title = ""
    msg.add_field(name="NEWS :gun:", value="`{} {}`".format(userName.display_name, random.choice(killmsgs)))
    msg.set_footer(text=footer_text)
    await client.say(embed=msg)
    print("============================================================")
    print("KILL COMMAND")
    print("{}".format(context.message.author))
    print("============================================================")

# ROAST COMMAND
@client.command(pass_context=True)
async def roast(context, userName: discord.User):
    roasts = ["I saw a piece of shit today. It reminded me of you.",
              "your face is a physical weapon.",
              "I know you from somewhere. Oh yea, I see you in the trashcan."
              "don't worry, you're not adopted... yet. We still haven't found anyone who wants you.",
              "unless your name is 'Google', stop acting like you know everything.",
              "if I wanted to kill myself I would climb up your ego and jump in your IQ",
              "you are so stupid that you got hit by a parked car.",
              "you're so fat that when god created light, you were asked to move out of the way.",
              "I heard you were taken to a dog show and you won.",
              "you suck so much, I can use you as a vacumcleaner.",
              "maybe you should stop making fun of others just to get attention, cause the world doesn't rotate around your crap looking ass.",
              "try not to spit when you talk, we don't need a public shower here.",
              "you remind me of the owner, eew.",
              "I can't breathe when I see you... cause I'm suffocating of your bullshit.",
              "your mom is twice the man you will ever be.",
              "you have the right to remain silent, cause what ever you say will be stupid anyways.",
              "the only thing you are good at is being a cunt.",
              "it's hard for you isn't it? Not to be a dick.",
              "it's hard to ignore you, mostly cause you smell like shit.",
              "you must've fallen from Mars, cause you clearly can't understand anything happening around you.",
              "did you fall from Heaven? Cause so did Satan.",
              "you're so ugly, you went to an ugly competition and they said 'No professionals allowed!'.",
              "you really shouldn't try cooking, cause the last time you did, it ended with 3 houses being on fire.",
              "did Satan send you to kill people? Cause your smell is killing me.",
              "I'd give you a nasty look but you've already got one.",
              "if laughter is the best medicine, your face must be curing the world.",
              "the only way you'll ever get laid is if you crawl up a chicken's ass and wait.",
              "scientists say the universe is made up of neutrons, protons and electrons. They forgot to mention morons.",
              "your family tree must be a cactus because everyone on it is a prick.",
              "someday you'll go far... and I hope you stay there.",
              "save your breath, you'll need it to blow your date.",
              "the zoo called. They're wondering how you got out of your cage?",
              "you have something on your chin... no, the 3rd one down.",
              "thought of you today. It reminded me to take the garbage out.",
              "you're so ugly when you look in the mirror, your reflection looks away.",
              "it's better to let someone think you're stupid than open your mouth and prove it.",
              "were you born this stupid or did you take lessons?",
              "calling you an idiot would be an insult to all stupid people.",
              "I just stepped in something that was smarter than you... and smelled better too."]
    footer_text = "Paradise ☁"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
    msg.title = ""
    msg.add_field(name=":fire: Roast Machine", value="`{}, {}`".format(userName.display_name, random.choice(roasts)))
    msg.set_footer(text=footer_text)
    await client.say(embed=msg)
    print("============================================================")
    print("ROAST COMMAND")
    print("{}".format(context.message.author))
    print("============================================================")

# HEAVEN COMMAND
@client.command(pass_context=True)
async def heaven(ctx):
    heaven = ["Heaven is Real – God created it",
               "Jesus, the Christ came down to Earth from Heaven",
               "Jesus went back to Heaven when He rose from the dead",
               "Jesus is now seated at the right hand of God (the Majesty) in Heaven",
               "heaven is also known as a place where the birds fly and the clouds float – the Bible also calls this the firmament",
               "heaven is a place where the stars, sun and constellations shine – this is the stellar heaven",
               "Heaven is where the believer goes when he leaves this planet – it is home",
               "Believers can look forward to a new heaven – it is the blessed hope and a perfect place",
               "Heaven is God’s home and He existed before His creation – this is the Heaven of heavens; the high and holy place",
               "Before creation, Jesus (God’s Son) and Holy Spirit lived in Heaven with God",]
    author = ctx.message.author
    footer_text = "Paradise"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
    msg.title = ""
    msg.set_author(name=str(author.name), icon_url=author.avatar_url)
    msg.add_field(name= ":angel:  Heaven Facts", value= "{}".format(random.choice(heaven)))
    msg.set_footer(text=footer_text)
    await client.say(embed=msg)
    print("============================================================")
    print("HEAVEN COMMAND")
    print("{}".format(author))
    print("============================================================")


# SUICIDE COMMAND
@client.command(pass_context=True)
async def suicide(ctx):
    suicide = ["In 2015 (latest available data), there were 44,193 reported suicide deaths in the U.S.",
               "Suicide is the 2nd leading cause of death for those between the ages of 15 and 34 in the United States.",
               "Currently, suicide is the 10th leading cause of death in the United States.",
               "A person dies by suicide about every 12.8 minutes in the United States.",
               "Every day, approximately 121 Americans take their own life.",
               "Ninety percent of all people who die by suicide have a diagnosable psychiatric disorder at the time of their death.",
               "There are four male suicides for every female suicide, but three times as many females as males attempt suicide.",
               "494,169 people visited a hospital for injuries due to self-harm behavior, suggesting that approximately 12 people harm themselves (not necessarily intending to take their lives) for every reported death by suicide.",
               "25 million Americans suffer from depression each year.",
               "Over 50 percent of all people who die by suicide suffer from major depression. If one includes alcoholics who are depressed, this figure rises to over 75 percent.",
               "Depression affects nearly 5-8 percent of Americans ages 18 and over in a given year.",
               "Depression is among the most treatable of psychiatric illnesses. Between 80 percent and 90 percent of people with depression respond positively to treatment, and almost all patients gain some relief from their symptoms. But first, depression has to be recognized.",
               "More Americans suffer from depression than coronary heart disease, cancer, and HIV/AIDS.",
               "Nearly 30,000 Americans commit suicide every year.",
               "In the U.S., suicide rates are highest during the spring.",
               "Suicide is the 3rd leading cause of death for 15 to 24-year-olds and 2nd for 24 to 35-year-olds.",
               "On average, 1 person commits suicide every 16.2 minutes.",
               "Each suicide intimately affects at least 6 other people.",
               "About 2/3 of people who complete suicide are depressed at the time of their deaths. Depression that is untreated, undiagnosed, or ineffectively treated is the number 1 cause of suicide.",
               "There is 1 suicide for every 25 attempted suicides.",
               "Males make up 79% of all suicides, while women are more prone to having suicidal thoughts.",
               " in 65,000 children ages 10 to 14 commit suicide each year.",]
    author = ctx.message.author
    footer_text = "Paradise "
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
    msg.title = ""
    msg.set_author(name=str(author.name), icon_url=author.avatar_url)
    msg.add_field(name= ":skull: Suicide Facts", value= "{}".format(random.choice(suicide)))
    msg.set_footer(text=footer_text)
    await client.say(embed=msg)
    print("============================================================")
    print("SUICIDE COMMAND")
    print("{}".format(author))
    print("============================================================")
        

# SAY COMMAND
@client.command(pass_context=True)
async def say(context, *, args):
    await client.say("`{}`".format(args))
    print("============================================================")
    print("SAY COMMAND")
    print("{}".format(context.message.author))
    print("============================================================")

# USER INFO COMMAND
@client.command(pass_context=True)
async def profile(context, userName: discord.Member):
    imageurl = userName.avatar_url
    author = context.message.author
    footer_text = "Paradise ☁"
    msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
    msg.title = ":page_with_curl: USER INFORMATION"
    msg.set_thumbnail(url=imageurl)
    msg.set_author(name=str(userName), icon_url=userName.avatar_url)
    msg.add_field(name="NAME:", value=(userName), inline=True)
    msg.add_field(name="ID:", value=(userName.id), inline=True)
    msg.add_field(name="CREATED AT:", value=(userName.created_at), inline=True)
    msg.add_field(name="JOINED AT:", value=(userName.joined_at), inline=True)
    msg.add_field(name="STATUS:", value=(userName.status), inline=True)
    msg.add_field(name="IS BOT:", value=(userName.bot), inline=True)
    msg.add_field(name="GAME:", value=(userName.game), inline=True)
    msg.add_field(name="NICKNAME:", value=(userName.nick), inline=True)
    msg.add_field(name="TOP ROLE:", value=(userName.top_role), inline=True)
    msg.set_footer(text=footer_text)
    await client.say(embed=msg)
    print("============================================================")
    print("PROFILE COMMAND")
    print("{}".format(author))
    print("============================================================")

'''
MODERATION COMMANDS
'''

# RAW SAY COMMAND
@client.command(pass_context=True)
async def rawsay(context, *, args):
    for role in context.message.author.roles:
        if role.name == "Paradise Bot":
            await client.say("{}".format(args))
            print("============================================================")
            print("RAWSAY COMMAND")
            print("{}".format(context.message.author))
            print("============================================================")

# TAKE/GIVE ROLE COMMAND
@client.command(pass_context=True)
async def takerole(ctx, userName: discord.Member, *, rolename):
    for role in ctx.message.author.roles:
        if role.name == "Paradise Bot":
            rolename2 = discord.utils.get(ctx.message.server.roles, name='{}'.format(rolename))
            await client.remove_roles(userName, rolename2)
            author = ctx.message.author
            footer_text = "Paradise ☁"
            msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
            msg.title = ""
            msg.set_author(name=str(author.name), icon_url=author.avatar_url)
            msg.add_field(name= ":outbox_tray: Taking away role...", value= "`{} has removed {} from {}`".format(ctx.message.author, rolename2, userName.display_name), inline=True)
            msg.set_footer(text=footer_text)
            await client.say(embed=msg)
            print("============================================================")
            print("TAKEROLE COMMAND")
            print("{}".format(author))
            print("============================================================")

@client.command(pass_context=True)
async def giverole(ctx, userName: discord.Member, *, rolename):
    for role in ctx.message.author.roles:
        if role.name == "Paradise Bot":
            rolename2 = discord.utils.get(ctx.message.server.roles, name='{}'.format(rolename))
            await client.add_roles(userName, rolename2)
            author = ctx.message.author
            footer_text = "Paradise ☁"
            msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
            msg.title = ""
            msg.set_author(name=str(author.name), icon_url=author.avatar_url)
            msg.add_field(name= ":inbox_tray: Giving role...", value= "`{} has given {} to {}`".format(ctx.message.author, rolename2, userName.display_name), inline=True)
            msg.set_footer(text=footer_text)
            await client.say(embed=msg)
            print("============================================================")
            print("GIVEROLE COMMAND")
            print("{}".format(author))
            print("============================================================")

# UNBAN COMMAND
@client.command(pass_context=True)
async def unban(ctx, userID):
    for role in ctx.message.author.roles:
        if role.name == "Paradise Bot":
            banned_users = await client.get_bans(ctx.message.server)
            user = discord.utils.get(banned_users,id=userID)
            if user is not None:
                await client.unban(ctx.message.server, user)
                author = ctx.message.author
                footer_text = "Paradise ☁"
                msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
                msg.title = ""
                msg.set_author(name=str(author.name), icon_url=author.avatar_url)
                msg.add_field(name= ":tools: UNBAN TOOLS", value= "`{}#{} has been unbanned by {}!`".format(user.name, user.discriminator, ctx.message.author), inline=True)
                msg.set_footer(text=footer_text)
                await client.say(embed=msg)
                print("============================================================")
                print("UNBAN COMMAND")
                print("{}".format(author))
                print("============================================================")
            else:
                author = ctx.message.author
                footer_text = "Paradise ☁"
                msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
                msg.title = ""
                msg.set_author(name=str(author.name), icon_url=author.avatar_url)
                msg.add_field(name= ":octagonal_sign: ERROR", value= "`{} isn't banned!`".format(user.name), inline=True)
                msg.set_footer(text=footer_text)
                await client.say(embed=msg)
                print("============================================================")
                print("UNBAN COMMAND")
                print("{}".format(author))
                print("============================================================")

# KICK COMMAND
@client.command(pass_context=True)
async def kick(ctx, userName: discord.Member):
    for role in ctx.message.author.roles:
        if role.name == "Paradise Bot":
            await client.kick(userName)
            author = ctx.message.author
            footer_text = "Paradise ☁"
            msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
            msg.title = ""
            msg.set_author(name=str(author.name), icon_url=author.avatar_url)
            msg.add_field(name= ":boot: KICK BOOT", value= "`{} has been kicked by {}!`".format(userName.display_name, ctx.message.author), inline=True)
            msg.set_footer(text=footer_text)
            await client.say(embed=msg)
            print("============================================================")
            print("KICK COMMAND")
            print("{}".format(author))
            print("============================================================")

# BAN COMMAND
@client.command(pass_context=True)
async def ban(ctx, userName: discord.Member, days=None):
    for role in ctx.message.author.roles:
        if role.name == "Paradise Bot":
            if days == None:
                await client.ban(userName)
                author = ctx.message.author
                footer_text = "Paradise ☁"
                msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
                msg.title = ""
                msg.set_author(name=str(author.name), icon_url=author.avatar_url)
                msg.add_field(name= ":hammer: BAN HAMMER", value= "`{} has been banned by {}! No messages were deleted!`".format(userName.display_name, ctx.message.author), inline=True)
                msg.set_footer(text=footer_text)
                await client.say(embed=msg)
                print("============================================================")
                print("BAN COMMAND")
                print("{}".format(author))
                print("============================================================")
            else:
                await client.ban(userName, delete_message_days=days)
                author = ctx.message.author
                footer_text = "Paradise ☁"
                msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
                msg.title = ""
                msg.set_author(name=str(author.name), icon_url=author.avatar_url)
                msg.add_field(name= ":hammer: BAN HAMMER", value= "`{} has been banned by {}! Deleting messages from the past {} days...`".format(userName.display_name, ctx.message.author, days), inline=True)
                msg.set_footer(text=footer_text)
                await client.say(embed=msg)
                print("============================================================")
                print("BAN COMMAND")
                print("{}".format(author))
                print("============================================================")

@client.command(pass_context=True)
async def prune(ctx, number : int):
    for role in ctx.message.author.roles:
        if role.name == "Paradise Bot":
            deleted = await client.purge_from(ctx.message.channel, limit=number)
            author = ctx.message.author
            footer_text = "Paradise ☁"
            msg = discord.Embed(colour=random.randint(0, 0xFFFFFF), description= "")
            msg.title = ""
            msg.set_author(name=str(author.name), icon_url=author.avatar_url)
            msg.add_field(name= ":wastebasket: CHAT CLEANER", value= "`Deleted {} message(s)!`".format(len(deleted), inline=True))
            msg.set_footer(text=footer_text)
            await client.say(embed=msg)
            print("============================================================")
            print("PRUNE COMMAND")
            print("{}".format(author))
            print("============================================================")

'''
'''
# THIS WILL TURN ON YOUR BOT
requests.post('https://cleverbot.io/1.0/create', json={'user':CBuser, 'key':CBkey, 'nick':'Paradise'})

client.run('NDAxNDE5MzAwMDk2NzA0NTI1.DUC_6g.fBLV2RXYxMqyY384u5lu4wtty04')
