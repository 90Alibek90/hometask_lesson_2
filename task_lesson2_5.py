# merchs = [57.8, 46.51, 97, 25, 38.51, 60.99, 78.54, 1024, 1.5]
# for merch in merchs:
#     rub = int(merch)
#     kk = (merch - rub) * 100
#     print(f'{rub} руб {kk:02.0f} коп')
#
#
# merchs = [57.8, 46.51, 97, 25, 38.51, 60.99, 78.54, 1024, 1.5]
# print(id(merchs))
# merchs.sort()
# print(id(merchs))
# for merch in merchs:
#     rub = int(merch)
#     kk = (merch - rub) * 100
#     print(f'{rub} руб {kk:02.0f} коп', end=', ')

merchs = [57.8, 46.51, 97, 25, 38.51, 60.99, 78.54, 1024, 1.5]
# for merch in sorted(merchs)[::-1][:5]:
#     rub = int(merch)
#     kk = (merch - rub) * 100
#     print(f'{rub} руб {kk:02.0f} коп', end=', ')

print([f'{int(merch)} руб, {(merch - int(merch)) * 100:02.0f} коп' for merch in sorted(merchs)[::-1][:5]])
