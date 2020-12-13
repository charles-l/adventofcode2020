with open('input_day13') as f:
    f = [x.strip() for x in f.readlines()]
earliest_departure = int(f[0])
available_lines = [int(l) for l in f[1].split(',') if l != 'x']
waiting_time, line_id = min((-(earliest_departure % -l), l) for l in available_lines)
print(waiting_time * line_id)
