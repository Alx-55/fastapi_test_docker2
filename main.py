from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/users")  # ручка чтобы в конце проверить, что всё работает
async def get_users():
    return [{'id': 1, 'name': 'Artem'}]


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)  # для docker используем четыре нуля; тут uvicorn.run позволяет запускать приложение командой
                                                  # python main.py через терминал

