from aiohttp import web

async def efetua_login():
    print('blabla')
    data = {
        'usuario': 'mestre',
        'senha' : 'mestra'
    }
    response = web.post('https://localhost:8000')
    data = response.json()
    print(data)
    return data

app = web.Application()
app.router.add_post('/login', efetua_login())