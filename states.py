import aiogram.fsm.state


class Form(aiogram.fsm.state.StatesGroup):
    waiting_for_contact = aiogram.fsm.state.State()

