
# python3 manage.py shell - start Django shell terminal

# from women.models import * - import models

# Women.objects.all() - get all posts from DB

# Women.objects.all()[:5] - show first 5 posts

# Women.objects.all()[3:8] - show entries 3 to 8. And 8 does not turn on

# Women.objects.order_by('pk') - change sort order
# Women.objects.order_by('-pk') - reverse sort order
# Women.objects.all().reverse() - reverse sort for all orders
# Women.objects.filter(pk__lte=2) - selecting records whose primary key is less than or equal to 2
# Women.objects.get(pk=2) - selecting one record whose primary key is 2

# from django.db import connection - import connection for view queries (requests)

# connection.queries - command to view queries (requests)

# --------------> To process data from linked tables

# w = Women.objects.get(pk=2) - selecting one record whose primary key is 2
# w - All table fields, ID, also a foreign key (cat_id) and a property (cat) that refers to the (Category) are available in the variable
# w.cat or w.pk or... - access to values
# w.cat.name - get (name) from Category table

# Creating a query using the Category primary model to get all the posts associated with it.
# To record an Actress, we need to get all the records from the Women model that also belong to actresses.
# ----- <secondary model>_set <---- construction for reading records of related models
# c = Category.objects.get(pk=1) - we selected the value with index 1 from the Category table.
# c.women_set.all() - read all values associated with one category from the Women table
# women_set - secondary model name

# <attribute name>_gte - ( >= )
# <attribute name>_lte - ( <= )

# Women.objects.filter(title__contains='er') - filter by part of the title name line
# Women.objects.filter(title__icontains='ER') - filter by part of the title name line. Case insensitive

# Women.objects.filter(pk__in=[2,5,11,12], is_published=True) - selects records by values. Using a list [2,5,11,12].
#   You can filter by several parameters, for example (is_published=True)

# from django.db.models import Q - import Q class
# Women.objects.filter(Q(pk__lt=5) | Q(cat_id=2)) - take all records with a primary key less than 5 or cat_id equal to 2
# Women.objects.filter( ~ Q(pk__lt=5) | Q(cat_id=2)) - ( ~ ) reverse condition similar to the previous one
# Women.objects.filter( ~ Q(pk__lt=5) | Q(cat_id=2)) - ( ~ ) reverse condition similar to the previous one






























