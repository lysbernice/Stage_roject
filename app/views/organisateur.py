from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Exetat, Etudiant, Commune, Laureat

def index(request):
    assert isinstance(request, HttpRequest)
    exetats= Exetat.objects.all().count()
    return render(
        request,
        'app/organisateur/home/index.html',
            {
            'exetats': exetats
        }
    )

# def queryset_to_list(queryset):
#     liste=[]
#     for i in range(len(queryset)):
#         liste.append(list(queryset[i].values())[0])
#     return liste
    
# def report_filter_laureat(request):
#     etudiants_list = queryset_to_list(Laureat.objects.all().values("etudiant_id").distinct())
#     etudiants = Etudiant.objects.filter(id__in=etudiants_list)
#     code_centres = queryset_to_list(Laureat.objects.all().values("code_centre").distinct())
#     code_participations = queryset_to_list(Laureat.objects.all().values("code_participation").distinct())
#     code_ecoles =  queryset_to_list(Laureat.objects.all().values("code_ecole").distinct())
   
#     # arable_land_area = queryset_to_list(Household.objects.all().values("arable_land_area").distinct())
#     # number_cattle = queryset_to_list(Household.objects.all().values("number_cattle").distinct())
#     # responsible_name = queryset_to_list(Household.objects.all().values("responsible_name").distinct())
#     # responsible_surname = queryset_to_list(Household.objects.all().values("responsible_surname").distinct())
#     # responsible_phone = queryset_to_list(Household.objects.all().values("responsible_phone").distinct())
#     # census_date = queryset_to_list(Household.objects.all().values("census_date").distinct())
#     return render(
#         request, 
        
#         'app/organisateur/repo_laureat/report_filter_laureat.html',
#         {
#             'etudiants': etudiants,
#             'code_centres': code_centres,
#             'code_participations': code_participations,
#             'code_ecoles': code_ecoles,
#             # 'arable_land_area': arable_land_area,
#             # 'number_cattle': number_cattle,
#             # 'responsible_name': responsible_name,
#             # 'responsible_surname': responsible_surname,
#             # 'responsible_phone': responsible_phone,
#             # 'census_date': census_date,
#             # 'provinces': provinces,
#             # 'communes': communes,
#         }
#         )
  
  
  
# def laureat_filter_stab(request):
#     if request.method == 'POST':
#         selected_etudiant = request.POST.get('etudiant')
#         selected_code_centre = request.POST.get('code_centre')
#         selected_code_participation = request.POST.get('code_participation')
#         selected_code_ecole = request.POST.get('code_ecole')

        
        
#         #----Data for Select Field ----#
#         etudiants_list = queryset_to_list(Laureat.objects.all().values("etudiant_id").distinct())
#         etudiants = Etudiant.objects.filter(id__in=etudiants_list)
#         code_centres = queryset_to_list(Laureat.objects.all().values("code_centre").distinct())
#         code_participations = queryset_to_list(Laureat.objects.all().values("code_participation").distinct())
#         code_ecoles =  queryset_to_list(Laureat.objects.all().values("code_ecole").distinct())

        
#         #--------Filtering--------------------------------

#         laureats = Laureat.objects.all()
#         if selected_etudiant:
#             laureats = laureats.filter(etudiant_id = selected_etudiant)

#         if selected_code_centre:
#             laureats = laureats.filter(code_centre = selected_code_centre)

#         if selected_code_participation:
#             laureats = laureats.filter(code_participation =selected_code_participation)

#         if selected_code_ecole:
#             laureatse = laureats.filter(code_ecole = selected_code_ecole)
       

#         totals_ecoles = laureats.count()
#         totals_participations= laureats.count()
#         totals_etudiants=laureats.count()
#         totals_centres=laureats.count()
#         context ={
#             'selected_etudiant':selected_etudiant,
#             'selected_code_ecole':selected_code_ecole,
#             'selected_code_participation':selected_code_participation,
#             'selected_code_ecole':selected_code_ecole,
            
#             'etudiants': etudiants,
#             'code_centres': code_centres,
#             'code_participations': code_participations,
#             'code_ecoles': code_ecoles,
            

#             'totals_ecoles':totals_ecoles,
#             'totals_participations':totals_participations,
#             'totals_etudiants':totals_etudiants,
#             'totals_centres':totals_centres,
            
#             'laureats':laureats,
#         }
#         return render(request, 'app/organisateur/repo_laureat/laureat_filter_stab.html', context)
 
      
  
