class <%= viewClass %>(django.views.generic.View):
<% _.each(methods, function(m) { %>    def <%= m.toLowerCase() %>(self, request, *args, **kwargs):
        pass

<% }) %>
