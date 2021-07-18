import requests
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, executor, types



bot = Bot('<TOKEN>', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)



@dp.message_handler(commands=['crypto'], commands_prefix="!/.")
async def crypto(message: types.Message):
    CRYPTO = 'https://coinmarketcap.com/ru/all/views/all/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'}


    full_page = requests.get(CRYPTO)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    last = soup.findAll("a", {"href": "/ru/currencies/bitcoin/markets/", "class": "cmc-link"})
    last2 = soup.findAll("a", {"href": "/ru/currencies/ethereum/markets/", "class": "cmc-link"})
    last3 = soup.findAll("a", {"href": "/ru/currencies/tron/markets/", "class": "cmc-link"})
    last4 = soup.findAll("a", {"href": "/ru/currencies/aave/markets/", "class": "cmc-link"})
    last5 = soup.findAll("a", {"href": "/ru/currencies/monero/markets/", "class": "cmc-link"})
    last6 = soup.findAll("a", {"href": "/ru/currencies/litecoin/markets/", "class": "cmc-link"})
    last7 = soup.findAll("a", {"href": "/ru/currencies/neo/markets/", "class": "cmc-link"})
    last8 = soup.findAll("a", {"href": "/ru/currencies/dash/markets/", "class": "cmc-link"})


    sentence = last[0].text
    sentence2 = last2[0].text
    sentence3 = last3[0].text
    sentence4 = last4[0].text
    sentence5 = last5[0].text
    sentence6 = last6[0].text
    sentence7 = last7[0].text
    sentence8 = last8[0].text


    CryptoMessage = f"Вот актуальный курс крипты:\n"\
                    f"<b>Bitcoin</b>: <code>{sentence}</code>\n"\
                    f"<b>Ethereum</b>: <code>{sentence2}</code>\n"\
                    f"<b>Tron</b>: <code>{sentence3}</code>\n"\
                    f"<b>Aave</b>: <code>{sentence4}</code>\n"\
                    f"<b>Monero</b>: <code>{sentence5}</code>\n"\
                    f"<b>Litecoin</b>: <code>{sentence6}</code>\n"\
                    f"<b>Neo</b>: <code>{sentence7}</code>\n"\
                    f"<b>Dash</b>: <code>{sentence8}</code>"
    await message.answer(CryptoMessage)


@dp.message_handler(commands=['covid'])
async def covid(message: types.Message):

    markup = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton('Россия', callback_data='ru')
    item2 = types.InlineKeyboardButton('Украина', callback_data='ua')
    item3 = types.InlineKeyboardButton('Казахстан', callback_data='kz')
    item4 = types.InlineKeyboardButton('Беларусь', callback_data='be')


    markup.add(item,item2)
    markup.add(item3,item4)


    world = "https://index.minfin.com.ua/reference/coronavirus/geography/"
    soup5 = BeautifulSoup(requests.get(world).content, "html.parser")
    convertg = soup5.findAll("td", {"class": "bg-total larger", "align": "right"})
    converth = soup5.findAll("td", {"class": "bg-total", "align": "right"})


    KAZAKHSTAN = f"📈 <b>ВЕСЬ МИР</b>\n"\
                 f"🧟 Заражённых: <code>{convertg[0].text}</code>\n"\
                 f"😵 Смертей: <code>{converth[1].text}</code>\n"\
                 f"😷 Выздоровело: <code>{converth[2].text}</code>\n"\
                 f"🤒 Болеют: <code>{converth[3].text}</code>"
    await message.answer(KAZAKHSTAN, reply_markup=markup)




