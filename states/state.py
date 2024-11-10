from aiogram.fsm.state import State, StatesGroup

class MyStates(StatesGroup):
    phone = State()
    location = State()
