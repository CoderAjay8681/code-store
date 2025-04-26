from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CodeSnippet
from .forms import CodeSnippetForm

@login_required
def code_list(request):
    snippets = CodeSnippet.objects.filter(owner=request.user)
    return render(request, 'codestore/code_list.html', {'snippets': snippets})

@login_required
def code_create(request):
    if request.method == 'POST':
        form = CodeSnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.owner = request.user
            snippet.save()
            return redirect('code_list')
    else:
        form = CodeSnippetForm()
    return render(request, 'codestore/code_form.html', {'form': form})

@login_required
def code_update(request, pk):
    snippet = get_object_or_404(CodeSnippet, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = CodeSnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect('code_list')
    else:
        form = CodeSnippetForm(instance=snippet)
    return render(request, 'codestore/code_form.html', {'form': form})

@login_required
def code_delete(request, pk):
    snippet = get_object_or_404(CodeSnippet, pk=pk, owner=request.user)
    if request.method == 'POST':
        snippet.delete()
        return redirect('code_list')
    return render(request, 'codestore/code_confirm_delete.html', {'snippet': snippet})


# Create your views here.
