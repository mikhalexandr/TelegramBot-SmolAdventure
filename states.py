from aiogram.fsm.state import State, StatesGroup


class HistoryStates(StatesGroup):
    pass


class QuestsStates(StatesGroup):
    setting_quest = State()
    setting_team = State()
    creating_team_name = State()
    adding_to_team = State()
    preparing_for_quest = State()
