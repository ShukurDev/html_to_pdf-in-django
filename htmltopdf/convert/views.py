from typing import Dict

from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views import View


# Create your views here.
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


data = {
    "Company": "Shukurali Rezamonov",
    "address": "Oltinsoy district,Friend street",
    "City": "Termite",
    "State": "DT",
    "zipcode": "12345",

    "phone": "937990702",
    "email": "shukurdev02@gmail.com",
    "website": "shukurdevblog.heroku.com",
}


class ViewPdf(View):
    def get(request, *args, **kwargs):
        pdf = render_to_pdf('pdf_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class DownloadPdf(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('pdf_template.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoise_%s.pdf" %'12341231'
        content = "attachment; filename = '%s'" %(filename)
        response['Content-Disposition'] = content
        return response


def index(request):
    context = {}
    return render(request, 'index.html', context)
