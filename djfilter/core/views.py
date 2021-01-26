from django.shortcuts import render
from django.db.models import Q
from core.models import journal, category
# Create your views here.
def valid_query(param):
    return param != '' and param is not None
def filterView(request):
    categories = category.objects.all()
    query_journal = journal.objects.all()
    title_contains = request.GET.get('title_contains')
    id_exact = request.GET.get('id_exact')
    title_or_author = request.GET.get('title_or_author')
    view_count_min = request.GET.get('view_count_min')
    view_count_max = request.GET.get('view_count_max')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    category_field = request.GET.get('category_fl')
    reviewed_checked = request.GET.get('reviewed')
    not_reviewed = request.GET.get('notReviewed')

    if valid_query(title_contains):
        query_journal=query_journal.filter(title__icontains = title_contains)
    elif valid_query(id_exact):
        query_journal=query_journal.filter(id=id_exact)
    elif valid_query(title_or_author):
        query_journal=query_journal.filter(Q(title__icontains=title_or_author)| Q(author__name__icontains=title_or_author)).distinct()
    if valid_query(view_count_min):
        query_journal = query_journal.filter(views__gte=view_count_min)
    if valid_query(view_count_max):
        query_journal = query_journal.filter(views__lt=view_count_max)
    if valid_query(date_min):
        query_journal = query_journal.filter(publish_date__gte=date_min)
    if valid_query(date_max):
        query_journal = query_journal.filter(publish_date__lt=date_max)
    if valid_query(category_field) and category_field != 'Choose...':
        query_journal=query_journal.filter(categories__name= category_field)
    if reviewed_checked == 'on':
        query_journal=query_journal.filter(reviewed=True)
    if not_reviewed == 'on':
        query_journal=query_journal.filter(reviewed=False)
    diction = {'journals': query_journal,'categories':categories}
    return render(request, 'filter_view.html', context=diction)