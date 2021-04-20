# Convert '$12,345.67' -> '€12.345,67'
import re       # import regex module


def converter(ammount):
    ammount = ammount.strip(' ')
    # regex look behind for $ . or ,
    deconstructAmm = list(re.split(r'(?<=[$.,])', ammount))
    print(deconstructAmm)
    deconstructAmm[0] = '€'
    deconstructAmm[1] = deconstructAmm[1].replace(',', '.')
    deconstructAmm[2] = deconstructAmm[2].replace('.', ',')
    ammount = ''.join(deconstructAmm)
    return ammount


print(converter('     $12,345.67     '))
