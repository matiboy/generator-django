class <%= className %>(django.views.generic.View):
<% _.each(methods, function(m) { %><%= method %>
    pass<% }) %>
