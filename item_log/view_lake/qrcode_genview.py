from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
import qrcode 
from io import BytesIO

class QRCodeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        value = kwargs.get('value')

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(f'http://jnbdrive.info/info/{value}')
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, "PNG")
        buffer.seek(0)
        return HttpResponse(buffer.getvalue(), content_type="image/png")