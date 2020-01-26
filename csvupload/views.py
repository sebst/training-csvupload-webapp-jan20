from django.shortcuts import render

# Create your views here.



# HERAMB
from django.shortcuts import render
from django.http import HttpResponse
from .models import Period, Upload
from django import forms
# Create your views here.

def period_list(request):
    list_of_periods = Period.objects.all()

    return render(request, 'csvupload/period_list.html',{"periods":list_of_periods})


class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['file_name', 'csv_file']


def period_detail(request, pk):
    list_of_periods = Period.objects.all()
    selected_period = list_of_periods[pk-1]
    all_uploads = Upload.objects.filter(period=selected_period)

    form = UploadForm()

    if request.method=="GET":
        pass
        # case 1
    if request.method=="POST":
        # case 2
        instance_of_new_upload = Upload(
            user=request.user,
            period=selected_period
        )
        form = UploadForm(request.POST, files=request.FILES, instance=instance_of_new_upload)
        if form.is_valid():
            instance_of_new_upload = form.save()

    return render(request, 
                  'csvupload/period_detail.html',
                  {
                      'selected_period':selected_period,
                      'all_upload':all_uploads,
                      'form': form,
                })




# IULIAN



def mergefiles(uploads):
    new_file_lines = list()

    for upload in uploads:
        if len(new_file_lines) == 0:
            fo = upload.csv_file.open('r')
            lines = fo.readlines()
            lines1 = "\n".join( [ line.strip() for line in  lines[0:]])
            new_file_lines.append(lines1)
        else:
            fo = upload.csv_file.open('r')
            lines = fo.readlines()
            lines1 = "\n".join( [ line.strip() for line in  lines[1:]])
            new_file_lines.append(lines1)
    return "\n".join(new_file_lines)


def _mergefiles(uploads):
    
    new_file_lines = list()

    for upload in uploads:
        fo = upload.csv_file.open('r')
        lines = fo.readlines()
        new_file_lines.append(lines)
 
    new_file = ""
    for mylist in new_file_lines:
        for mystring in mylist:
            new_file += mystring
    return new_file


def concat(request, pk):
    uploads = Upload.objects.filter(period__pk=pk)
    merged_file = mergefiles(uploads)
    response = HttpResponse(merged_file, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="foo.csv"'
    return response

