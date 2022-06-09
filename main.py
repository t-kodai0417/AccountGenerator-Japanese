credits="""
        _      _              
  /\/\ (_) ___| | _____ _   _ 
 /    \| |/ __| |/ / _ \ | | |
/ /\/\ \ | (__|   <  __/ |_| |
\/    \/_|\___|_|\_\___|\__, |
                        |___/ 
ADD ME ON DISCORD  The Young Mickey#0139
OR JOIN THE DISCORD SERVER https://discord.gg/ZPXrpjUJkC
IF YOU WANT A BETTER BOT, WE CAN PROVIDE. THIS IS FOR FREE AND NOT MUCH WORK WAS PUT INTO IT
FORKED BY Kodai#2008. DISCORD SERVER: https://discord.gg/brazilshop"""







#ACCOUNT FILE NAMES NEED TO BE LOWERCASED
print(credits)
import discord,json,os,random
from discord.ext import commands
import asyncio

with open("config.json") as file: # Load the config file
    info = json.load(file)
    token = info["token"]
    delete = info["autodelete"]
    prefix = info["prefix"]
    channel_id=info["chid"].split(",")

bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Bot Running!")
@bot.command() # Stock command
async def stock(ctx):
    if str(ctx.channel.id) in channel_id:
            stockmenu = discord.Embed(title="Account Stock",description="") # Define the embed
            for filename in os.listdir("Accounts"):
                with open("Accounts\\"+filename) as f: # Open every file in the accounts folder
                    ammount = len(f.read().splitlines()) # Get the ammount of lines
                    name = (filename[0].upper() + filename[1:].lower()).replace(".txt","") #Make the name look nice
                    stockmenu.description += f"*{name}* - {ammount}\n" # Add to the embed
            await ctx.send(embed=stockmenu) # Send the embed



@bot.command() #Gen command
async def gen(ctx,name=None):
    if str(ctx.channel.id)in channel_id:
            if name == None:
                await ctx.send("Specify the account you want!") # Say error if no name specified
            else:
                name = name.lower()+".txt" #Add the .txt ext
                if name not in os.listdir("Accounts"): # If the name not in the directory
                    await ctx.send(f"Account does not exist. `{prefix}stock`")
                else:
                    with open("Accounts\\"+name) as file:
                        lines = file.read().splitlines() #Read the lines in the file
                    if len(lines) == 0: # If the file is empty
                        await ctx.send("These accounts are out of stock") #Send error if lines = 0
                    else:
                        with open("Accounts\\"+name) as file:
                            account = random.choice(lines) # Get a random line
                        try: #Try to send the account to the sender
                            await ctx.author.send(f"`{str(account)}`\n\nThis message will delete in {str(delete)} seconds!",delete_after=delete)
                        except: # If it failed send a message in the chat
                            await ctx.send("Failed to send! Turn on ur direct messages")
                        else: # If it sent the account, say so then remove the account from the file
                            await ctx.send("Sent the account to your inbox!")
                            with open("Accounts\\"+name,"w") as file:
                                file.write("") #Clear the file
                            with open("Accounts\\"+name,"a") as file:
                                for line in lines: #Add the lines back
                                    if line != account: #Dont add the account back to the file
                                        file.write(line+"\n") # Add other lines to file

@bot.command() #Gen command
async def add_item(ctx):
  if ctx.author.guild_permissions.administrator:
    if str(ctx.channel.id)in channel_id:
      #print("")
      def check(user):
        return user.channel == ctx.channel and user.author==ctx.author
  
      #args=ctx.content.split()
      #buyer=ctx.member
      await ctx.send("在庫が見られないように管理者だけのチャットで実行することをお勧めします。\nアイテムの名前を入力してください。\n例:Minecraft")
      try:
          user = await bot.wait_for("message",check=check,timeout=60)
          file_hozon=user.content.lower()
       
  
      except asyncio.TimeoutError:
          await ctx.send("タイムアウトしました。")
          return
      await ctx.send("在庫を入力してください:\n例:sample@gmail.com:12345")
      try:
          user = await bot.wait_for("message",check=check,timeout=60)
          try:
            with open("Accounts\\"+file_hozon+".txt","r") as file:
                binary_data=file.read()
          except:
              binary_data=""
          with open("Accounts\\"+file_hozon+".txt","a") as file:
            if binary_data=="":
              file.write(user.content)
            else:
              file.write('\n'+user.content)
          await ctx.send(f"{file_hozon}に{user.content} を追加しました。")
  
      except asyncio.TimeoutError:
          await ctx.send("タイムアウトしました。")
          return


@bot.command() #Gen command
async def stockdel(ctx,name=None):
    def check(user):
        return user.channel == ctx.channel and user.author==ctx.author
    if str(ctx.channel.id)in channel_id:
        if ctx.author.guild_permissions.administrator:
            if name == None:
                await ctx.send("hikisuu") # Say error if no name specified
            else:
                name = name.lower()+".txt" #Add the .txt ext
                await ctx.send("hontouniii?")
                try:
                    user = await bot.wait_for("message",check=check,timeout=60)
                    yesorno=user.content.lower()
                    if yesorno=="yes":
                        try:
                            import os
                            os.remove("Accounts/"+name)
                            await ctx.send("seikou")
                        except:
                            await ctx.send("sippai")
                    else:
                        await ctx.send("kyanseru")
            
                except asyncio.TimeoutError:
                    await ctx.send("タイムアウトしました。")
                    return
                
                

bot.run(token)
