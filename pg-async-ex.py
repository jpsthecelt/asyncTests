import asyncpg
from quart import Quart, jsonify
app = Quart(__name__)

@app.before_first_request
async def create_db():
    app.db = await asyncpg.create_pool(
        app.config['DATABASE'], loop=loop,)

@app.route('/')
async def index():
    async with app.db.acquire() as conn:
        info = await conn.fetchval(
            'SELECT info FROM something',)
    return jsonify(info=info)

