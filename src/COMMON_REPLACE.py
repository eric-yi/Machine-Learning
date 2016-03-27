#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

SPECIAL = "%"
GENERAL = "?"
h = (SPECIAL, SPECIAL, SPECIAL, SPECIAL, SPECIAL, SPECIAL)

_Outlook = ('Sunny', 'Overcast', 'Rain')
_Temperature = ('Hot', 'Mild', 'Cool')
_Humidity = ('High', 'Normal')
_Wind = ('Weak', 'Strong')

_RUN = ('Yes', 'No')

_CONDITIONS = {
    'outlook': (0, _Outlook),
    'temperature': (1, _Temperature),
    'humiidty': (2, _Humidity),
    'wind': (3, _Wind)
}

_PlayTennis = (
    {_RUN[1]: (_Outlook[0], _Temperature[0], _Humidity[0], _Wind[0])},
    {_RUN[1]: (_Outlook[0], _Temperature[0], _Humidity[0], _Wind[1])},
    {_RUN[0]: (_Outlook[1], _Temperature[0], _Humidity[0], _Wind[0])},
    {_RUN[0]: (_Outlook[2], _Temperature[1], _Humidity[0], _Wind[0])},
    {_RUN[0]: (_Outlook[2], _Temperature[2], _Humidity[1], _Wind[0])},
    {_RUN[1]: (_Outlook[2], _Temperature[2], _Humidity[1], _Wind[1])},
    {_RUN[0]: (_Outlook[1], _Temperature[2], _Humidity[1], _Wind[1])},
    {_RUN[1]: (_Outlook[0], _Temperature[1], _Humidity[0], _Wind[0])},
    {_RUN[0]: (_Outlook[0], _Temperature[2], _Humidity[1], _Wind[0])},
    {_RUN[0]: (_Outlook[2], _Temperature[1], _Humidity[1], _Wind[0])},
    {_RUN[0]: (_Outlook[0], _Temperature[1], _Humidity[1], _Wind[1])},
    {_RUN[0]: (_Outlook[1], _Temperature[1], _Humidity[0], _Wind[1])},
    {_RUN[0]: (_Outlook[1], _Temperature[0], _Humidity[1], _Wind[0])},
    {_RUN[1]: (_Outlook[2], _Temperature[1], _Humidity[0], _Wind[1])}
)

def playtennis_string():
    str = 'Day\tOutlook\tTemperature\tHumidity\tWind\tPlayTennis\n'
    n = 0
    for entry in _PlayTennis:
        for result in _RUN:
            if entry.has_key(result):
                value = entry[result]
                _str = 'd%d\t%s\t%s\t%s\t%s\t%s\n' % (n, value[0], value[1], value[2], value[3], result)
                str += _str
                break;
        n += 1

    return str

def entropy(condition):
    if not _CONDITIONS.has_key(condition):
        print 'no condition exist'
        return
    _con = _CONDITIONS[condition]
    index = _con[0]
    _condition = _con[1]
    total = 0
    _params = {}
    for entry in _PlayTennis:
        for result in _RUN:
            if entry.has_key(result):
                v = entry[result]
                value = v[index]
                _find = False
                for k, v in _params.iteritems():
                    if value == k:
                        _params[k] += 1
                        _find = True
                        break
                if not _find:
                    _params[value] = 0
        total += 1

    _entr = float(0)
    for k, v in _params.iteritems():
        rate = v / float(total)
        cur_entr = -rate * math.log(rate, 2)
        _entr += cur_entr
    return _entr

def gain(S, A):
    total = 0
    positive = 0
    negtive = 0
    for entry in _PlayTennis:
        for result in _RUN:
            if entry.has_key(result):
                if result == 'Yes':
                    positive += 1
                else:
                    negtive += 1

        total += 1


    positive_rate = positive / float(total)
    negtive_rate = negtive / float(total)
    netropy = -(positive_rate * (math.log(positive_rate, 2))) - (negtive_rate * math.log(negtive_rate, 2))
    print 'positive = %d, negtive = %d, total = %d' % (positive, negtive, total)
    print positive_rate
    print math.log(positive_rate, 2)
    print negtive_rate
    print netropy


def loop_print_entropy():
    for k, v in _CONDITIONS.iteritems():
        _entropy = entropy(k)
        print '%s entropy: %f' %(k, _entropy)

if __name__ == '__main__':
    print playtennis_string()
    loop_print_entropy()
    gain(None, None)

