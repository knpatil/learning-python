

def ascii_figure():
    slash_count = 16
    star_count = 0
    for i in range(0, 5):
        print('/' * slash_count, '*' * (star_count * 8), '\\' * slash_count,
              sep='')
        slash_count -= 4
        star_count += 1

ascii_figure()
