import os

from django.test import TestCase
from mysettings import settings
# Create your tests here.
if __name__ == '__main__':
    print('==============')
    print(os.path.join(settings.BASE_DIR, 'test'))

