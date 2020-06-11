from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
import csv, io
from . import models

# Create your views here.
@permission_required('admin.can_add_log_entry')
def uni_csv_upload(request):
    template_name = 'csv_upload.html'

    csv_order = {
        'order': 'order of CSV file should be: university, ranking_system, rank, score, year'
    }

    if request.method == "POST":
        csv_file = request.FILES['file']

        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'This is not a CSV file')

        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        csv_content = csv.reader(io_string, delimiter=',', quotechar="|")
        for row in csv_content:
            _, created = models.UniRankingByYearModel.objects.update_or_create(
                university=models.UniversityModel.objects.get(title=row[1]),
                ranking_system=models.RankingSystemModel.objects.get(name=row[2]),
                rank_display=row[3],
                score=row[4],
                year=row[5],
            )
        context = {}
        return render(request, template_name, context)

    else:
        return render(request, template_name, csv_order)