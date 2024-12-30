from django.db.models import Q
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)
from goods.models import Products


def q_search(query, goods=Products.objects.all()):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    vector = SearchVector("name", "description")
    search_query = SearchQuery(query)

    result = (
        Products.objects.annotate(rank=SearchRank(vector, search_query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )
    result = goods.annotate(
        rank=SearchRank(vector, search_query),
        headline_name=SearchHeadline(
            "name",
            search_query,
            start_sel='<span style="background-color:yellow">',
            stop_sel="</span>",
        ),
        headline_description=SearchHeadline(
            "description",
            search_query,
            start_sel='<span style="background-color:yellow">',
            stop_sel="</span>",
        )
    ).filter(rank__gt=0).order_by("-rank")
    return result

    # keywords = [word for word in query.split() if len(word) >2]

    # q_objects = Q()

    # for token in keywords:

    # q_objects|= Q(description__icontains=token)
    # q_objects|= Q(name__icontains=token)

    # return Products.objects.filter(q_objects)
