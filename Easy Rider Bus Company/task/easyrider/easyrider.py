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
# import json
# from collections import defaultdict
#
#
# def count_stops(str_JSON):
#     stop_dict = defaultdict(lambda: 0)
#     bus_list = json.loads(str_JSON)
#
#     for bus_route in bus_list:
#         stop_dict[bus_route['bus_id']] += 1
#
#     print("Line names and number of stops:")
#     for key, value in stop_dict.items():
#         print(f"{key}: {value}")
#
#
# count_stops(input())

# ----------------------------------------------STAGE 4----------------------------------------------
# import json
# from collections import defaultdict
#
#
# def count_stops(str_JSON):
#     start_stops_set, stop_set_uniq, stop_set_non_uniq, finish_stops_set = set(), set(), set(), set()
#     stop_dict = defaultdict(lambda: [0, 0])
#     bus_list = json.loads(str_JSON)
#
#     for bus_route in bus_list:
#         # checking start stops
#         if bus_route['stop_type'] == 'S':
#             # check if start stop for this route already exists
#             if stop_dict[bus_route['bus_id']][0]:
#                 print(f"There are multiple start stops for the line: {bus_route['bus_id']}.")
#                 break
#             else:
#                 start_stops_set.add(bus_route['stop_name'])
#                 stop_dict[bus_route['bus_id']][0] = 1
#         # checking final stops
#         if bus_route['stop_type'] == 'F':
#             # check if finish stop for this route already exists
#             if stop_dict[bus_route['bus_id']][1]:
#                 print(f"There are multiple finish stops for the line: {bus_route['bus_id']}.")
#                 break
#             else:
#                 finish_stops_set.add(bus_route['stop_name'])
#                 stop_dict[bus_route['bus_id']][1] = 1
#         # checking transfer stops
#         if bus_route['stop_name'] not in stop_set_uniq:
#             stop_set_uniq.add(bus_route['stop_name'])
#         else:
#             stop_set_non_uniq.add(bus_route['stop_name'])
#     else:
#         for key, value in stop_dict.items():
#             if value[0] != 1 or value[1] != 1:
#                 print(f"There is no start or end stop for the line: {key}.")
#                 break
#         else:
#             print(f"Start stops: {len(start_stops_set)} {sorted(start_stops_set)}")
#             print(f"Transfer stops: {len(stop_set_non_uniq)} {sorted(stop_set_non_uniq)}")
#             print(f"Finish stops: {len(finish_stops_set)} {sorted(finish_stops_set)}")
#
#
# count_stops(input())

# ----------------------------------------------STAGE 5----------------------------------------------
# import json
# import re
# from collections import defaultdict
# from datetime import time
#
#
# def check_time(str_JSON):
#     time_dict = defaultdict(lambda: time(hour=0, minute=0))
#     err_dict = {}
#     bus_list = json.loads(str_JSON)
#
#     for bus_route in bus_list:
#         c_hour, c_min = re.findall(r'\d{2}', bus_route['a_time'])
#         c_time = time(int(c_hour), int(c_min))
#
#         if bus_route['bus_id'] in err_dict.keys():
#             continue
#         else:
#             if c_time < time_dict[bus_route['bus_id']]:
#                 err_dict[bus_route['bus_id']] = bus_route['stop_name']
#             else:
#                 time_dict[bus_route['bus_id']] = c_time
#
#     print("Arrival time test:")
#     if len(err_dict) == 0:
#         print("OK")
#     else:
#         for key, value in err_dict.items():
#             print(f"bus_id line {key}: wrong time on station {value}")
#
#
# check_time(input())

# ----------------------------------------------STAGE 6----------------------------------------------
import json
from collections import defaultdict


def count_stops(str_JSON):
    wrong_stops_list = []
    route_list = []
    non_id_stop_set, stop_set_uniq, stop_set_non_uniq = set(), set(), set()
    bus_list = json.loads(str_JSON)

    final = False
    last_id = 0
    for bus_route in bus_list:
        if bus_route['bus_id'] not in route_list:
            route_list.append(bus_route['bus_id'])
            final = False
            if bus_route['stop_type'] != 'S':
                if bus_route['stop_name'] not in wrong_stops_list:
                    wrong_stops_list.append(bus_route['stop_name'])
        else:
            if bus_route['stop_type'] == 'S':
                if bus_route['stop_name'] not in wrong_stops_list:
                    wrong_stops_list.append(bus_route['stop_name'])
            if bus_route['stop_type'] == 'F':
                if final:
                    wrong_stops_list.append(bus_route['stop_name'])
                else:
                    final = True
        if bus_route['stop_name'] not in stop_set_uniq:
            stop_set_uniq.add(bus_route['stop_name'])
        else:
            stop_set_non_uniq.add(bus_route['stop_name'])
        if bus_route['stop_type'] == 'O':
            non_id_stop_set.add(bus_route['stop_name'])

        last_id = bus_route['bus_id']

    for item in stop_set_non_uniq.intersection(non_id_stop_set):
        wrong_stops_list.append(item)

    print("On demand stops test:")
    if len(wrong_stops_list) == 0:
        print("OK")
    else:
        print(sorted(wrong_stops_list))


count_stops(input())