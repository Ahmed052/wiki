from django.shortcuts import render,redirect
from . import util
import markdown
from random import randint

def convert_md_to_html(title):
    content=util.get_entry(title)
    if content == None:
        return None
    else:
       html_content= markdown.markdown(content) 
       return html_content
   
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request,title):
    content=convert_md_to_html(title)
    if content == None:
        return render(request,"encyclopedia/error.html",{
            "message": "Page not found"
        })
    return render(request, "encyclopedia/entry_page.html", {"title": title, "content": content})

def search(request):
    if request.method == 'POST':
        user_search = request.POST.get('q')
        entries = util.list_entries()
        matching= [entry for entry in entries if user_search.lower() in entry.lower()]

        if not matching:
            return render(request, "encyclopedia/error.html", {
                "message": "No matching entry found"
            })

    return render(request, "encyclopedia/index.html", {
            'entries': matching
        })

    
    
def new_page(request):
    if request.method =="POST":
      title= request.POST.get('new_title')
      content= request.POST.get("new_content")

      if title in util.list_entries():
          return render(request,"encyclopedia/error.html",{
              "message": "title already exists"
          })
      if title=="" or content=="":
          return render(request,"encyclopedia/error.html",{
              "message": "title and content are reqiered"
          })       
      else:
         util.save_entry(title,content)
    return render (request, "encyclopedia/new_page.html")
  
def random_page(request):
     entries = util.list_entries()
     random_title = entries[randint(0, len(entries)-1)]
     content=convert_md_to_html(random_title)
     return render(request,"encyclopedia/entry_page.html",{
        "title":random_title,
        "content":content
    })
def edit(request):
    if request.method == "POST":
        title = request.POST.get("entry_title")
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })
    
def save(request):
   if request.method =="POST":
       title= request.POST.get("new_title")
       content= request.POST.get("new_content")
       util.save_entry(title,content)
       final_content = convert_md_to_html(title)
       return render(request,"encyclopedia/entry_page.html",{
             "title":title,
             "content":final_content
         })

   return    
   



