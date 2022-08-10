from .models import Student
# from django.shortcuts import render
# from django.shortcuts import render
# from rest_framework import views, status, parsers, response, serializers, viewsets, mixins, generics
from rest_framework import viewsets, response, status
# from django.shortcuts import get_object_or_404
from .serializer import StudentSerializer

"""
class StudentCreateView(generic.CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_view.html'
    success_url = '/student/create/'

    # это тоже рабочая функция как и get_context_data
    # def get(self, request, *args, **kwargs):
    #     students = Student.objects.all()
    #     form = StudentForm()
    #     return render(request, 'student_view.html', {'students': students, 'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        students = Student.objects.all()
        context['students'] = students
        return context


class StudentCourseView(generic.CreateView):
    model = StudentCourse
    form_class = StudentCourseForm
    template_name = 'student_course_view.html'
    success_url = '/student/student_course/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        students = StudentCourse.objects.all()
        context['students'] = students
        return context
"""

#
# @csrf_exempt
# def student_list(request):
#     """
#         List all courses or create a new course
#     """
#     if request.method == 'GET':
#         student = Student.objects.all()
#         serializer = StudentSerializer(instance=student, many=True)
#         return JsonResponse(data=serializer.data, safe=False, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         data = parsers.JSONParser().parse(request)
#         serializer = StudentSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(data=serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# @csrf_exempt
# def students_detail(request, pk):
#     try:
#         student = Student.objects.get(id=pk)
#     except Student.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = StudentSerializer(instance=student)
#         return JsonResponse(data=serializer.data, status=200)
#     elif request.method in {'PUT', 'PATCH'}:
#         data = parsers.JSONParser().parse(request)
#         serializer = StudentSerializer(instance=student, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(data=serializer.data, status=status.HTTP_200_OK)
#         return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         student.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)
#

"""
на генериках
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
"""

"""    
class StudentListMixinView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class StudentDetailMixinView(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView
):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer

        def get(self, request, *args, **kwargs):
            return super().retrieve(request, *args, **kwargs)

        def patch(self, request, *args, **kwargs):
            return super().update(request, *args, **kwargs)

        def delete(self, request, *args, **kwargs):
            return super().destroy(request, *args, **kwargs)

""""""


class StudentsListAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        student = Student.objects.all()
        serializer = StudentSerializer(instance=student, many=True)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)


class StudentDetailAPIView(views.APIView):

    def get_object(self, pk):
        try:
            student = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            raise serializers.ValidationError(detail="obj does not exist")
        return student

    def get(self, request, pk):
        student = self.get_object(pk=pk)
        serializer = StudentSerializer(instance=student)
        return JsonResponse(data=serializer.data, status=200)

    def patch(self, request, pk):
        student = self.get_object(pk=pk)
        data = parsers.JSONParser().parse(request)
        serializer = StudentSerializer(instance=student, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        student = self.get_object(pk=pk)
        student.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
"""

"""
class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(instance=queryset, many=True)
        return response.Response(data=serializer.data)

    def retrieve(self, request, pk):
        queryset = Student.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(instance=student)
        return response.Response(data=serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, pk=None):
        queryset = Student.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        serializer.is_valid(raise_exception=True)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        queryset = Student.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        student.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
"""


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
