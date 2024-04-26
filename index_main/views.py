from django.shortcuts import render, redirect
from .models import Articles
from django.http import HttpResponse
# from .forms import InputForm
from .forms import ArticlesForm
from django.views.generic import DetailView,UpdateView,DeleteView
def index(request):
    t=Articles.objects.all()
    siyahi= {'titul': 'Əsas səhifə',
            'siyahi': [1, 2, 'Salam', 'A',4 , 6],
            'luget': {'ad': 'Audi', 'qiymet': 5000},
            #'form':InputForm(),
            't': t
            }
    return render(request,'index_main/index.html',siyahi)

def about(request):
    return render(request,'index_main/about.html',{'titul': 'Haqqimizda'})

def create(request):
    # sahə tipləri validasiyası zamanı error sətri üçün dəyişən
    error = ''
    # əgər forma baruzerdən qayıdırsa şərti yoxlanılır. Bu zaman post metodu true olacaq.
    if request.method == 'POST':
        # form obyektinə sahələrlə qayıdan datalar mənimsədilir.
        form = ArticlesForm(request.POST)
        # əgər sahələrdəki datalar sahə dəyişən tiplərinə uyğundursa şərti yoxlanılır(validasiya).
        if form.is_valid():
            # onda datalaları bazada saxlayan save metodu çağırılır.
            form.save()
            # Lazımi səhifəyə yönləndirilir
            return redirect('index')
        # əgər sahələrdəki datalar sahə dəyişən tiplərinə uyğun gəlmədikdə error dəyişəni ilə səhifəyə səhv qayıdacaq.
        else:
            error = 'Formada səhv var!'
            # Böş sahələrdən ibarət forma "hazırlanır" form obyektinə verilir.
    form = ArticlesForm()
    # forma lüğət dəyişəninə mənimsədilir.
    data = {'form': form,'error': error}
     # forma sahəlrinə uyğun şablon əsasında sənifə yığılır
    return render(request, 'index_main/create.html', data)



class NewsDetailView(DetailView):
    model = Articles
    template_name = 'index_main/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    # fields = ['title', 'anons', 'full_text', 'date']
    template_name = 'index_main/create.html'
    form_class = ArticlesForm
    # def get_success_url(self):

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/'
    template_name = 'index_main/delete_view.html'



# def NewsDetailViewFun(request, pk):
#     t = Articles.objects.get(id=pk)
#     return render(request, 'index_main/details_view.html', {'article': t})
#def xeberler(request):
    #return HttpResponse("Xeberler Sehifesi")


# Create your views here.
