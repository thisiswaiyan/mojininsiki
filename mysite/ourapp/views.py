from django.shortcuts import render
from django.http import HttpResponse
from mysite.forms import PDFUploadForm

file_extensions = ['pdf', 'jpg', 'jpeg', 'png']

def index(request):
    error_message = ""
    if request.method == "POST":
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post_values = request.POST.copy()
            f = request.FILES["file_upload"]
            filename = form.cleaned_data.get('file_upload').name.split('.')
            form.fields['file_upload'].initial = f.name
            if filename[-1].lower() not in file_extensions:
                error_message = "アップロードされたファイルでは認識検査は実行できません。"
            else:
                error_message = ""
    else:
        form = PDFUploadForm()
        
    return render(request, 'index.html', {"form": form,
                                          "error_message": error_message})