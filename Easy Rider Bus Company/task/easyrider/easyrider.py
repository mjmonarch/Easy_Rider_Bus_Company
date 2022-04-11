# ----------------------------------------------STAGE 1----------------------------------------------

import json
from collections import defaultdict


def check(str_JSON):
    err_dict = defaultdict(lambda: 0)
    bus_list = json.loads(str_JSON)

    for bus_route in bus_list:
        for elem in ['bus_id', 'stop_id', 'next_stop']:
            if type(bus_route[elem]) != int:
                err_dict[elem] += 1
        for elem in ['stop_name', 'a_time']:
            if type(bus_route[elem]) != str or bus_route[elem] == "":
                err_dict[elem] += 1
        if type(bus_route['stop_type']) != str or len(bus_route['stop_type']) > 1:
            err_dict['stop_type'] += 1

    print("Type and required field validation:", sum(err_dict.values()), "errors")
    output_errors = ['bus_id', 'stop_id', 'stop_name', 'next_stop', 'stop_type', 'a_time']
    for err in output_errors:
        print(f"{err}: {err_dict[err]}")

check(input())