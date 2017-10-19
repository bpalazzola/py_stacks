# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
import random
import string
allowed_chars = ''.join((string.ascii_letters, string.digits))
unique_id = ''.join(random.choice(allowed_chars) for _ in range(32))
unique_id
'121CyaSHHzX8cqbgLnIg1C5qNrnv21uo'
