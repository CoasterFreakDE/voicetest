import sys
import traceback

from discord.ext import commands


class MusicBot(commands.Bot):
    initial_extensions = ['cogs.joincommand',
                          'cogs.playcommand']

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        await self.process_commands(message)


#######################################################################

client = MusicBot(command_prefix=commands.when_mentioned_or('!'))

if __name__ == '__main__':
    for extension in client.initial_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

client.run('')
