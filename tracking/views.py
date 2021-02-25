from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, reverse, redirect

# Create your views here.
from django.http import HttpResponseRedirect
from django.views import View
from django.views.decorators.http import etag

from .forms import VisitorForm
from .models import Visitor

from random import randint


class FingerprintView(View):
    template_name = 'tracking/fingerprint.html'

    def get(self, request):
        fp = request.GET.get('fp')
        if fp:
            form = None
            visitors = Visitor.objects.filter(fp=fp)
        else:
            form = VisitorForm()
            visitors = None
        ctx = {'fp': fp, 'form': form, 'visitors': visitors}
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = VisitorForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)
        visitor = form.save(commit=True)
        return redirect('tracking:detail', fp = visitor.fp)


class DetailView(View):
    template_name = 'tracking/fingerprint.html'

    def get(self, request, fp):
        visitors = Visitor.objects.filter(fp=fp)
        ctx = {'fp': fp, 'visitors': visitors}
        return render(request, self.template_name, ctx)


def my_etag(request):
    if request.headers.get('if-none-match'):
        return request.headers.get('if-none-match')
    else:
        id = format(randint(0, 9999999999), '010d')
        return '"'+id+'"'


class EtagView(View):
    template_name = 'tracking/etag.html'

    # def dispatch(self, request, *args, **kwargs):
    #     @etag(my_etag)
    #     def _dispatch(request, *args, **kwargs):
    #         return super(EtagView, self).dispatch(request, *args, **kwargs)
    #     return _dispatch(request, *args, **kwargs)

    def get(self, request):
        if request.headers.get('if-none-match'):
            etag = request.headers.get('if-none-match')
        else:
            id = format(randint(0, 9999999999), '010d')
            etag = '"' + id + '"'

        ctx = {'etag': etag}
        resp = render(request, self.template_name, context=ctx)
        resp['etag'] = etag
        return resp