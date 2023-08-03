
![logo](ReadmeFolder.jpg)

## Telegram bot as an ad builder
### Introduction:
In the course of writing and designing posts for telegram, users face a number of problems
(at the moment, the usual preparation of posts takes place either with difficulty in the messenger or
editing through other documents), I also wanted to be not tied
to a smartphone or PC for more comfortable writing. To solve this problem
and to spend as little time on it as possible, the idea of creating this bot appeared.
The bot is an auxiliary moderator tool for faster
compilation of posts and sending them to the channel. First of all , the idea of the bot is
in simplifying and saving moderator time :yum: 
## About the bot:
The bot is based on the logic of the state machine (FSM), for step-by-step compilation of a post.
Information is drawn from a pre-filled (parsing) sqlite3 database,
which frees the moderator to host the current information. After opening the table, the moderator only has to "copy / paste"
data at the request of the bot. After checking the post, it is carried out
sending a post to a channel or editing.
### Future updates:
+ Add parsing.  
For more comfortable adding data to sqlite3.
+ Make a bot friend with sqlite3.  
Add a search option given\editing from the table via the bot.  

*In other words, to switch the work to a more autonomous mode* :sunglasses:  
*P.s. list of modules used in requirements*

____________  

## Телеграм-бот как конструктор объявлений
### Введение:
В ходе написания и оформления постов для telegram, пользователи сталкиваются с рядом проблем 
(в данный момент обычная подготовка постов происходит или с трудом в месседжере или 
редактирование через другие документы), так же хотелось быть не привязанным
к смартфону или пк для более комфортного написания. Чтобы решить данную проблему 
и тратить на неё как можно меньше времени появилась  идея создания данного бота. 
Бот представляет собой вспомогательный инструмент модератора для более быстрого 
составления постов и их отправки в канал. В первую очередь задумка бота заключается 
в упрощении и экономии времени модератора :yum:  
### О боте:
В основе бота лежит логика машины состояний (FSM), для пошагового составление поста.
Информация черпается из предворительно заполненной(парсинг) базы данных sqlite3,
что освобождает модератора о размещении у себя текущей информации. После открытия таблицы модератору предстоит лишь "копировать\вставить"
данные по требованию бота. После проверки поста осуществляется его
отправки поста в канал либо редактирование.
### Дальнешие планы по улучшению:
+ Добавить парсинг.  
Для более конмфортного добавления данных в sqlite3.

+ Подружить бот с sqlite3.  
Добавить вариант перебора\редактирования данный из таблицы через бота.

*Иными словами, перевести работу в более автономный режим* :sunglasses:  
*P.s. список используемых модулей в requirements*



