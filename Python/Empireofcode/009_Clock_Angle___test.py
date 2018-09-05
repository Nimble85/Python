
def clock_angle(time):
    m = int(time[3:])       # получаем срез строки time в минутах и приводим его к int
    h = int(time[:2])       # получаем срез строки time в часах и приводим его к int

    # print('minutes ', m, type(m))
    #print('hourse ', h, type(h))
    print(h, m)

    if h > 12:
        h = (h - 12)

    d = (h + (m /60 ))        #кол-во часов
    #d = (360 * (h % 12) / 12)
    #print(d, 'summ_hh')

    f = ((d * 5) * 6)           #градусы часов
    #print (f, 'gradys hourses')
    g = ((m * 6))               #градусы минут
    #print (g, 'gradys minutes')

    ang = abs(f - g)
    print(abs, 'fysfgfdsgdf')
    reang = 360 - ang

    print('Ugol resultat = ', ang)
    print('Reang = ', reang)


    if ang > reang:
        print(reang)
        return reang

    else:
        print(ang)
        return ang



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")