@dp.callback_query_handler(lambda call: True)
async def callback_inline(call):
    if call.message:
        if call.data == 'kz':

            markup = types.InlineKeyboardMarkup()
            item = types.InlineKeyboardButton('Назад', callback_data='wr')

            markup.add(item)

            kazakhstan = "https://index.minfin.com.ua/reference/coronavirus/geography/kazakhstan/"
            soup1 = BeautifulSoup(requests.get(kazakhstan).content, "html.parser")
            convert1 = soup1.findAll("strong", {"class": "black"})
            convert2 = soup1.findAll("strong", {"class": "red"})
            convert3 = soup1.findAll("strong", {"class": "green"})
            convert4 = soup1.findAll("strong", {"class": "blue"})


            KAZAKHSTAN =f"📈 <b>КАЗАХСТАН</b>\n"\
                        f"🧟 Заражённых: <code>{convert1[0].text}</code>\n"\
                        f"😵 Смертей: <code>{convert2[0].text}</code>\n"\
                        f"😷 Выздоровело: <code>{convert3[0].text}</code>\n"\
                        f"🤒 Болеют: <code>{convert4[0].text}</code>"
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=KAZAKHSTAN, reply_markup=markup)
        
        elif call.data == 'ru':
            markup = types.InlineKeyboardMarkup()
            item = types.InlineKeyboardButton('Назад', callback_data='wr')

            markup.add(item)


            russian = "https://index.minfin.com.ua/reference/coronavirus/geography/russia/"
            soup1 = BeautifulSoup(requests.get(russian).content, "html.parser")
            convert1 = soup1.findAll("strong", {"class": "black"})
            convert2 = soup1.findAll("strong", {"class": "red"})
            convert3 = soup1.findAll("strong", {"class": "green"})
            convert4 = soup1.findAll("strong", {"class": "blue"})


            KAZAKHSTAN =f"📈 <b>РОССИЯ</b>\n"\
                        f"🧟 Заражённых: <code>{convert1[0].text}</code>\n"\
                        f"😵 Смертей: <code>{convert2[0].text}</code>\n"\
                        f"😷 Выздоровело: <code>{convert3[0].text}</code>\n"\
                        f"🤒 Болеют: <code>{convert4[0].text}</code>"

            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=KAZAKHSTAN, reply_markup=markup)
            
        elif call.data == 'ua':
            markup = types.InlineKeyboardMarkup()
            item = types.InlineKeyboardButton('Назад', callback_data='wr')

            markup.add(item)


            ukraine = "https://index.minfin.com.ua/reference/coronavirus/ukraine/"
            soup1 = BeautifulSoup(requests.get(ukraine).content, "html.parser")
            convert1 = soup1.findAll("strong", {"class": "black"})
            convert2 = soup1.findAll("strong", {"class": "red"})
            convert3 = soup1.findAll("strong", {"class": "green"})
            convert4 = soup1.findAll("strong", {"class": "blue"})


            KAZAKHSTAN =f"📈 <b>УКРАИНА</b>\n"\
                        f"🧟 Заражённых: <code>{convert1[0].text}</code>\n"\
                        f"😵 Смертей: <code>{convert2[0].text}</code>\n"\
                        f"😷 Выздоровело: <code>{convert3[0].text}</code>\n"\
                        f"🤒 Болеют: <code>{convert4[0].text}</code>"

            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=KAZAKHSTAN, reply_markup=markup)

        elif call.data == 'be':
            markup = types.InlineKeyboardMarkup()
            item = types.InlineKeyboardButton('Назад', callback_data='wr')

            markup.add(item)


            belarus = "https://index.minfin.com.ua/reference/coronavirus/geography/belarus/"
            soup1 = BeautifulSoup(requests.get(belarus).content, "html.parser")
            convert1 = soup1.findAll("strong", {"class": "black"})
            convert2 = soup1.findAll("strong", {"class": "red"})
            convert3 = soup1.findAll("strong", {"class": "green"})
            convert4 = soup1.findAll("strong", {"class": "blue"})


            KAZAKHSTAN =f"📈 <b>БЕЛАРУСЬ</b>\n"\
                        f"🧟 Заражённых: <code>{convert1[0].text}</code>\n"\
                        f"😵 Смертей: <code>{convert2[0].text}</code>\n"\
                        f"😷 Выздоровело: <code>{convert3[0].text}</code>\n"\
                        f"🤒 Болеют: <code>{convert4[0].text}</code>"

            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=KAZAKHSTAN, reply_markup=markup)

        elif call.data == 'wr':
            markup = types.InlineKeyboardMarkup()
            item = types.InlineKeyboardButton('Россия', callback_data='ru')
            item2 = types.InlineKeyboardButton('Украина', callback_data='ua')
            item3 = types.InlineKeyboardButton('Казахстан', callback_data='kz')
            item4 = types.InlineKeyboardButton('Беларусь', callback_data='be')

            markup.add(item,item2)
            markup.add(item3,item4)


            world = "https://index.minfin.com.ua/reference/coronavirus/geography/"
            soup1 = BeautifulSoup(requests.get(world).content, "html.parser")
            convertg = soup1.findAll("td", {"class": "bg-total larger", "align": "right"})
            converth = soup1.findAll("td", {"class": "bg-total", "align": "right"})


            KAZAKHSTAN =f"📈 <b>ВЕСЬ МИР</b>\n"\
                        f"🧟 Заражённых: <code>{convertg[0].text}</code>\n"\
                        f"😵 Смертей: <code>{converth[1].text}</code>\n"\
                        f"😷 Выздоровело: <code>{converth[2].text}</code>\n"\
                        f"🤒 Болеют: <code>{converth[3].text}</code>"

            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=KAZAKHSTAN, reply_markup=markup)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
