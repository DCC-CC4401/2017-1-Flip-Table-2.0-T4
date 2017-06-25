import datetime
import simplejson
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Count, Sum
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.views.generic.edit import FormView