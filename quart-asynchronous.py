from quart import (Quart, render_template,)

app = Quart(__name__)

@app.route('/')
async def index():
    return await render_template( 'index.html', 
        message='Grus Gott, mein freund! (quart-async)', )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
