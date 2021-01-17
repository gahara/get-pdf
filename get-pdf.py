import asyncio
from pyppeteer import launch


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://github.com/gahara')
    await page.pdf({
        'path': 'page.pdf',
        'format': 'Letter',
        'margin': {
            'top': '20px',
            'bottom': '40px',
            'left': '20px',
            'right': '20px'
        }
    })

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())