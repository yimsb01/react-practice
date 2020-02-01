import os

from django.test import TestCase

# Create your tests here.
from mysettings.settings import BASE_DIR

if __name__ == '__main__':
    print('--------------')
    print(os.path.dirname(BASE_DIR))
    print(os.path.join(os.path.dirname(BASE_DIR), 'frontend', 'build'))
