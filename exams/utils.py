from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from io import BytesIO

class GeneratePDFMixin:

    def render_html_to_pdf(self, template_name, context):
        template = get_template(template_name)
        html = template.render(context)
        result = BytesIO()

        try:
            pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
            return HttpResponse(result.getvalue(),
                                content_type="application/pdf")
        except Exception as e:
            print(e)
            return None