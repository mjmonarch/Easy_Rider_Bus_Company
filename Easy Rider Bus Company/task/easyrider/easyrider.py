# ----------------------------------------------STAGE 1----------------------------------------------
#
# import json
# from collections import defaultdict
#
#
# def check(str_JSON):
#     err_dict = defaultdict(lambda: 0)
#     bus_list = json.loads(str_JSON)
#
#     for bus_route in bus_list:
#         for elem in ['bus_id', 'stop_id', 'next_stop']:
#             if type(bus_route[elem]) != int:
#                 err_dict[elem] += 1
#         for elem in ['stop_name', 'a_time']:
#             if type(bus_route[elem]) != str or bus_route[elem] == "":
#                 err_dict[elem] += 1
#         if type(bus_route['stop_type']) != str or len(bus_route['stop_type']) > 1:
#             err_dict['stop_type'] += 1
#
#     print("Type and required field validation:", sum(err_dict.values()), "errors")
#     output_errors = ['bus_id', 'stop_id', 'stop_name', 'next_stop', 'stop_type', 'a_time']
#     for err in output_errors:
#         print(f"{err}: {err_dict[err]}")
#
# check(input())

# ----------------------------------------------STAGE 2----------------------------------------------
#
# import json
# from collections import defaultdict
# import re
#
#
# def check(str_JSON):
#     err_dict = defaultdict(lambda: 0)
#     bus_list = json.loads(str_JSON)
#
#     for bus_route in bus_list:
#         # check stop_name
#         if not re.match('([A-Z][a-z]+ )+(?=(Road|Avenue|Boulevard|Street)$)', bus_route['stop_name']):
#             err_dict['stop_name'] += 1
#         #  check stop_type
#         if not re.match('S$|O$|F$', bus_route['stop_type']) and bus_route['stop_type']:
#             err_dict['stop_type'] += 1
#         #  check a_time
#         if not re.match('([01][0-9]|2[0-3]):([0-5]\d)$', bus_route['a_time']):
#             err_dict['a_time'] += 1
#
#     print("Type and required field validation:", sum(err_dict.values()), "errors")
#     output_errors = ['stop_name', 'stop_type', 'a_time']
#     for err in output_errors:
#         print(f"{err}: {err_dict[err]}")
#
#
# check(input())

# ----------------------------------------------STAGE 3----------------------------------------------
import json
from collections import defaultdict


def count_stops(str_JSON):
    stop_dict = defaultdict(lambda: 0)
    bus_list = json.loads(str_JSON)

    for bus_route in bus_list:
        stop_dict[bus_route['bus_id']] += 1

    print("Line names and number of stops:")
    for key, value in stop_dict.items():
        print(f"{key}: {value}")


count_stops(input())