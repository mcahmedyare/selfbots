import asyncio
from discord.ext import commands
from discord.ext.self import Self

bot_token1 = "ODg1NzQ3MzQ4NjE2MTM4NzUy.YTrigg.5fvGU1tnR6365XGA4kG4gfCkwmo"
bot_token2 = "ODg1NzQ3MzM3MTE1MzM2NzI1.YTrifw.vIxkytzMv40fTokDxRyteTDhwGY"
redirect_channel_id = "1067197395298955350"

class RedirectSelfBot(Self):
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        redirect_channel = self.get_channel(redirect_channel_id)
        await redirect_channel.send(message.content)

bot1 = RedirectSelfBot(command_prefix='!')
bot2 = RedirectSelfBot(command_prefix='!')

async def run_bot(bot, token):
    await bot.start(token)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(run_bot(bot1, bot_token1)),
        loop.create_task(run_bot(bot2, bot_token2)),
    ]
    loop.run_until_complete(asyncio.wait(tasks))