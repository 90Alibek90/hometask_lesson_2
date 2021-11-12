my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_list = []
for element in my_list:
    if element.isdigit():
        new_list.extend(['"', f'{int(element):02}', '"'])
    elif (element.startswith('+') or element.startswith('')) and element[1:].isdigit():
        new_list.extend(['"', f'{element[0]}{int(element[1:]):02}', '"'])
    else:
        new_list.append(element)

out_info = ' '.join(new_list)
symbol_idxs = []
for idx, letter in enumerate(out_info):
    if letter == '"':
        symbol_idxs.append(idx)
for idx in range(len(symbol_idxs)):
    if idx % 2 == 0:
        symbol_idxs[idx] = symbol_idxs[idx] + 1
    else:
        symbol_idxs[idx] = symbol_idxs[idx] - 1

for del_idx in reversed(symbol_idxs):
    out_info = out_info[:del_idx] + out_info[del_idx + 1:]
print(out_info)
