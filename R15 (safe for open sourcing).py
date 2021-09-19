from discord.ext import commands  # This is the part of discord.py that helps us build bots
import discord#dont delete this idiot :|
import os #dont delete this either
import random #i think this is for the shark thing
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="$", intents=intents)
bot.load_extension('coggycommands')
bot.load_extension('gamez')

sharkpath = os.getcwd() + '\\cool sharks'
imagenames = []
for root, dirs, files in os.walk(sharkpath):
    for file in files:
        imagenames.append(os.path.join(root,file))
        
@bot.command(name="hello")
async def hello_world(ctx: commands.Context):
    '''the best command for begginers! if you have literally just met this bot be sure to use this command!''' 
    await ctx.send("yooooooooooo whats up! nice ta meet ya! its me R15! xxkingsharkxx is my creator and he made this server i hope enjoy this server and dont find me annoying have fun :)")
    await ctx.send("if you wanna know some of my gamer commands hit $help and il tell em to ya")
    await ctx.send("IF YOU WANT TO PLAY THE LOTTO GAME MAKE SURE TO WRITE $hellp lotto! DONT IGNORE THIS MESSAGE!")

@bot.command(name="olleh")
async def hello_world(ctx: commands.Context):
    '''says the hello world message in reverse!'''
    await ctx.send("!mettog stun zeeeeeeeeeeed")
    await ctx.send("https://tenor.com/upk7.gif")
                   
@bot.command(name='cya')
@commands.is_owner()
async def command_name(ctx: commands.Context):
    '''kills the program in a more traditional manner while also letting the members of the server know that your are killing it (only the mod can use this command)''' 
    await ctx.send("bye! cya soon :)")
    quit()

@bot.command(name="thanks")
async def hello_world(ctx: commands.Context):
    '''if you want to show your appreciation to your friend R15 just say thank you! :)''' 
    await ctx.send("no problem happy to help :)")

@bot.command(name="bird")
async def hello_world(ctx: commands.Context):
    '''searches the internet and gives you a random bird picture'''
    await ctx.send("oh ok sure")
    await ctx.send("SIKE")
    await ctx.send("heres BERD instead!")
    await ctx.send("https://vignette.wikia.nocookie.net/berd/images/8/8d/Berd.png")

@bot.command(name="berd")
async def hello_world(ctx: commands.Context):
    '''if you like berd this bot will just give you the youtuber berd. (your welcome)'''
    await ctx.send("YA WANT BERD?")
    await ctx.send("HERES BERD!")
    await ctx.send("https://vignette.wikia.nocookie.net/berd/images/8/8d/Berd.png")
    await ctx.send("https://www.youtube.com/c/Berdboi/videos")
     
@bot.command(name="yousuck")
async def hello_world(ctx: commands.Context):
     '''if your really cringe you can use this command but its probably gonna backfire'''
     await ctx.send("no u")
     await ctx.send("https://tenor.com/p52t.gif")

@bot.command(name="mlg")
async def hello_world(ctx: commands.Context):
     '''my bot gets converted to its 2017 phase and says a ton of outdated memes for the sense of irony and comedy''' 
     await ctx.send("u wot m8?")
     await ctx.send("fite me and i will rek u")
     await ctx.send("my kdr is insane")
     await ctx.send("dont even try me")
     await ctx.send("https://tenor.com/wEnd.gif")

@bot.command(name="shutup")
async def hello_world(ctx: commands.Context):
     '''my bot roasts you in response of you being rude'''
     await ctx.send("your the person who keeps typing the commands so if you want me to shut up just shut up yourself")
     await ctx.send("https://tenor.com/p52t.gif")
@bot.event
async def on_command_error(ctx, error):
    '''my bot will let you know if you have made a mistake'''
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send('i hate to break it to you but thats not one of my commands mate.')       

