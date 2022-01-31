import asyncio
from playwright.sync_api import sync_playwright  
from playwright.async_api import async_playwright   
import os   
import time    

async def parser():        
    page_path = "https://www.tesla.com"        
    async with async_playwright() as p:          
        browser = await p.chromium.launch(headless=True)           
        page = await browser.new_page(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')         
        await page.goto(page_path) 
        page_content = await page.content()            
        await browser.close()
        print(page_content)    
        
asyncio.get_event_loop().run_until_complete(parser()) 