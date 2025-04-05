import telebot
from telebot import types

ImemologyI_bot = telebot.TeleBot('7443563348:AAESttLP8aIcH19qVNJGemb6oioMha8Ps64')

def create_keyboard():
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button1 = types.KeyboardButton('Новые мемы после 2020года')
    button2 = types.KeyboardButton('Старые мемы до 2020года')
    button3 = types.KeyboardButton('Выключить бота')
    button4 = types.KeyboardButton('ОценитьБота')
    keyboard.add(button1, button2, button3, button4)
    return keyboard

def create_keyboard2():
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button1 = types.KeyboardButton('крокодило бомбандиро')
    button2 = types.KeyboardButton('бомбини гусини')
    button3 = types.KeyboardButton('сияющий мага')
    button4 = types.KeyboardButton('грустный хомяк')
    button5 = types.KeyboardButton('чиловый парень')
    button6 = types.KeyboardButton('бобрито бондитто')
    button7 = types.KeyboardButton('Сидим с бобром за столом')
    button8 = types.KeyboardButton('хамстер комбат')
    button9 = types.KeyboardButton('турецкий стрелок')
    button10 = types.KeyboardButton('вы когда нибудь мечтали стать лучшей версией себя')
    button11 = types.KeyboardButton('Обратно в меню')
    keyboard.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11) 
    return keyboard


def create_keyboard3():
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button1 = types.KeyboardButton('Чикибамбони')
    button2 = types.KeyboardButton('THIS IS FINE')
    button3 = types.KeyboardButton('Денег нет но вы держитесь')
    button4 = types.KeyboardButton('ДОГИ')
    button5 = types.KeyboardButton('ЛЯГУШОНОК ПЕПЕ')
    button6 = types.KeyboardButton('Кандибобер')
    button7 = types.KeyboardButton('Троллфейс')
    button8 = types.KeyboardButton('Ждун')
    button9 = types.KeyboardButton('Наталья морская пехота')
    button10 = types.KeyboardButton('Чел с пальцем у виска')
    button11 = types.KeyboardButton('Обратно в меню')
    keyboard.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11) 
    return keyboard


@ImemologyI_bot.message_handler(commands=['start'])
def start(m, res = False):
    ImemologyI_bot.send_message(m.chat.id, 'Здравствуйте, этот бот рассказывает историю мемов.Про какой рассказать?', reply_markup = create_keyboard())

@ImemologyI_bot.message_handler(command=['usingMp3'])
def usingMp3(message):
    audio = open('./hak/bobrs.mp3', 'rb')



