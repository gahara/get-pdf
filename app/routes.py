import asyncio
from flask import request, send_file
from app import app

from .utils import get_pdf_with_pypeteer


@app.route('/pdf')
def catch_all():
    url = request.args.get('url')
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.get_event_loop().run_until_complete(get_pdf_with_pypeteer(url))

    return send_file('page.pdf', as_attachment=True)
