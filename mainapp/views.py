from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
# Create your views here.
class MonthPostDetailView(DetailView):
    pass

class NewsPostDetailView(DetailView): # новое
    model = NewsPostForm
    template_name = 'news-sinlge.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        dropdown = NavList.objects.all()

        context['dropdown'] = dropdown

        return context

class TalapkerPostDetailView(DetailView): 
    model = NavList
    template_name = 'profession_single-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        dropdown = NavList.objects.all()

        context['dropdown'] = dropdown

        return context
        

def news_single_page(request):
    dropdown = NavList.objects.all()
    return render(request, 'news-single.html', {'dropdown':dropdown})
def index_page(request):
    talapker = TalapkerPost.objects.order_by('-id')[:3]
    slider = SwiperImg.objects.order_by('-id')[:6]
    bigPost = NewsBigPost.objects.all()
    shortPost = NewsShortPost.objects.order_by('-id')[:2]
    longPost = NewsLongPost.objects.all()
    dropdown = NavList.objects.all()
    return render(request, 'index.html', {'dropdown':dropdown,'talapker': talapker,'slider': slider,'bigPost': bigPost.last(),'shortPost':shortPost,'longPost':longPost.last(), 'lang': 'kz',})

def news_page(request):
    dropdown = NavList.objects.all()
    newsPost = NewsPostForm.objects.all()
    news_paginator = Paginator(newsPost, 2)
    page_num = request.GET.get('page')
    page = news_paginator.get_page(page_num)
    for pos in newsPost:
        print(pos)
        print(pos.slug)
    return render(request, 'news.html',{'dropdown':dropdown,"newsPost": newsPost,'page':page})

def about_page(request):
    dropdown = NavList.objects.all()
    return render(request, 'about_us.html',{'dropdown':dropdown})


def talapker_page(request):
    dropdown = NavList.objects.all()
    table = TalapkerPageTable.objects.all()
    return render(request, 'talapker.html' , {'dropdown':dropdown,'table':table})

def student_page(request):
    dropdown = NavList.objects.all()
    page_description = StudentPageForm.objects.all()
    return render(request, 'students.html',{'dropdown':dropdown,'page_description':page_description.last()})

def gallery_page(request):
    dropdown = NavList.objects.all()
    gallery = Gallery.objects.all()
    return render(request, 'gallery.html', {'dropdown':dropdown,'gallery':gallery})

def contact_page(request):
    dropdown = NavList.objects.all()
    return render(request, 'contact.html', {'dropdown':dropdown})

def calendar_page(request):
    dropdown = NavList.objects.all()
    return render(request, 'calendar.html',{'dropdown':dropdown})

def kodeks_page(request):
    dropdown = NavList.objects.all()

    return render(request,'ar-namys kodeksi.html',{'dropdown':dropdown})

def parents_page(request):
    dropdown = NavList.objects.all()
    for_parents = For_parents.objects.all()
    return render(request, 'for_parents.html',{'dropdown':dropdown,'for_parents':for_parents})

def profession_page(request):
    dropdown = NavList.objects.all()

    return render(request, 'profession_single-page.html',{'dropdown':dropdown})


def student_life_page(request):
    dropdown = NavList.objects.all()
    student_img = students_life_img.objects.order_by('-id')[:2]
    students_description = students_life_description.objects.all()
    return render(request,'student_life.html',{'dropdown':dropdown,'student_img':student_img,'students_description':students_description})

def clubs_page(request):
    club_video = clubs_page_video.objects.all()
    club_form = clubs_page_form.objects.all()
    dropdown = NavList.objects.all()
    photos = clubImage.objects.all()
    return render(request,'clubs.html',{'dropdown':dropdown,'club_form':club_form,'photos':photos,'club_video': club_video.last()})

def valounter_page(request):
    video = ValounterVideo.objects.all()
    dropdown = NavList.objects.all()
    return render(request,'valounter.html',{'dropdown':dropdown,'video':video.last()})


def kz_page(request):

    return render(request, '')
def ru_page(request):

    return render(request, '')
def en_page(request):

    return render(request, '')