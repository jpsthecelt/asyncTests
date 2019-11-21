from quart import (Quart, g, request, render_template_string, )
from quart.helpers import make_response

app = Quart(__name__)

@app.route('/')
async def route():
    data = await request.get_json()
    return await render_template_string( "Hello {{name}}", name=data['name'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
