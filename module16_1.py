from fastapi import FastAPI

appp = FastAPI()

@appp.get('/')
async def main_page():
    return 'Главная страница'

@appp.get('/user/admin')
async def admin():
    return 'вы вошли как администратор'

@appp.get('/user/{user_id}')
async def usern():
    return f'вы вошли как пользователь № {user_id}'

@appp.get('/user')
async def info(username: str, age: int):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'