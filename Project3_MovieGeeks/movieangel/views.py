# coding:utf-8
from django.shortcuts import render
from __future__ import unicode_literals
import uuid, random
import json
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from movieangel.models import Movie, Genre

# Create your views here.
@ensure_csrf_cookie
def index(request):
    genre_selected = request.GET.get('genre')

    api_key = get_api_key()

    if genre_selected:
        selected = Genre.objects.filter(name=genre_selected)[0]
        movies = selected.movies.order_by('-year', 'movie_id')
    else:
        movies = Movie.objects.order_by('-year', 'movie_id')

    genres = get_genres()

    page_number = request.GET.get("page", 1)
    page, page_end, page_start = handle_pagination(movies, page_number)

    context_dict = {
        'movies': page,
        'genres': genres,
        'api_key': api_key,
        'session_id': session_id(request),
        'user_id':user_id(request),
        'pages': range(page_start, page_end),
    }

    return render(request, 'movieangel/index.html', context_dict)

# 分页
def handle_pagination(movies, page_number):
    paginate_by = 18

    paginator = Paginator(movies, paginate_by)

    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page_number = 1
        page = paginator.page(page_number)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    page_number = int(page_number)
    page_start = 1 if page_number < 5 else page_number - 3
    page_end = 6 if page_number < 5 else page_number + 2
    return page, page_end, page_start

# 获得API_KEY
def get_api_key():
    # Load Credentials
    cred = json.loads(open(".prs").read())
    return cred['themoviedb_apikey']

# 获得所有电源类型名
def get_genres():
    return Genre.objects.all().values('name').distinct()

# 设置session_id
def session_id(request):
    if not "session_id" in request.session:
        request.session["session_id"] = str(uuid.uuid1())

    return request.session["session_id"]

# 设置usr_id, 没有就随机出来一个
def user_id(request):
    user_id = request.GET.get("user_id")

    if user_id:
        request.session['user_id'] = user_id

    if not "user_id" in request.session:
        request.session['user_id'] = random.randint(10000000000, 90000000000)

    print("ensured id: ", request.session['user_id'])
    return request.session['user_id']
