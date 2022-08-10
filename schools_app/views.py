# from .forms import SchoolForm
# from .models import School
# from django.views import generic
# from django.shortcuts import render
#
#
# class SchoolCreateView(generic.CreateView):
#     model = School
#     form_class = SchoolForm
#     template_name = 'school_view.html'
#     success_url = '/school/create/'
#
#     def get(self, request, *args, **kwargs):
#         schools = School.objects.all()
#         form = SchoolForm()
#         return render(request, 'school_view.html', {'schools': schools, 'form': form})
