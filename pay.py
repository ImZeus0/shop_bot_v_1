import hmac
import hashlib
import base64
import requests
from config import merchant_id, secret_key
import json


def check_pay(invoice_id):
    url = 'https://api.cryptonator.com/api/merchant/v1/getinvoice?'
    params = merchant_id + '&' + invoice_id + '&' + secret_key
    hash = hashlib.sha1()
    hash.update(bytes(params, 'utf-8'))
    print(type(hash.hexdigest()))
    res = url + 'merchant_id=' + merchant_id + '&invoice_id=' + invoice_id + '&secret_hash=' + hash.hexdigest()
    response = requests.get(res)
    data = response.content
    print(data)


def startpayment(amount, id):
    start_url = 'https://api.cryptonator.com/api/merchant/v1/startpayment?'
    item_name = '&item_name=proxy'
    invoice_amount = '&invoice_amount=' + str(amount)
    invoice_currency = '&invoice_currency=usd'
    merchant = '&merchant_id=' + merchant_id
    order_id = '&order_id=' + str(id)
    return start_url + merchant + item_name + invoice_amount + invoice_currency + order_id
