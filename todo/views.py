# Create your views here.
# http://localhost:8000/todo/
# 2012.10.11, chaiwei, created.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader    
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.utils import timezone
from todo.models import TodoEntry

# ver 1: output values directly
def index1(request):
     all_todo_list = TodoEntry.objects.all().order_by('-create_date')

     output = ','.join([p.task for p in all_todo_list])

     return HttpResponse(output)

# ver 2: using template
                 
def index2(request):
     all_todo_list = TodoEntry.objects.all().order_by('-create_date')

     t = loader.get_template('todo/index.html')
     c = Context({
          'all_todo_list' : all_todo_list,
          })  

     return HttpResponse(t.render(c))


# ver 3: using shortcut

def index(request):
    all_todo_list = TodoEntry.objects.all().order_by('-create_date')

    return render_to_response('todo/index.html', {'all_todo_list' : all_todo_list}, context_instance = RequestContext(request))  

def add(request):
    try:
        task_msg = request.POST['task_msg']
        entry = TodoEntry(task = task_msg, status = 1, create_date = timezone.now())
        entry.save()
    except (KeyError):
        return render_to_response('todo/index.html', {'error_msg' : "no task msg isprovided!"}, context_instance = RequestContext(request))

    return HttpResponseRedirect("/todo/")

def delete(request, entry_id):
    entry = get_object_or_404(TodoEntry, pk=entry_id)
    entry.delete()

    return HttpResponseRedirect("/todo/")
    
