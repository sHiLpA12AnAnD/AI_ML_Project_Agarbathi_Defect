from django.shortcuts import render
import pandas as pd

# Create your views here.

# Dashboard Index View below :-)

def index(request):
    df = pd.read_csv('E:/AB Plastomech Pvt Ltd/Responsive Dashboard/Agarbathi_dashboard_ Bar_Pie_code_Dash/agarbathi.csv')
    columnlist = list(df)
    columnlist.remove("Agarbathi Classification")
    rows = df[columnlist].sum(axis=1)
    total = rows.sum()
    accepted = rows[1]
    rejected = rows[0]
    return render(request, 'dashapp/agarbathi.html', {"accepted": accepted, "rejected": rejected, "total": total})
