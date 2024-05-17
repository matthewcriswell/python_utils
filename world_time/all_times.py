from zoneinfo import ZoneInfo, available_timezones
from datetime import datetime, timedelta

dt_now = datetime.now()

dt_now_list = list()
for tz in available_timezones():
    dt_now_list.append((tz, dt_now.astimezone(ZoneInfo(tz))))

dt_now_list_sorted = sorted(dt_now_list, key=lambda item: item[1].timetuple())

dt_by_ctime = dict()
for item in dt_now_list_sorted:
    item_ctime = item[1].ctime()
    if item_ctime in dt_by_ctime:
        dt_by_ctime[item_ctime].append(item[0])
    else:
        dt_by_ctime[item_ctime] = [item[0]]

for item in dt_by_ctime:
    print(f'{item}: {dt_by_ctime[item]}')

for item in dt_by_ctime:
    print(f'{item}')
print(f'There are currently {len(dt_by_ctime)} distinct times in {len(available_timezones())} different timezones')
