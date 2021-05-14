import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.in/Logitech-MX-Master-Ultrafast-Customisation/dp/B07YXNDK6X/ref=sr_1_2?crid=2BSG49MWPT2HK&dchild=1&keywords=mx+mouse+3&qid=1621004548&sprefix=mx+mouse%2Ckitchen%2C281&sr=8-2"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(id="priceblock_ourprice").get_text()

price_without_currency = float(price.replace('₹', '').split('.')[0].replace(',', ''))
# price_as_float = float(price_without_currency)
print(price_without_currency)


import smtplib

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200

if price_without_currency < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("YOUR_SMTP_ADDRESS", port=587) as connection:
        connection.starttls()
        result = connection.login("YOUR_EMAIL", "YOUR_PASSWORD")
        connection.sendmail(
            from_addr="YOUR_EMAIL",
            to_addrs="YOUR_EMAIL",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
