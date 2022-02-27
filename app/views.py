from django.shortcuts import render
import os
import pandas as pd
from parser1 import settings
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import mimetypes
from django.core.files.storage import FileSystemStorage
from ecl2df import grid, EclFiles, compdat, wcon, summary

def main(request):
    if request.method == 'POST':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location='static/uploads')
        filename = fs.save(myfile.name, myfile)
        well_eclfiles = EclFiles(f'static/uploads/{myfile}.DATA')
        well_compdat = compdat.df(well_eclfiles)
        df1 = pd.DataFrame(well_compdat)
        df1.to_excel('static/uploads/results.xlsx')
        chun_size = 20000
        response = StreamingHttpResponse(
            FileWrapper(
                open('static/uploads/results.xlsx', 'rb'),
                chun_size
            ),
            content_type=mimetypes.guess_type(
                'static/uploads/results.xlsx'
            )[0]
        )
        response['Content-Length'] = os.path.getsize('static/uploads/results.xlsx')
        response['Content-Disposition'] = 'attachment; filename=result.xlsx'
        return response
    return render(request, 'main.html')
