from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import myform, FamilyForm
from django.urls import reverse_lazy
import json
from django.contrib import messages
# Create your views here.

class Create (FormView):
    form_class = myform
    template_name = 'index.html'
    success_url = reverse_lazy('create')
    # get_context_data = 'myform'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = myform(self.request.POST)
        else:
            context['formset'] = myform()
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Saved Successfully')
        data = form.cleaned_data
        file_path = 'john.json'
        try:
            with open(file_path, 'r+') as f:
                try:
                    existing_file = json.load(f)
                except json.JSONDecodeError:
                    existing_file = []
        except FileNotFoundError:
            existing_file = []
            
        existing_file.append(data)
        
        with open(file_path, 'w') as f:
            json.dump(existing_file, f, indent= 4)
            
        return super().form_valid(myform)
            

# def Create (request):
#     if request.method == 'POST':
#         formset = myform(request.method)
#         if formset.is_valid():
#             for form in formset:
#                 print(form.cleaned_data)
#             return redirect('create')
#     else:
#         formset = myform()
#     return render(request, 'index.html', {'formset': formset})