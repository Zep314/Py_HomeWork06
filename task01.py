# Написать программу вычисления арифметического выражения заданного строкой. 
# Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций. 
# Пример: 1+2*3 => 7; (1+2)*3 => 9;

operators = '+-/*^' # такие операции

def my_parse(string): # раскалываем строку на операнды, скобки и числа в список
    ret = []
    num = ''
    for char in string:
        if char in '.0123456789':
            num += char
        elif char in operators or char in '()':
            if len(num)>0: 
                ret.append(num)
                num = ''
            ret.append(char)
    if len(num)>0: ret.append(num)        
    return ret

def solver2operand(expression): # тут ждем 3 элемента в списке, из которых первый и последний - числа,
                                # а средний - операнд (просто операция над 2-мя числами)
    match expression[1]:
        case '+': return str(float(expression[0]) + float(expression[2]))
        case '-': return str(float(expression[0]) - float(expression[2]))
        case '*': return str(float(expression[0]) * float(expression[2]))
        case '/': return str(float(expression[0]) / float(expression[2]))
        case '^': return str(float(expression[0]) ** float(expression[2]))
        case _  : 
            print('Ошибка в выражении (1)')
            exit()
    return '0'

def get_operand_index(expression,op): # возвращаем первый сначала списка индекс элемента op
    try:
        return expression.index(op)
    except ValueError: # а вот тут not op in expression
        return -1

def iterator(expression): # тут обрабатываем список элементов выражения
    if expression[0] == '-': expression.insert(0,'0') # это если в первое число в выражении отрицательное
    match len(expression):
        case 0: return []            # такого не должно быть, но все же...
        case 1: return expression    # такого не должно быть, но все же...
        case 2: return expression[0] # такого не должно быть, но все же...
        case 3: return [solver2operand(expression)] # тут все просто - 3 элемента - просто считаем их
        case _: 
            mypos = get_operand_index(expression,')') # ищем закр. скобку
            if mypos == -1: # скобок нет!

                mypos = get_operand_index(expression,'^') # ^ - самая высокая приоритет
                if mypos == -1 or \
                   ((get_operand_index(expression,'*') < mypos)       # умножение и деление - равны по приоритету
                   and get_operand_index(expression,'*') > -1):       # но, тут вычисляем, кто из */ стоит первым
                            mypos = get_operand_index(expression,'*') #
                if mypos == -1 or \
                   ((get_operand_index(expression,'/') < mypos)       # 
                   and get_operand_index(expression,'/') > -1):       #  
                            mypos = get_operand_index(expression,'/') # вот прям до сюда вычисляем...

                if mypos == -1: mypos = get_operand_index(expression,'+') # если */^ не нашли - то + или -
                if mypos == -1: mypos = get_operand_index(expression,'-')

                if mypos > -1:
                    expression[mypos-1] = str(solver2operand(expression[mypos-1:mypos+2])) # вычисляем операцию
                                                                                           # с наивысшим приоритетом 
                                                                                           # результат пишем в ячейку
                                                                                           # первого операнда 
                    del expression[mypos:mypos+2]  # удаляем из списка операцию и второй операнд
                    return expression
            else: # обработка скобок
                open_bracket = mypos # ищем откр. скобку - берем сначала позицию закр. скобку
                for i in range(mypos,-1,-1): # идем от закр. скобки назад, пока не надем откр. скобку
                    if expression[i] == '(':
                        open_bracket = i # типа нашли
                        break
                
                # делим список на 3 куска
                expr1 = expression[0:open_bracket] # то, что до откр. скобки
                expr3 = expression[mypos+1:] # то, что после закр. скобки

                expr2 = iterator(expression[open_bracket+1:mypos]) # а вот середину без скобок - засовываем
                                                                   # сами в себя (оно там само разберется, что к чему) 
                expression = [] # восстанавливаем наш бедный список

                if len(expr1) > 0: expression.extend(expr1) # вдруг впереди только одна скобка и была 
                expression.extend(expr2)
                if len(expr3) > 0: expression.extend(expr3) # вдруг позади только одна скобка и была
                return expression

def my_solver(expression):
    while len(expression)>1: # должен остаться один элемент в списке - ответ
        expression = iterator(expression)
    return expression

# ======================================================
# тесты всякие
s = '12*3+3+5+2*2'
print(f'Вычисляем: \'{s}\' = {my_solver(my_parse(s))[0]} - контрольное занчение: {eval(s)}')
s = '1+2*(3+5)'
print(f'Вычисляем: \'{s}\' = {my_solver(my_parse(s))[0]} - контрольное занчение: {eval(s)}')
s= '15/(7-(1+1))*3-(2+(1+1))'
print(f'Вычисляем: \'{s}\' = {my_solver(my_parse(s))[0]} - контрольное занчение: {eval(s)}')
s = '-2*5'
print(f'Вычисляем: \'{s}\' = {my_solver(my_parse(s))[0]} - контрольное занчение: {eval(s)}')
s = '-2^5'
print(f'Вычисляем: \'{s}\' = {my_solver(my_parse(s))[0]} - контрольное занчение: {eval(s.replace("^","**"))}')
