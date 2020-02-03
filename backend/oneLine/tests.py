import os

from django.test import TestCase

# Create your tests here.
from mysettings.settings import BASE_DIR

if __name__ == '__main__':
    dic = {
        'a': 'answer a',
        'b': 'answer b'
    }

    print(dic['a'])
    print(dic.get('c'))
