from datetime import datetime
from aiohttp import web
#from db_connection import *
from config import IP
import re
import logging
#import db_connection

logging.basicConfig(filename="server.log", level=logging.INFO)


def get_invoice_id(req):
    res = re.findall(r'invoice_id=([a-z0-9]+)',req)[0].split('=')[0]
    return str(res)

def get_invoice_status(req):
    res = re.findall(r'invoice_status=([a-z0-9]+)',req)[0].split('=')[0]
    return str(res)

def get_invoice_amount(req):
    res = re.findall(r'invoice_amount=([0-9]*[.,]?[0-9]+)',req)[0].split('=')[0]
    return float(res)

def get_order_id(req):
    res = re.findall(r'order_id=([A-Za-z0-9]+)',req)[0].split('=')[0]
    return res


async def handler(request):
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if request.body_exists:
        data_b = await request.read()
        data = str(data_b.decode('utf-8'))
        logging.info(data)
        try:
            if get_invoice_status(data) == 'unpaid':
                logging.info(date_now+" [create payment] "+get_order_id(data)+' '+get_invoice_status(data)+' '+str(get_invoice_amount(data)))
            elif get_invoice_status(data) == 'confirming' or get_invoice_status(data) == 'mispaid':
                #con = connect()
                id = int(get_order_id(data)[:-12])
                ammount = get_invoice_amount(data)
                #create_payment(con, get_order_id(data), get_invoice_id(data), get_invoice_status(data),
                #               get_invoice_amount(data),date_now)
                #add_funds(con,id,ammount)
                #    payed(con,id)
                #con.close()
                logging.info(date_now+" [confirming payment] "+get_order_id(data)+' '+get_invoice_status(data)+' '+str(get_invoice_amount(data)))
            elif get_invoice_status(data) == 'cancelled':
                logging.info(date_now+" [cancelled payment] "+get_order_id(data)+' '+get_invoice_status(data)+' '+str(get_invoice_amount(data)))
            else:
                pass
        except:
            pass
    return web.json_response({"ok": 1})

app = web.Application()
app.add_routes([web.view('/', handler)])
web.run_app(app, host=IP, port=8080)
