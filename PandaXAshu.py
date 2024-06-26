from datetime import datetime, timedelta
from pytz import timezone
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from config import Config
from aiohttp import web
from route import web_server
import requests
import asyncio

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="renamer",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username  
        self.uptime = Config.BOT_UPTIME     
        if Config.WEBHOOK:
            app = web.AppRunner(await web_server())
            await app.setup()       
            await web.TCPSite(app, "0.0.0.0", Config.PORT).start()     
        print(f"{me.first_name} Is Started.....✨️")
        for id in Config.ADMIN:
            try:
                await self.send_message(Config.LOG_CHANNEL, f"**{me.first_name} Is Started.....✨️**")                                
            except Exception as e:
                print(f"Error sending start message: {str(e)}")
        if Config.LOG_CHANNEL:
            try:
                await self.send_redeploy_message(me)

                # Schedule redeployment after 90 minutes
                await self.schedule_redeploy()

            except Exception as e:
                print(f"Error sending redeploy message: {str(e)}")
                print("Please Make This Is Admin In Your Log Channel")

    async def send_redeploy_message(self, me):
        try:
            curr = datetime.now(timezone("Asia/Kolkata"))
            date = curr.strftime('%d %B, %Y')
            time = curr.strftime('%I:%M:%S %p')
            await self.send_message(Config.REDEPLOY, f"**{me.mention} Is Restarted !!**\n\n📅 Date : `{date}`\n⏰ Time : `{time}`\n🌐 Timezone : `Asia/Kolkata`\n\n🉐 Version : `v{__version__} (Layer {layer})`</b>")
            await self.send_message(Config.FLOG_CHANNEL, f"{me.mention}-{time}")
        except Exception as e:
            print(f"Error sending redeploy message: {str(e)}")

    async def schedule_redeploy(self):
        while True:
            try:
                # Sleep for 90 minutes
                await asyncio.sleep(5400)

                # Redeploy the app
                await self.redeploy_app()

            except Exception as e:
                print(f"Error in redeployment schedule: {str(e)}")

    async def redeploy_app(self):
        try:
            print("Redeploying the app...")
            await self.send_message(Config.REDEPLOY, f"**{me.mention} Is Redeploying !!`</b>")
            response = requests.post(Config.REDEPLOY_URL)
            if response.status_code == 200:
                print("App redeployed successfully!")
                await self.send_message(Config.REDEPLOY, f"**{me.mention} Is Redeploying successfully!!!`</b>")
            else:
                print(f"Failed to redeploy app. Status code: {response.status_code}")
                await self.send_message(Config.REDEPLOY, f"**{me.mention} Is Redeploying Failed!!!`</b>")

        except Exception as e:
            print(f"Error redeploying app: {str(e)}")

# Instantiate and run the Bot
Bot().run()

# ʀᴀᴘᴏ ᴄʀᴇᴀᴛᴏʀ https://github.com/AshutoshGoswami24
# ʀᴀᴘᴏ https://github.com/AshutoshGoswami24/Rename-Bot




# from datetime import datetime
# from pytz import timezone
# from pyrogram import Client, __version__
# from pyrogram.raw.all import layer
# from config import Config
# from aiohttp import web
# from route import web_server

# class Bot(Client):
#     def __init__(self):
#         super().__init__(
#             name="renamer",
#             api_id=Config.API_ID,
#             api_hash=Config.API_HASH,
#             bot_token=Config.BOT_TOKEN,
#             workers=200,
#             plugins={"root": "plugins"},
#             sleep_threshold=15,
#         )

#     async def start(self):
#         await super().start()
#         me = await self.get_me()
#         self.mention = me.mention
#         self.username = me.username
#         self.uptime = Config.BOT_UPTIME
#         if Config.WEBHOOK:
#             app = web.Application()
#             app.router.add_route('GET', '/', web_server)
#             runner = web.AppRunner(app)
#             await runner.setup()
#             site = web.TCPSite(runner, "0.0.0.0", 8080)
#             await site.start()
#         print(f"{me.first_name} Is Started.....✨️")
#         for admin_id in Config.ADMIN:
#             try:
#                 await self.send_message(admin_id, f"**{me.first_name} Is Started.....✨️**")
#             except Exception as e:
#                 print(f"Error sending message to admin {admin_id}: {e}")
#         if Config.LOG_CHANNEL:
#             try:
#                 curr = datetime.now(timezone("Asia/Kolkata"))
#                 date = curr.strftime('%d %B, %Y')
#                 time = curr.strftime('%I:%M:%S %p')
#                 await self.send_message(Config.LOG_CHANNEL, f"**{me.mention} Is Restarted !!**\n\n📅 Date : `{date}`\n⏰ Time : `{time}`\n🌐 Timezone : `Asia/Kolkata`\n\n🉐 Version : `v{__version__} (Layer {layer})`</b>")
#                 await self.send_message(Config.FLOG_CHANNEL, f"{me.mention}-{time}")
#             except Exception as e:
#                 print(f"Error sending log message: {e}")

# if __name__ == "__main__":
#     Bot().run()




# from datetime import datetime
# from pytz import timezone
# from pyrogram import Client, __version__
# from pyrogram.raw.all import layer
# from config import Config
# from aiohttp import web
# from route import web_server

# class Bot(Client):

#     def __init__(self):
#         super().__init__(
#             name="renamer",
#             api_id=Config.API_ID,
#             api_hash=Config.API_HASH,
#             bot_token=Config.BOT_TOKEN,
#             workers=200,
#             plugins={"root": "plugins"},
#             sleep_threshold=15,
#         )

#     async def start(self):
#         await super().start()
#         me = await self.get_me()
#         self.mention = me.mention
#         self.username = me.username  
#         self.uptime = Config.BOT_UPTIME     
#         if Config.WEBHOOK:
#             app = web.AppRunner(await web_server())
#             await app.setup()       
#             await web.TCPSite(app, "0.0.0.0", 8080).start()     
#         print(f"{me.first_name} Is Started.....✨️")
#         for id in Config.ADMIN:
#             try: await self.send_message(Config.LOG_CHANNEL, f"**{me.first_name}  Is Started.....✨️**")                                
#             except: pass
#         if Config.LOG_CHANNEL:
#             try:
#                 curr = datetime.now(timezone("Asia/Kolkata"))
#                 date = curr.strftime('%d %B, %Y')
#                 time = curr.strftime('%I:%M:%S %p')
#                 await self.send_message(Config.LOG_CHANNEL, f"**{me.mention} Is Restarted !!**\n\n📅 Date : `{date}`\n⏰ Time : `{time}`\n🌐 Timezone : `Asia/Kolkata`\n\n🉐 Version : `v{__version__} (Layer {layer})`</b>")
#                 await self.send_message(Config.FLOG_CHANNAL, f"{me.mention}-{time}")
#             except:
#                 print("Please Make This Is Admin In Your Log Channel")

# Bot().run()



# # PandaWep
# # Don't Remove Credit 🥺
# # Telegram Channel @PandaWep
# # Developer https://github.com/PandaWep
