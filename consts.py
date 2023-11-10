START_MESSAGE = "Здравствуй, дорогой пользователь! Бот создан для того, чтобы вы лучше узнали родной город"

HELP_DICT = {
    "start": "выводит приветственное сообщение",
    "help": "выводит это сообщение"
}

GUIDES_DICT = {
    "sis1hm": "CAACAgIAAxkBAAEB5w9lTiyzFLK21HvBHewjvqbAproWGgAC7zMAArIraEpx8oaJ2UBrnjME",
    "sis1false": "CAACAgIAAxkBAAEB5xVlTi97iWOC2pereKPNYuTlQkMNwQAClz4AAqJQaEpDJE5t0UCpYTME",
    "sis1true": "CAACAgIAAxkBAAEB5xllTi-DOrVfJThoTK0D8__3hATyNQAC7ToAAk6daEp3YVnVdtz1qzME",
    "sis1hello": "CAACAgIAAxkBAAEB5xdlTi9_wVST3TdN3DieO0AMgrRNmAAC2EAAArv7aEprLlz9aVNeeDME",
    "sis2hm": "CAACAgIAAxkBAAEB5xtlTi-FD8agQskWrcAItH8W0w8alAACjDsAAlrJcUp1kQ96bPF6hjME",
    "sis2false": "CAACAgIAAxkBAAEB5x9lTi-KVQ__zQ0W4JQNmMHJ-FkNSAACizkAAvTzcEosAW77py-VszME",
    "sis2true": "CAACAgIAAxkBAAEB5x1lTi-IHabP7ygQjStc4H0QeVrlvwACeFUAAgOXcEr5yPJLFOboODME",
    "sis2hello": "CAACAgIAAxkBAAEB5yFlTi-N77aUWDKzpk7y9vvlqunPbwACRjYAAhINcUrlHyQwEHnppjME"
}

QUESTS = ["Квест1", "Квест2", "Квест3"]


def get_help_message():
    res = "Функции бота РЕШУ ЕГЭ:\n"
    for key in HELP_DICT:
        res += f"/{key} - {HELP_DICT[key]}\n"
    return res
