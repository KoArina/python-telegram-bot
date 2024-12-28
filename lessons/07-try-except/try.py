print('Input N1:')
n1 = input()
print('Input N2:')
n2 = input()

# помилки
try:
    d = int(n1) / int(n2)
    print(d)
except ZeroDivisionError:
    print('ділення на нуль')
except TypeError:
    print('що за нерозумний програміст')

    d = int(n1) / int(n2)
    print('переведено в INT: ', d)
finally:
    print('блок винятків завершено')


print('програма працює!')


