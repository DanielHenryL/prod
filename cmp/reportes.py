import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.utils import timezone

from .models import ComprasDet, ComprasEnc

def link_callback(uri, rel):
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path=result[0]
    else:
        sUrl = settings.STATIC_URL        # Typically /static/
        sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL         # Typically /media/
        mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path

def reporte_compras(request):
    template_path = 'cmp/compras_print_all.html'
    today = timezone.now()

    compras = ComprasEnc.objects.all()
    context = {
        'obj':compras,
        'today':today,
        'request':request,
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="todas_compras.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    #Crear el pdf
    pisaStatus = pisa.CreatePDF(
        html, dest = response, link_callback=link_callback
    )
    #si hay algun error
    if pisaStatus.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
    return response

def imprimir_compra(request, compra_id):
    template_path = 'cmp/compras_print_one.html'
    today = timezone.now()

    enc = ComprasEnc.objects.filter(pk=compra_id).first()
    if enc:
        detalle = ComprasDet.objects.filter(compra=compra_id)
    else:
        detalle={}

    context = {
        'detalle':detalle,
        'encabezado':enc,
        'today':today,
        'request':request,
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    #Crear el pdf
    pisaStatus = pisa.CreatePDF(
        html, dest = response, link_callback=link_callback
    )
    #si hay algun error
    if pisaStatus.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    
    return response

