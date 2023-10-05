from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BugForm
from .models import Bug

class BugCreateView(View):
    template_name = 'register_bug.html'

    def get(self, request):
        form = BugForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bug_list')
        return render(request, self.template_name, {'form': form})
    
class BugDetailView(View):
    template_name = 'view_bug.html'

    def get(self, request, bug_id):
        bug = get_object_or_404(Bug, pk=bug_id)
        return render(request, self.template_name, {'bug': bug})

class BugListView(View):
    template_name = 'bug_list.html'

    def get(self, request):
        bugs = Bug.objects.all()
        return render(request, self.template_name, {'bugs': bugs})