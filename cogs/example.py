"""Example cog."""
import gearbox
cog = gearbox.Cog('example')

@cog.command
@cog.alias('hi')
def hello(author):
    """Say hello."""
    return f'Hello, {author.name}!'
