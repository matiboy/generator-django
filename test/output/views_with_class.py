import django.views.generic

# Preferrably use yo django:route to create new views and corresponding urls
class OtherAccount(django.views.generic.View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass
