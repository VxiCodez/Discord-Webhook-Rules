import requests
import discord_webhook
import socket
from discord_webhook import DiscordWebhook, DiscordEmbed


print('██     ██ ███████ ██████  ██   ██  ██████   ██████  ██   ██     ██████  ██    ██ ██      ███████ ███████ ')
print('██     ██ ██      ██   ██ ██   ██ ██    ██ ██    ██ ██  ██      ██   ██ ██    ██ ██      ██      ██      ')
print('██  █  ██ █████   ██████  ███████ ██    ██ ██    ██ █████       ██████  ██    ██ ██      █████   ███████ ')
print('██ ███ ██ ██      ██   ██ ██   ██ ██    ██ ██    ██ ██  ██      ██   ██ ██    ██ ██      ██           ██ ')
print(' ███ ███  ███████ ██████  ██   ██  ██████   ██████  ██   ██     ██   ██  ██████  ███████ ███████ ███████ ')
print('')
print('')
print('Webhook Rule Sender By: Vxi#0208')
webhook = input("Please enter the Webhook: ")



webhook = DiscordWebhook(url=webhook)
embed1 = DiscordEmbed(
    title='Rules. Please Read These Rules And Obey Them. @everyone',
    description=f'\n Please Read These Rules! \n \n 1. First Of All, Please Obey By Discord TOS So [Please Click Here To Read The Guidelines](https://discord.com/guidelines) [Please Click Here To Read TOS](https://discord.com/terms) \n \n 2. No Inappropriate Language \n The use of profanity should be kept to a minimum. However, any derogatory language towards any user is prohibited.  \n \n  3. No spamming \n Dont send a lot of small messages right after each other. Do not disrupt chat by spamming. \n \n 4. No pornographic/adult/other NSFW material \n This is a community server and not meant to share this kind of material. \n \n 5. No advertisements \n We do not tolerate any kind of advertisements, whether it be for other communities or streams. You can post your content in the media channel if it is relevant and provides actual value (Video/Art) \n \n 6. No offensive names and profile pictures \n You will be asked to change your name or picture if the staff deems them inappropriate. \n \n 7. Server Raiding \n Raiding or mentions of raiding are not allowed. \n \n 8. Direct & Indirect Threats \n \n 9. Please Dont Try Bypass Slurs By Using Fonts, Could Get You Banned \n \n Threats to other users of DDoS, Death, DoX, abuse, and other malicious threats are absolutely prohibited and disallowed. \n \n  The Admins and Mods will Mute/Kick/Ban per discretion. If you feel mistreated dm an Admin and we will resolve the issue.  \n \n All Channels will have pinned messages explaining what they are there for and how everything works. If you dont understand \n something, feel free to ask! \n \n Your presence in this server implies accepting these rules, including all further changes. These changes might be done at any time \n without notice, it is your responsibility to check for them.'
)

embed1.set_footer(text='Rules | Rules Made by Vxi#0208')

embed2 = DiscordEmbed(
    title='Please Read Below:',
    description=f'\n Please Feel Free To Add My Discord Bot [Please Click Here And Select The Server To Add Oreo](https://discord.com/api/oauth2/authorize?client_id=776530055412842526&permissions=8&scope=bot)  \n '
)

embed1.set_footer(text='Rules | Rules Made by Vxi#0208')

webhook.add_embed(embed1)
webhook.add_embed(embed2)
response = webhook.execute()
