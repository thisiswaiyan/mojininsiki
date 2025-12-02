from django import forms


class PDFUploadForm(forms.Form):
    file_upload = forms.FileField(label="ファイル名", widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["file_upload"].initial = ""