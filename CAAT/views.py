from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control


def logout(req):

    redirect('/')