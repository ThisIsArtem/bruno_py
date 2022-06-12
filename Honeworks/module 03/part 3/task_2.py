def en_counter(string):
    number_of_long_words = 0
    current_len = 0
    for i in range(len(string)):
        if 65 <= ord(string[i]) <= 122:
            current_len += 1
        else:
            if current_len < 5:
                number_of_long_words += 1
            current_len = 0
    print(number_of_long_words)


def ru_counter(string):
    stop_lst = [' ', '.', ',', '—', '?', '\n']
    number_of_long_words = 0
    current_len = 0
    for i in range(len(string)):
        if string[i] not in stop_lst:
            current_len += 1
        else:
            if 0 < current_len < 5:
                number_of_long_words += 1
            current_len = 0
    print(number_of_long_words)


txt = '''Было просто пасмурно, дуло с севера, 
А к обеду насчитал сто градаций серого. 
Так всегда первого ноль девятого, 
То ли весь мир сошёл с ума, то ли я — того. 
На столе записка от неё смятая, 
Недопитый виски допиваю с матами. 
Посмотрю в окно, допишу главу, 
Первое сентября, дворник жжёт листву. 
И серым облакам наплевать на нас, 
Если знаешь, как жить — живи 
Ты хотела плыть, как все? 
Так плыви… '''

ru_counter(txt