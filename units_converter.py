from itertools import zip_longest


def is_number(ab):
    try:
        float(ab)
        return True
    except ValueError:
        return False


def sum_lists(list_1, list_2):
    list_united = [x + y for x, y in zip_longest(list_1, list_2, fillvalue=0)]
    return list_united


def print_result(hhh):
    kkk = print(hhh)
    return kkk


while True:
    result_output = 0
    conver_type = input('''
        Please type in the physical value you would like to convert from measurement convention system to nonmetrical 
        (mainly British):
        area
        cubature 
        pressure
        temperature 
        q for exit
        ''')
    if conver_type == 'q':
        print('Exit')
        break
    if conver_type in ('area', 'cubature', 'pressure', 'temperature',):
        if conver_type == 'area':
            value = input('Please type in the value in square metres: ')
            while not is_number(value):
                value = input("Not a value. Enter a value in numbers: ")
            ar1 = ((float(value) * 93.23957197) / 1000000)  # tsp
            ar2 = ((float(value) * 2.589988110336) / 1000000)  # mi^2
            ar3 = float(value) * 25.29285264  # rd^2
            ar4 = float(value) * 0.83612736  # yd^2
            ar5 = float(value) * 0.09290304  # ft^2
            ar6 = float(value) * 10000 * 6.4516  # in^2
            conversion = [str(ar1), str(ar2), str(ar3), str(ar4), str(ar5), str(ar6)]
            units = [' tsp', ' mi^2', ' rd^2', ' yd^2', ' ft^2', ' in^2']
            result_output = sum_lists(conversion, units)
        if conver_type == 'cubature':
            value = input('Please type in the value in cubic metres: ')
            while not is_number(value):
                value = input('Not a value. Enter a value in numbers: ')
            cu1 = float(value) * 0.764554857984  # yd^3
            cu2 = float(value) * 0.001 * 28.316846592  # ft^3
            cu3 = float(value) * 0.001 * 0.001 * 16.387064  # in^3
            cu4 = float(value) * 0.001 * 163.65924  # bl
            cu5 = float(value) * 0.001 * 36.36872  # bu
            cu6 = float(value) * 0.001 * 4.546090  # gal
            cu7 = float(value) * 0.001 * 1.1365225  # qt
            cu8 = float(value) * 0.001 * 0.56826125  # pt
            conversion = [str(cu1), str(cu2), str(cu3), str(cu4), str(cu5), str(cu6), str(cu7), str(cu8)]
            units = [' yd^3', ' ft^3', ' in^3', ' bl', ' bu', ' gal', ' qt', ' pt']
            result_output = sum_lists(conversion, units)
        if conver_type == 'pressure':
            value = input('Please type in the value in pascal: ')
            while not is_number(value):
                value = input('Not a value. Enter a value in numbers: ')
            pr1 = float(value) / 249.08891  # inH2O
            pr2 = float(value) / 2989.006692  # ftH2O
            pr3 = float(value) / 3386.38815789474  # inHg
            pr4 = float(value) / 6894.757293178  # psi
            pr5 = float(value) / 6894757.2931783  # ksi
            pr6 = float(value) / 47.8802589803  # psf
            pr7 = float(value) / 15444256.3366971  # br.tsi
            pr8 = float(value) / 107251.780115952  # br.tsf
            conversion = [str(pr1), str(pr2), str(pr3), str(pr4), str(pr5), str(pr6), str(pr7), str(pr8)]
            units = [' inH2O', ' ftH2O', ' inHg', ' yd^2', ' ft^2', ' in^2']
            result_output = sum_lists(conversion, units)
        if conver_type == 'temperature':
            value = input('Please type in the value in Celcius degrees: ')
            while not is_number(value):
                value = input('Not a value. Enter a value in numbers: ')
            tmp1 = float(value) + 273.15  # Kelvin
            tmp2 = float(value) * (9 / 5) + 32  # Farenheit
            tmp3 = (float(value) + 273.15) * (9 / 5)  # Rankin
            tmp4 = float(value) * (4 / 5)  # Reomur
            conversion = [str(tmp1), str(tmp2), str(tmp3), str(tmp4)]
            units = [' Kelvin', ' Farenheit', ' Rankin', ' Reomur']
            result_output = sum_lists(conversion, units)
    else:
        print('Not executable type of conversion! Please, choose available conversion type.')
    if result_output != 0:
        hit = 0
        print_result(result_output)
        hit = hit + 1
        if hit >= 2:
            break
