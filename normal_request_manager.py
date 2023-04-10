from query_and_preserve import query_and_preserve
from query_order_and_pay import query_order_and_pay
from query_and_collect_ticket import query_and_collect_ticket
from query_and_enter_station import query_and_enter_station
from query_and_cancel import query_one_and_cancel

from atomic_queries import _login, _query_orders, _query_high_speed_ticket

from utils import random_boolean
import time
import sys

from threading import Thread

num_threads = 10
num_reqs_per_thread = 1
elapse = 2

def main():
    headers = {
        "Cookie": "JSESSIONID=21A0370861087E0831E5D25D56BC9ABB; YsbCaptcha=BE12EE0295F548569DCC1D5B07FDBA55",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTYyNzI2MzE4NywiZXhwIjoxNjI3MjY2Nzg3fQ.xOXWi3QpTYL1OZqXaAHmpifyPc_lMX9smtOPTUveO9M",
        "Content-Type": "application/json"
    }


    for i in range(num_reqs_per_thread):
        #now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        #print(f"now_time:{now_time}")

        if i == 0:
            uid, token = _login()
            if uid is not None and token is not None:
                headers['Authorization'] = "Bearer " + token

        #print(f"idx:{i}")

        #start  = time.time()
        query_and_preserve(headers)
        #end = time.time()
        #print(end - start, file=sys.stderr)
        
        # 1/4 几率取消
        #if random_boolean() and random_boolean():
        #    query_one_and_cancel(headers)
        #else:
        #    pairs = _query_orders(headers=headers, types=tuple([0, 1]))
        #    pairs2 = _query_orders(headers=headers, types=tuple([0, 1]), query_other=True)
        #    pairs = pairs + pairs2
        #    query_order_and_pay(headers, pairs)
        #    query_and_collect_ticket(headers)
        #    query_and_enter_station(headers)



def main_thread():
    threads = []

    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print(f"start:{start_time}")

    for i in range(num_threads):
        t = Thread(name="thread" + str(i), target=main)
        time.sleep(elapse/1000)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # print(f"start:{start_time} end:{end_time}")


def query_order():
    headers = {
        "Cookie": "JSESSIONID=21A0370861087E0831E5D25D56BC9ABB; YsbCaptcha=BE12EE0295F548569DCC1D5B07FDBA55",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTYyNzI2MzE4NywiZXhwIjoxNjI3MjY2Nzg3fQ.xOXWi3QpTYL1OZqXaAHmpifyPc_lMX9smtOPTUveO9M",
        "Content-Type": "application/json"
    }
    uid, token = _login()
    if uid is not None and token is not None:
        headers['Authorization'] = "Bearer " + token

    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"start:{start_time}")

    for i in range(50):
        pairs = _query_orders(headers=headers, types=tuple([0, 1]), query_other=False)
        print(pairs)

    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"start:{start_time} end:{end_time}")


def query_tickets():
    headers = {
        "Cookie": "JSESSIONID=21A0370861087E0831E5D25D56BC9ABB; YsbCaptcha=BE12EE0295F548569DCC1D5B07FDBA55",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTYyNzI2MzE4NywiZXhwIjoxNjI3MjY2Nzg3fQ.xOXWi3QpTYL1OZqXaAHmpifyPc_lMX9smtOPTUveO9M",
        "Content-Type": "application/json"
    }
    uid, token = _login()
    if uid is not None and token is not None:
        headers['Authorization'] = "Bearer " + token


    date = time.strftime("%Y-%m-%d", time.localtime())

    start = "Shang Hai"
    end = "Su Zhou"
    high_speed_place_pair = (start, end)

    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"start:{start_time}")

    for i in range(50):
        trip_ids = _query_high_speed_ticket(place_pair=high_speed_place_pair, headers=headers, time=date)
        print(trip_ids)

    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"start:{start_time} end:{end_time}")


if __name__ == '__main__':
    num_threads = int(sys.argv[1])
    main_thread()

