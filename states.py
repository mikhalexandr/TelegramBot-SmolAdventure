# все состояния

from aiogram.fsm.state import State, StatesGroup


class HistoryStates(StatesGroup):
    setting_history = State()
    preparing_for_history = State()

    history1_passing = State()
    history2_passing = State()
    history3_passing = State()


class QuestsStates(StatesGroup):
    setting_quest = State()
    setting_team = State()
    creating_team_name = State()
    adding_to_team = State()
    preparing_for_quest = State()