@ImemologyI_bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == "Новые мемы после 2020года":
        ImemologyI_bot.reply_to(message, "Который из них", reply_markup = create_keyboard2())
    elif message.text == "Старые мемы до 2020года":
        ImemologyI_bot.reply_to(message, "Который из них", reply_markup = create_keyboard3())
    elif message.text == "крокодило бомбандиро":
        ImemologyI_bot.reply_to(message, "Мем о крокодиле-бомбардировщике Bombardiro Crocodilo зародился в середине февраля 2025 года в TikTok.Первое видео с изображением и озвучкой Bombardiro Crocodilo опубликовал пользователь TikTok 20 февраля 2025 года. В ролике представлен созданный нейросетью образ бомбардировщика с лицом крокодила и итальянское описание")
        ImemologyI_bot.send_photo(message.chat.id, open('./hak/krokod.jpg','rb'))
        audio = open('./hak/krok.mp3', 'rb')
        ImemologyI_bot.send_audio(chat_id=message.chat.id, audio=audio, caption ="Описание")
        audio.close()
    elif message.text == "бомбини гусини":
        ImemologyI_bot.reply_to(message, "Бомбомбини Гузини (Бомбомбини Гуццини или Бумбамбини Гузини) — одно из итальянских животных созданным искусственным интеллектом, опубликованное в TikTok.Бомбомбини Гузини по канону является братом Бомбардиро Крокодило.Также он ненавидит своего брата.") 
        ImemologyI_bot.send_photo(message.chat.id, open('./hak/gysito.jpg','rb'))
        audio = open('./hak/gusi.mp3', 'rb')
        ImemologyI_bot.send_audio(chat_id=message.chat.id, audio=audio, caption ="Описание")
        audio.close()
    elif message.text == "сияющий мага":
        ImemologyI_bot.reply_to(message, "История мема начинается с публикации пользователя YouTube 28 декабря 2024 года. Он выложил короткий видеоролик с исполнителями лезгинки, используя фонк-музыку. Видео стало вирусным, собрав более 4 млн просмотров и почти 600 тысяч лайков. Вторым автором является пользователь rusNOrules. Он опубликовал видео с диалогом: «Что ты будешь делать, если тебя окружит толпа?» — «Сиять». Ролик набрал более 3 млн просмотров и 350 тысяч лайков, после чего стал популярным.")
        ImemologyI_bot.send_photo(message.chat.id, open('./hak/maga.jpg','rb'))
        audio = open('./hak/maga.mp3', 'rb')
        ImemologyI_bot.send_audio(chat_id=message.chat.id, audio=audio, caption ="Лучший из лучших")
        audio.close()
    elif message.text == "грустный хомяк":
        ImemologyI_bot.reply_to(message, "Считается, что автор мема позаимствовал фото и отредактировал его. Он увеличил хомяку глаза, сделав их огромными и пронзительными, а также немного изменил щёки, чтобы картинка получилась трогательной. После этого пользователь смонтировал небольшое видео, добавив музыку  и опубликовал.")
        ImemologyI_bot.send_photo(message.chat.id, open('./hak/grystni.jpg','rb'))
        audio = open('./hak/hom.mp3', 'rb')
        ImemologyI_bot.send_audio(chat_id=message.chat.id, audio=audio, caption ="Только не прослезитесь")
        audio.close()
    elif message.text == "чиловый парень":
        ImemologyI_bot.reply_to(message, "История мема начинается с публикации изображения художника Фила Бэнкса в социальных сетях. Бэнкс подписал работу словами: «Это мой новый персонаж — просто чилловый парень, которому на всё наплевать».")
        ImemologyI_bot.reply_to(message, "Настоящий успех пришёл к иллюстрации в августе 2024 года, когда пользователь TikTok  создал видео, использовав рисунок и трендовым звуком. Ролик мгновенно стал вирусным, собрав миллионы просмотров и вызвав всплеск интереса к образу.")
        ImemologyI_bot.send_photo(message.chat.id, open('./hak/chillguy.jpg','rb'))
        audio = open('./hak/guy.mp3', 'rb')
        ImemologyI_bot.send_audio(chat_id=message.chat.id, audio=audio, caption ="Кайф")
        audio.close()
    elif message.text == "бобрито бондитто":
        ImemologyI_bot.reply_to(message, "«Бобритто бандито» — одно из животных из вселенной крокодило бомбардиро, созданных искусственным интеллектом и опубликованных в TikTok. ")
        ImemologyI_bot.reply_to(message, "Описание мема: бобер-бандит в чёрном пиджаке, чёрных очках и шляпе, с автоматом «АК-47»")
        ImemologyI_bot.send_photo(message.chat.id, open('./hak/bobrbond.jpg','rb'))
        audio = open('./hak/bobond.mp3', 'rb')
        ImemologyI_bot.send_audio(chat_id=message.chat.id, audio=audio, caption ="Опасный бобр")
        audio.close()
    elif message.text == "Сидим с бобром за столом":
        ImemologyI_bot.reply_to(message, "Авторы песни «Бобр» (в которой есть фраза «Сидим с бобром за столом») — Вячеслав Скрипка и Андрей Попов. По словам Вячеслава Скрипки, идея трека родилась после того, как его друг написал прикольную музыку. Вдохновившись им, Скрипка сочинил текст про бобра")
        ImemologyI_bot.send_photo(message.chat.id, open('./hak/bobrstol.jpg','rb'))
        audio = open('./hak/bobrs.mp3', 'rb')
        ImemologyI_bot.send_audio(chat_id=message.chat.id, audio=audio, caption ="A вот и сама песня")
        audio.close()
    elif message.text == "хамстер комбат":
        ImemologyI_bot.reply_to(message, "Hamster Kombat — игра в стиле tap-to-earn («нажимай и зарабатывай»), которая была запущена 25 марта 2024 года и вскоре стала вирусной. Игра доступна в мессенджере Telegram.Популярность игры привела к созданию мемов. Пользователи создавали юмористические картинки, где в главной роли выступал хомяк, и шутили о том, что с помощью игры станут миллиардерами.")
        ImemologyI_bot.send_photo(message.chat.id, open('./hak/hamster.jpg','rb'))
    elif message.text == "турецкий стрелок":
        ImemologyI_bot.reply_to(message, "51-летний турецкий стрелок Юсуф Дикеч стал новым героем Сети после своего появления на Олимпиаде в Париже: вместо привычной спортивной экипировки он вышел на стрельбище в обычных очках и мятой футболке с логотипом своей страны. Рука в кармане и незаинтересованный в происходящем вид окончательно покорили публику — теперь его называются «турецкий батя» или «батя на отдыхе»")
        ImemologyI_bot.send_photo(message.chat.id, open('./hak/turkie.jpg','rb'))
    elif message.text == "вы когда нибудь мечтали стать лучшей версией себя":
        ImemologyI_bot.reply_to(message, "Изначально эта аудиодорожка использовалась в видеороликах с популярными персонажами, переживающими трансформацию. Например, момент, когда Шрек выпивал волшебное зелье и превращался в человека. Со временем мем приобрёл иронический оттенок. Пользователи социальных сетей начали сопоставлять совершенно различные, но созвучные или визуально схожие элементы. Например, Наполеона Бонапарта сравнивали с тортом, а Юлия Цезаря — с салатом.")
        ImemologyI_bot.send_photo(message.chat.id, open('./hak/sybstan.jpg','rb'))#Новые тут заканчиваютсЯ
        audio = open('./hak/sybst.mp3', 'rb')
        ImemologyI_bot.send_audio(chat_id=message.chat.id, audio=audio, caption ="Так фраза звучит в фильме Субстанция")
        audio.close()
    elif message.text == "Чикибамбони":
        ImemologyI_bot.reply_to(message, "это абстрактный мем, на котором изображена овца из компьютерной игры 'Майнкрафт'. Многие считают, что в далеком прошлом данное слово было синонимом великолепного настроения. Вероятно, неологизм был позаимствован из итальянского языка и является чем-то наподобие 'чики-пуки'")
        ImemologyI_bot.send_photo(message.chat.id, open('./hak/chiki.jpg','rb'))
        audio = open('./hak/chiki.mp3', 'rb')
        ImemologyI_bot.send_audio(chat_id=message.chat.id, audio=audio, caption ="A вот и сама песня")
        audio.close()
    elif message.text == "THIS IS FINE":
        ImemologyI_bot.reply_to(message, "В комиксе антропоморфный пёс сидит в доме за столом, окружённый языками пламени. « This is fine» («Всё в порядке»), — говорит он с улыбкой. « Я нормально отношусь к событиям, которые происходят вокруг», — добавляет герой, попивая чай из кружки. « Это окей, всё будет окей», — упорно твердит он, пока его шерсть не начинает гореть.")
        ImemologyI_bot.send_photo(message.chat.id, open('./hak/thisfine.jpg','rb'))
    elif message.text == "Денег нет но вы держитесь":
        ImemologyI_bot.reply_to(message, "Вы наверняка слышали эту фразу, но мало кто знает откуда она.«Денег нет, но вы держитесь» — краткое выражение, производное от фразы, произнесённой в мае 2016 года председателем правительства России Дмитрием Медведевым во время визита в Крым в ответ на жалобу пенсионерки о маленьком размере пенсии.")
        ImemologyI_bot.send_photo(message.chat.id, open('./hak/medved.jpg','rb'))
        audio = open('./hak/deneg.mp3', 'rb')
        ImemologyI_bot.send_audio(chat_id=message.chat.id, audio=audio, caption ="Тяжела жизнь")
        audio.close()
    elif message.text == "ДОГИ":
        ImemologyI_bot.reply_to(message, "23 февраля 2010 года воспитательница японского детского сада Ацуко Сато опубликовала в своём блоге несколько фотографий Кабосу, среди которых была и картинка с поднятой бровью, ставшая основой мема. 28 октября 2010 года фото собаки появилось на сайте Reddit с подписью LMBO LOOK THIS FUKKIN DOGE. Распространение мема: в апреле 2012 года пользователь с ником Leonsumbitches опубликовал на сайте Tumblr аудиофайл, который представлял собой произнесённый компьютерным голосом отрывок текста, в котором были написаны некоторые команды для пошаговой игры.")
        ImemologyI_bot.send_photo(message.chat.id, open('./hak/dogo.jpg','rb'))
    elif message.text == "ЛЯГУШОНОК ПЕПЕ":
        ImemologyI_bot.reply_to(message, "Лягушонок Пепе — популярный интернет-мем, изображающий зелёную антропоморфную лягушку. Персонаж может выражать различные эмоции: печаль, меланхолию, гнев, удивление и другие.")
        ImemologyI_bot.reply_to(message, "История мема: Впервые появился в 2005 году в серии комиксов художника Мэтта Фьюри. На оригинальных изображениях лягушонок улыбался.В 2008 году картинку с персонажем запостили , где лягушонка раскрасили в привычный зелёный цвет.В 2009 году с помощью фотошопа лягушонка сделали грустным, опустив уголки губ вниз.")
        ImemologyI_bot.reply_to(message, "Значение мема:часто лягушонок Пепе встречается с выражением «тебе никогда не узнать, как» выполнять какое-то действие. Иногда к картинке с персонажем добавляют надпись о чём-то печальном ")
        ImemologyI_bot.send_photo(message.chat.id, open('./hak/pepe.jpg','rb'))
        audio = open('./hak/pepe.mp3', 'rb')
        ImemologyI_bot.send_audio(chat_id=message.chat.id, audio=audio, caption ="музычка")
        audio.close()
    elif message.text == "Кандибобер":
        ImemologyI_bot.reply_to(message, "История мема «Кандибобер» началась с репортажа минских журналистов в 2010 году. Они проводили опрос среди прохожих о самых странных именах. Журналистка задала вопрос: «Людей с какими редкими именами вы встречали в жизни?». Женщина ответила: «Как вам сказать... Я прожила довольно долгую жизнь... Ибрагим вам что-нибудь говорит? Прекрасное имя. Аллах акбар. Я прошла Афганскую войну. И я желаю всем мужчинам пройти её. Мужчина определяется делом, а не словом. И если я ношу кандибобер на голове, это не значит, что я женщина или балерина».")
        ImemologyI_bot.send_photo(message.chat.id, open('./hak/kandibob.jpg','rb'))
        audio = open('./hak/kand.mp3', 'rb')
        ImemologyI_bot.send_audio(chat_id=message.chat.id, audio=audio, caption ="Культовая фраза этого мема")
        audio.close()
    elif message.text == "Троллфейс":
        ImemologyI_bot.reply_to(message, "Trollface был нарисован 18-летним студентом Оклендского колледжа Карлосом Рамиресом 19 сентября 2008 года в Microsoft Paint. Изображение было опубликовано на странице Рамиреса в DeviantArt, как часть комикса под названием «Trolls», повествующего о бессмысленном характере троллинга.")
        ImemologyI_bot.send_photo(message.chat.id, open('./hak/trollface.jpg','rb'))
    elif message.text == "Ждун":
        ImemologyI_bot.reply_to(message, "«Ждун» (настоящее имя — Homunculus loxodontus) — скульптура голландской художницы Маргрит ван Бреворт, созданная весной 2016 года для Лейденского университета (Нидерланды).  Изначально идея состояла в том, чтобы изобразить что-то, связанное с исследованиями и процедурами. Но художница обратила внимание на людей, которые сидят в очереди к врачу в ожидании диагноза, и решила посвятить скульптуру пациентам.")
        ImemologyI_bot.send_photo(message.chat.id, open('./hak/schdyn.jpg','rb'))
    elif message.text == "Наталья морская пехота":
        ImemologyI_bot.reply_to(message, "В 2013 году в сети появилось видео с женщиной, которая уверяла, что служила в морской пехоте. В кадре героиня просит денег на проезд и, получив отказ, начинает довольно экспрессивно выражать недовольство. Её манера речи, в которой изысканно смешались обсценная лексика с театральной уверенностью, сразу привлекла внимание интернет-пользователей и цитаты мгновенно разлетелись на мемы.")
        ImemologyI_bot.send_photo(message.chat.id, open('./hak/Natali.jpg','rb'))
        audio = open('./hak/natali.mp3', 'rb')
        ImemologyI_bot.send_audio(chat_id=message.chat.id, audio=audio, caption ="Гордое заявление женщины")
        audio.close()
    elif message.text == "Чел с пальцем у виска":
        ImemologyI_bot.reply_to(message, "Актёр Кайод Овуми (Kayode Ewumi) играл в нём Риза Симпсона по прозвищу Roll Safe. В одной из серий Риз рассказывает о своей девушке Рейчел, которую считает очень умной, и в этот момент прикладывает палец к виску")
        ImemologyI_bot.send_photo(message.chat.id, open('./hak/negr.jpg','rb'))
    elif message.text == "Обратно в меню":
	    ImemologyI_bot.reply_to(message, "Про какие мемы вам рассказать?", reply_markup = create_keyboard())    
    elif message.text == "Выключить бота":
	    ImemologyI_bot.reply_to(message, "Досвидания", reply_markup=types.ReplyKeyboardRemove(selective=False))
    elif message.text == "ОценитьБота":
            ImemologyI_bot.reply_to(message, "https://docs.google.com/forms/d/e/1FAIpQLSfFlHUVP1TVqiHryQEa_M8K0DMLvEN7KqbyH6NfHITkESN-8g/viewform?usp=dialog")
            ImemologyI_bot.send_photo(message.chat.id, open('./hak/qr.png', 'rb'))
    





        
ImemologyI_bot.polling(none_stop=True, interval=0)

   
