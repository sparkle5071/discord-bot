import discord
from discord.ext import commands
from discord.ui import Button, View

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# メッセージ保存用（削除のため）
sent_message = None

# メッセージ内容
MESSAGE_1 = "🏠 部室で活動中"
MESSAGE_2 = "🎤 講堂で練習中"
MESSAGE_3 = "💤 活動終了"

class ActivityView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="部室", style=discord.ButtonStyle.primary, emoji="🏠")
    async def room_button(self, interaction: discord.Interaction, button: Button):
        global sent_message
        if sent_message:
            await sent_message.delete()
        sent_message = await interaction.channel.send(MESSAGE_1)
        await interaction.response.defer()

    @discord.ui.button(label="講堂", style=discord.ButtonStyle.success, emoji="🎤")
    async def hall_button(self, interaction: discord.Interaction, button: Button):
        global sent_message
        if sent_message:
            await sent_message.delete()
        sent_message = await interaction.channel.send(MESSAGE_2)
        await interaction.response.defer()

    @discord.ui.button(label="終了", style=discord.ButtonStyle.danger, emoji="💤")
    async def end_button(self, interaction: discord.Interaction, button: Button):
        global sent_message
        if sent_message:
            await sent_message.delete()
        sent_message = await interaction.channel.send(MESSAGE_3)
        await interaction.response.defer()

@bot.event
async def on_ready():
    print(f"✅ ログイン完了: {bot.user}")
    # Botが起動したときにボタン付きメッセージを送信する（固定チャンネルIDを設定）
    channel_id = 1387455934900469840  # ←送信先のチャンネルIDに置き換えて！
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send("🧭 活動場所を選んでください：", view=ActivityView())
import os
bot.run(os.getenv("DISCORD_TOKEN"))  # トークンは環境変数から読み取る！

