import asyncio
from pyppeteer import launch
from terminaltables import SingleTable
from colorclass import Color


async def get_browser():
    return await launch()


async def get_page(browser, url):
    page = await browser.newPage()
    await page.goto(url)
    return page


async def create_account(page):
    # Click on create account to aceess app
    selector = "#createAccountBt"
    await page.click(selector)


async def select_top30(page):
    # Show top 30 currencies by market capitalization
    selector_top_list = "#navSubTop"
    await page.waitForSelector(selector_top_list)
    await page.click(selector_top_list)
    selector_top_30 = ".setCoinLimitBt[data-v='30']"
    await page.click(selector_top_30)


async def add_eur(page):
    # Select EUR fiat currency for the whole app
    selector_currency = "#nHp_currencyBt"
    await page.click(selector_currency)
    selector_add_currency = "#currencyAddBt"
    await page.click(selector_add_currency)
    selector_search = "input#addCurrencySearchTf"
    await page.type(selector_search, 'eur')
    selector_euro = "#addCurrencySearchResults > #add_currency_EUR"
    await page.waitForSelector(selector_euro)
    selector_euro_add = "#add_currency_EUR > .addRemCurrencyBt"
    await page.click(selector_euro_add)
    selector_use_euro = "#currencyBox > div[data-symbol='EUR']"
    await page.click(selector_use_euro)


async def extract_currency(page, currency):
    # Extract currency symbol
    symbol = await page.evaluate(
        "currency => currency.textContent",
        currency
    )
    symbol = symbol.strip()

    # Click on current currency
    await currency.click()
    selector_name = ".popUpItTitle"
    await page.waitForSelector(selector_name)
    # Extract currency name
    name = await page.querySelectorEval(
        selector_name,
        "elem => elem.textContent"
    )
    name = name.strip()
    # Extract currency actual price
    selector_price = "#highLowBox"
    price = await page.querySelectorEval(
        selector_price,
        "elem => elem.textContent"
    )
    _price = [
        line.strip() for line in price.splitlines() if len(line.strip())]
    price = parse_number(_price[1])
    # Extract currency 24h difference and percentage
    selector_24h = "#profitLossBox"
    price_24h = await page.querySelectorEval(
        selector_24h,
        "elem => elem.textContent"
    )
    _price_24h = [
        line.strip() for line in price_24h.splitlines() if len(line.strip())]
    perce_24h = parse_number(_price_24h[6])
    price_24h = parse_number(_price_24h[-2])
    # Extract currency capitalization rank
    selector_rank = "#profitLossBox ~ div.BG2.BOR_down"
    rank = await page.querySelectorEval(
        selector_rank,
        "elem => elem.textContent"
    )
    rank = int(rank.strip("Rank"))
    selector_close = ".popUpItCloseBt"
    await page.click(selector_close)
    return {
        "name": name,
        "symbol": symbol,
        "price": price,
        "price24h": price_24h,
        "percentage24h": perce_24h,
        "rank": rank
    }


async def navigate_top30_detail(page):
    # Iterate over the displayed currencies and extract data
    select_all_displayed_currencies = "#fullCoinList > [data-arr-nr]"
    select_currency = "#fullCoinList > [data-arr-nr='{}'] .L1S1"
    currencies = await page.querySelectorAll(select_all_displayed_currencies)
    total = len(currencies)

    datas = []
    for num in range(total):
        currency = await page.querySelectorEval(
            select_currency.format(num),
            "(elem) => elem.scrollIntoView()"
        )
        currency = await page.querySelector(select_currency.format(num))
        datas.append(await extract_currency(page, currency))
    return datas


async def scrape_cmc_io(url):
    browser = await get_browser()
    page = await get_page(browser, url)
    await create_account(page)
    await select_top30(page)
    await add_eur(page)
    currencies_data = await navigate_top30_detail(page)
    show_biggest_24h_winners(currencies_data)


def show_biggest_24h_winners(data):
    # Nicely print results on the terminal
    sorted_data = sorted(data, key=lambda x: x.get('percentage24h'))
    table_data = [[
        "Currency",
        "Symbol",
        "Actual price (€)",
        "24h price diff. (€)",
        "24h % diff",
        "Rank"
    ]]
    _red = Color("{autored}{}{/autored}")
    _green = Color("{green}{}{/green}")
    for row in sorted_data:
        if row['percentage24h'] < 0:
            _colored_row = [_red.format(value) for value in row.values()]
        else:
            _colored_row = [_green.format(value) for value in row.values()]
        table_data.append(_colored_row)
    table = SingleTable(table_data)
    table.title = "24h TOP 30 Currencies"
    table.justify_columns = {2: 'right', 3: 'right', 4: 'right', 5: 'right'}
    print(table.table)


def parse_number(str_num):
    # Helper to parse numeric strigns
    for symbol in ["€", "%", ","]:
        str_num = str_num.replace(symbol, "")
    return float(str_num)


if __name__ == "__main__":
    url = "http://coinmarketcap.io"

    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(scrape_cmc_io(url))