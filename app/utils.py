from pyppeteer import launch


async def get_pdf_with_pypeteer(url):
    browser = await launch(handleSIGINT=False,
                           handleSIGTERM=False,
                           handleSIGHUP=False)
    page = await browser.newPage()
    await page.goto(url)
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
