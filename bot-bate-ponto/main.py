import discord
from discord.ext import commands
from datetime import datetime

# Configuração dos intents
intents = discord.Intents.default()
intents.message_content = True  # recebimento das mensagens

# criação do bot com os intents configurados
bot = commands.Bot(command_prefix="!", intents=intents)

# armazenar o tempo de início de cada usuário
start_times = {}

# ID do canal para enviar a mensagem de ponto finalizado
TARGET_CHANNEL_ID = 0000000000000000

class FinalizarButton(discord.ui.View):
    def __init__(self, user_id):
        super().__init__(timeout=86400)  # Timeout de 24 horas (86.400 segundos)
        self.user_id = user_id

    @discord.ui.button(label="Finalizar", style=discord.ButtonStyle.danger)
    async def finalizar(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != self.user_id:
            await interaction.response.send_message("Você não pode finalizar o ponto de outra pessoa!", ephemeral=True)
            return

        # Responde à interação imediatamente para evitar timeout
        await interaction.response.send_message("Ponto finalizado, verifique as informações: https://discord.com/channels/1146919829463375872/1275953051672379507", ephemeral=False)

        # Continua o processamento de forma assíncrona
        await self.process_finalization(interaction)

    async def process_finalization(self, interaction: discord.Interaction):
        user_id = interaction.user.id
        mention = interaction.user.mention
        end_time = datetime.now()
        start_time = start_times.pop(user_id)
        total_time = end_time - start_time

        total_minutes, total_seconds = divmod(total_time.total_seconds(), 60)
        total_hours, total_minutes = divmod(total_minutes, 60)
        
        # Formatação do tempo total trabalhado
        hora_str = f"{int(total_hours)} horas" if total_hours > 1 else "1 hora" if total_hours == 1 else ""
        minuto_str = f"{int(total_minutes)} minutos" if total_minutes > 1 else "1 minuto" if total_minutes == 1 else ""

        formatted_total_time = f"{hora_str} e {minuto_str}" if hora_str and minuto_str else hora_str or minuto_str or "0 minutos"

        embed = discord.Embed(
            description=f"> **👋 Olá, {mention}!\n> ✔ Seu ponto foi finalizado com sucesso!**\n\n"
                        f"Entrada:\n```{start_time.strftime('%d/%m/%Y')} às {start_time.strftime('%H:%M:%S')}```\n"
                        f"Saída:\n```{end_time.strftime('%d/%m/%Y')} às {end_time.strftime('%H:%M:%S')}```\n"
                        f"Tempo total de serviço:\n```{formatted_total_time}```\n",
        
            color=discord.Color.red()
        )
        embed.set_thumbnail(url=interaction.user.avatar.url)
        embed.set_footer(text="Finalizado")
        embed.set_image(url="https://cdn.discordapp.com/attachments/1031210812301385821/1276259144659374111/Rosa_Amarelo_e_Preto_Gamer_Grunge_Banner_para_Twitch_4_1.png?ex=66c8e073&is=66c78ef3&hm=4939a2df3b78fe4b604d16b8b4e6041c222eb3d3efed10240ceb7e1e06b8e305&")

        channel = bot.get_channel(TARGET_CHANNEL_ID)
        if channel is not None:
            await channel.send(embed=embed)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command(name='iniciar')
async def iniciar(ctx):
    user_id = ctx.author.id
    mention = ctx.author.mention
    user_avatar = ctx.author.avatar.url
    if user_id in start_times:
        start_time = start_times[user_id].strftime("%H:%M:%S")
        date_str = start_times[user_id].strftime("%d/%m/%Y")
        embed = discord.Embed(
            description=f"> **👋 Olá, {mention}!**\n> **✔ Seu ponto foi iniciado com sucesso!**\n\n"
                        f"Entrada:\n```{date_str} às {start_time}```\nLembre-se:\n"
                        f"```O tempo mínimo de trabalho aceito é de 1 hora.```",
            color=3066993
        )
        embed.set_thumbnail(url=user_avatar)
        embed.set_footer(text="Em andamento...")
        embed.set_image(url="https://cdn.discordapp.com/attachments/1031210812301385821/1276250047096553472/Rosa_Amarelo_e_Preto_Gamer_Grunge_Banner_para_Twitch_2_2.png?ex=66c8d7fa&is=66c7867a&hm=7555feef3b5fd5e5da73e3f1b3be1ee9fde6115abf8c71ad170e5de5e23ce0e6")
        await ctx.send(embed=embed, view=FinalizarButton(user_id))
    else:
        start_times[user_id] = datetime.now()
        start_time = start_times[user_id].strftime("%H:%M:%S")
        date_str = start_times[user_id].strftime("%d/%m/%Y")
        embed = discord.Embed(
            description=f"> **👋 Olá, {mention}!**\n> **✔ Seu ponto foi iniciado com sucesso!**\n\n"
                        f"Entrada:\n```{date_str} às {start_time}```\nLembre-se:\n"
                        f"```O tempo mínimo de trabalho aceito é de 1 hora.```",
            color=3066993
        )
        embed.set_thumbnail(url=user_avatar)
        embed.set_footer(text="Em andamento...")
        embed.set_image(url="https://cdn.discordapp.com/attachments/1031210812301385821/1276250047096553472/Rosa_Amarelo_e_Preto_Gamer_Grunge_Banner_para_Twitch_2_2.png?ex=66c8d7fa&is=66c7867a&hm=7555feef3b5fd5e5da73e3f1b3be1ee9fde6115abf8c71ad170e5de5e23ce0e6")
        await ctx.send(embed=embed, view=FinalizarButton(user_id))

# Token do bot
bot.run('DISCORD_TOKEN')
