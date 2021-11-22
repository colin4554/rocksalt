from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from car_rec.forms import VehicleForm
from car_rec.models import Vehicle
from PIL import Image




class VehicleView(TemplateView):
    form = VehicleForm
    template_name = 'imageForm.html'

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        print(str(request.FILES))
        # read the image
        im = Image.open(dict(request.FILES)['image'][0])

        # show image
        im.show()
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            v = Vehicle(image=form.image, name="test")
            print(form.image)
            return HttpResponseRedirect(reverse_lazy('home', kwargs={'pk': pk}))
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        # return render(request, 'imageForm.html')
        return HttpResponse(str(Vehicle.objects.get(pk=0)))
        return self.post(request, *args, **kwargs)
