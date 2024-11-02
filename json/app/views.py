from django.shortcuts import render
from .forms import FamilyForm
from django.views.generic import FormView
from django.urls import reverse_lazy
import json
from django.contrib import messages
# Create your views here.


class Create(FormView):
    form_class = FamilyForm
    template_name = 'index.html'
    success_url = reverse_lazy('create')
    
    
    def form_valid(self, form):
        messages.success(self.request, "Form Submitted Successfuly!!!")
        data = form.cleaned_data
        file_path = 'john.json'
        
        try:
            with open(file_path, 'r+') as f:
                try:
                    existing_data = json.load(f)
                except json.JSONDecodeError:
                    existing_data = []
        except FileNotFoundError:
            existing_data = []
        existing_data.append(data)
        with open(file_path, 'w') as f:
            json.dump(existing_data, f, indent=4)
            
        return super().form_valid(form)