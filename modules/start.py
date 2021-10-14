from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types.bots_and_keyboards.callback_query import CallbackQuery
from pyrogram.types.messages_and_media.message import Message
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_img = 'https://telegra.ph/file/46afce7b8d597048fcc25.jpg'

start_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Look inside 👀", callback_data="start_inside")]])
callinside_markup = InlineKeyboardMarkup([[InlineKeyboardButton("How To use?", callback_data="start_how"),
                                          InlineKeyboardButton("Contact Owner", callback_data="start_owner"),
                                          InlineKeyboardButton("Whats New?", callback_data="start_new")],
                                          [InlineKeyboardButton("Back 🔙", callback_data="start_back")]])
back_one = InlineKeyboardMarkup([[InlineKeyboardButton("Back 🔙", callback_data="back_one")]])

@bot.on_message(filters.command(['start']) & ( filters.private |  filters.user("nousername_psycho")))
async def start(__, m:Message):
    user_id = m.from_user.id
    user_name = m.from_user.first_name
    usr_mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    await m.reply_photo(photo=start_img,
                        caption=f"Hello {usr_mention} 👋, Private usage strictly restricted."
                                "if you want to download any song you should join our group Mallu Music Corner "
                                "\n\nAre you intrested in bots? We can make bots with your own needs. contact us : @nousername_pycho",
                        reply_markup=start_markup)
    
@bot.on_callback_query(filters.regex("start_inside"))
async def cal_start_inside(__, c:CallbackQuery):
    await c.message.delete()
    await c.message.reply_text("Oh wow 🤩, I'm glad you want to know more about me. "
                               "Well, I am a telegram bot running on python3 with pyrogram framework. "
                               "We are using Youtube Dl For downloading Music and elephant Sql For Database.\n",
                               reply_markup=callinside_markup)
    
@bot.on_callback_query(filters.regex("start_how"))
async def cal_start_how(__, c:CallbackQuery):
    await c.message.delete()
    await c.message.reply_text("**Okay, I will help you. ✋**\n\n"
                               "First of all you should know the process happening behind the bot. "
                               "If you type `/song - song name`, bot will catch song name and it will try to get results from YouTube with that keyword. "
                               "And the first result return as an audio. Cool? "
                               "But the problem is if you type wrong song name it will act like same and the result is absolutely wrong. "
                               "So we added a new specific features. What's that? "
                               "If you don't know the song name correctly just copy YouTube video link and paste it in our group. Bot will fetch the audio"
                               "\n\n**Song Command - Examples** "
                               "⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n"
                                "⌊ `/song closer` \n"
                                "⌊ `/song Justin Bieber - Sorry` \n"
                                "⌊ `/song Alan Walker - Faded` \n"
                                "⌊ `/song Imagine Dragons - Thunder` \n"
                                "⌊ `/song Doja Cat - Boss B*tch ` \n"
                                "⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n"
                                "\n**Song Request Tips**"
                                "\n⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n"
                                "⌊ if you type song name only it will fetch the full song, but song name + lyric will fetch the lyric song. "
                                "So you can avoid cinematic dialogue from the song.\n"
                                "\n⌊ You can use `@vid` as inline for search, YouTube video links (it will help you to get the song name correctly) \n"
                                "⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯\n\n"
                                "©️ MalluMusicCorner",
                               reply_markup=back_one)

@bot.on_callback_query(filters.regex("back_one"))
async def back1(__, c:CallbackQuery):
    await c.message.edit("Oh wow 🤩, I'm glad you want to know more about me. "
                               "Well, I am a telegram bot running on python3 with pyrogram framework. "
                               "We are yousing Youtube Dl For downloading Music and elephant Sql For Database.\n",
                               reply_markup=callinside_markup)
    
@bot.on_callback_query(filters.regex("start_owner"))
async def owner(__, c:CallbackQuery):
    await c.message.edit("Hai 👋 conatact me if you want to create you own bot. (paid) else contact me in our group\n\n my id: @nousername_psycho",
                               reply_markup=back_one)
    
@bot.on_callback_query(filters.regex("start_new"))
async def new(__, c:CallbackQuery):
    await c.message.edit("**Whats new? 🆕**\n\n"
                         "⌊ Recently we added new Song Recognition🔥\n"
                         "⌊ Added Database (Speed Up Bot)🔥\n"
                         "⌊ Increased Bot Upload Speed🔥\n"
                         "⌊ More in Future \n"
                         "\n\n**What is Song Recognition?**"
                         "\n\nIdentify Song from a Video.? it's also possible, just send "
                         "a short video in our group, then type `/find` cmd reply to your video. Bot will try to fetch the song.",
                               reply_markup=back_one)
    
@bot.on_callback_query(filters.regex("start_back"))
async def main(__, c:CallbackQuery):
    user_id = c.from_user.id
    user_name = c.from_user.first_name
    usr_mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    await c.message.delete()
    await c.message.reply_photo(photo=start_img,
                        caption=f"Hello {usr_mention} 👋, Private usage strictly restricted."
                                "if you want to download any song you should join our group "
                                "\n\nAre you intrested in bots? We can make bots with your own needs. contact us : @nousername_pycho",
                        reply_markup=start_markup)
    
    