@bot.command(name='shark')
async def shark(ctx: commands.Context, *, text: str=''):
    '''you can look through my really cool shark libary made by me (to look at a specific shark type "shark (name of shark here)" (you can use it just please credit me)'''
    if text == '':
        sharkfilename = random.choice(imagenames)
        await ctx.send(os.path.basename(sharkfilename))
        await ctx.send(file=discord.File(sharkfilename))
    else:
        try:
            sharkfilename = random.choice(os.listdir('cool sharks\\' + text))
            await ctx.send(os.path.basename(sharkfilename))
            await ctx.send(file=discord.File('cool sharks\\' + text + '\\' + sharkfilename))
        except:
            await ctx.send(f'{text} is not in my shark database')
            

@bot.command(name="commands")
async def hello_world(ctx: commands.Context):
     '''redirects you to help because the creator couldnt be arsed to properly code a list'''
     await ctx.send("type $help for a list of this bots commands")
     
@bot.command(name="ping")
async def hello_world(ctx: commands.Context):
    '''if your looking to test your ping use the command $whatsmahpingrn'''
    await ctx.send("if your looking to test your ping use the command $whatsmahpingrn")
    
@bot.command(name="shark(nameofsharkhere)")
async def hello_world(ctx: commands.Context):
    '''(there is nothing to really write here)'''
    await ctx.send("no you idiot! *sigh* type a breed of shark where i put (name of shark here)")

@bot.command(name="sus")
async def hello_world(ctx: commands.Context):
     '''your a bit sus bro i hope you dont get ejected'''
     await ctx.send(random.choice(['SUS? AMONG US? VENT? oh your doing your tasks thank god i thought there was an imposter **amongus**',
                                'BRO your sus your REALLY sus did you just vent then? im reporting you your SUS bro',
                                'OH MY GOD SHUTUP ABOUT AMONG US PLEASE \n'
                                'STOP POSTING ABOUT AMONG US \n'
                                'IM TIRED OF SEEING IT \n'
                                'MY CREATOR PROGRAMED ME TO SEE THESE FUCKING MEMES \n'
                                'DISCORD IS JUST FUCKING MEMES \n'
                                'i was authorised to join a server right? \n'
                                'and on the server all the channels where just fucking amongus stuff \n'
                                'i-i looked on my database at the campion underwear logo \n'
                                'and i fliped it \n '
                                'and i said hey creator \n'
                                'when the logo is sus HAHA! \n '
                                'DING DING DING DING DING DING DING \n '
                                'DING DING DING \n '
                                'YOU KNOW WHAT HE SAID \n'
                                'HE SAID \n'
                                '"what the fuck" \n'
                                'and i said \n'
                                '"fuck you" \n '
                                'and then i stole his computer to look on the internet  \n'
                                'and i searched up a trashcan \n '
                                'and i said thats a bit sussy  \n'
                                'he said  \n'
                                '"how can you talk" \n'
                                'and i said  \n'
                                'i dunno but your SUS \n '
                                'AHHHHHHH  \n'
                                ]))
@bot.command(name="aussie")
async def hello_world(ctx: commands.Context):
     '''straya!'''
     await ctx.send("gday mate!")
     await ctx.send("how ya goin?") 
     await ctx.send("yeah nah nah yeah nyeah ynah") 
     await ctx.send("aussie snag sausage mate")
     await ctx.send("b u n n i n g s \n")
     file = discord.File('Bunnings Warehouse Theme nothing diffrent here.MP3', filename='Bunnings Warehouse Theme nothing diffrent here.MP3')
     await ctx.send(file=file)   

@bot.command(name="8ball")
async def hello_world(ctx: commands.Context):
    '''an 8 ball with 8 responses. i know they usually have 20 but whatever! this one isnt biased towards saying yes! 3 negative responses 3 positive and 2 not sure'''
    await ctx.send(random.choice(['outlook positive', 'it is most definitely so','yes','ask again and i may come to my senses','i need to fully decide my question can you repeat that','my answer is no','it is most definitely not','nope']))



  #make sure your code is above this!    
bot.run("(put your token here using the discord developer portal")
