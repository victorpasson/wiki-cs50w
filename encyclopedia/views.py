from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django import forms
from . import util
import random
import markdown2

# Class to represente the forms
class NewPage(forms.Form):
    title = forms.CharField(label='Page Title')
    content = forms.CharField(widget=forms.Textarea(), label='Markdown Content')

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entries(request, entrie):
    markdown = util.get_entry(entrie)
    if markdown is not None:
        html = markdown2.markdown(markdown)
        return render(request, "encyclopedia/entrie.html", {
            "entrie": entrie,
            "html": html
        })
    else:
        return render(request, "encyclopedia/entrie.html", {
            "entrie": "404",
            "html": "<h1>404</h1>Page not Found."
        })

def search(request):
    search = str(request.GET['q'])
    entries_itens = util.list_entries()

    result_search = []

    for item in entries_itens:
        if item.capitalize() == search.capitalize():
            return HttpResponseRedirect(reverse('entrie',  kwargs={'entrie': item}))
        else:
            if item.upper().find(search.upper()) is not -1:
                result_search.append(item)

    return render(request, "encyclopedia/search.html", {
        'searchs': result_search
        })

def randompage(request):
    entries_itens = util.list_entries()
    page = entries_itens[random.randint(0, len(entries_itens) - 1)]
    return HttpResponseRedirect(reverse('entrie',  kwargs={'entrie': page}))

def newpage(request):
    if request.method == "POST":
        form = NewPage(request.POST)
        if form.is_valid():
            title = str(form.cleaned_data["title"])
            markdown = form.cleaned_data["content"]
            entries_itens = util.list_entries()

            if all(x not in entries_itens for x in [title, title.capitalize(), title.upper(), title.lower]):
                util.save_entry(title, markdown)
                return HttpResponseRedirect(reverse('entrie',  kwargs={'entrie': title}))
            else:
                return render(request, "encyclopedia/entrie.html", {
                    "entrie": " Error",
                    "html": "<h1>Error</h1><p>The page you want to create already exist.</p>"
                    })

        else:
            return render(request, "encyclopedia/newpage.html", {
                "form": form
            })

    return render(request, "encyclopedia/newpage.html", {
        'form': NewPage()
    })

def edit(request, entrie):

    if request.method == "POST":
        content = request.POST['content']
        if content != "":
            util.save_entry(entrie, content)
            return HttpResponseRedirect(reverse('entrie',  kwargs={'entrie': entrie}))

        else:
            content = "#" + entrie
            util.save_entry(entrie, content)
            return HttpResponseRedirect(reverse('entrie',  kwargs={'entrie': entrie}))

    markdown = util.get_entry(entrie)
    return render(request, "encyclopedia/edit.html", {
        'markdown': markdown,
        'entrie': entrie
    })