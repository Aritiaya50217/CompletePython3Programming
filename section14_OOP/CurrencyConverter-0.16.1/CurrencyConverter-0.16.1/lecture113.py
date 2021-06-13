from currency_converter import CurrencyConverter
from datetime import date

''' The fallback method can be configured with the fallback_on_missing_rate_method parameter, which currently supports "linear_interpolation" and "last_known" values.  '''
c = CurrencyConverter(fallback_on_missing_rate=True,fallback_on_wrong_date=True)

# ถ้า value หรือ 100 ที่เราใส่มีค่ามากกว่า Rate ของ BGN จะเกิด Error จึงใช้ fallback_on_missing_rate = True เพื่อให้แสดงค่า Rate จริง ๆ ของ BGN ออกมา
print(c.convert(100, 'BGN', date=date(2010, 11, 21)))
# หาก date ที่เราใส่ไปไม่มีในข้อมูลจะเกิด Error จึงใส่ fallback_on_wrong_date=True เพื่อแสดงค่า Rate ของวันล่าสุดออกมา
print(c.convert(100, 'EUR', 'USD', date=date(1986, 2, 2)))
print(c._get_rate)