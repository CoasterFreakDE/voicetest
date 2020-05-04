from discord.ext import commands


class JoinCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='join')
    async def join(self, ctx):
        print('Test')
        voicec = ctx.author.voice
        if voicec:
            channel = voicec.channel
            if channel:
                await channel.connect()


#######################################################


def setup(bot):
    bot.add_cog(JoinCommand(bot))
