from django import forms

TEAM_OPTIONS = [
    ('1', 'Manchester United'), ('3', 'Arsenal'), ('4', 'Newcastle United'), 
    ('5', 'Blackburn Rovers'), ('6', 'Tottenham Hotspur'), ('7', 'Aston Villa'), 
    ('8', 'Chelsea'), ('11', 'Everton'), ('14', 'Liverpool'), ('30', 'Bolton Wanderers'), 
    ('35', 'West Bromwich Albion'), ('39', 'Wolverhampton Wanderers'), 
    ('43', 'Manchester City'), ('45', 'Norwich City'), ('52', 'Queens Park Rangers'), 
    ('54', 'Fulham'), ('56', 'Sunderland'), ('80', 'Swansea City'), ('110', 'Stoke City'), 
    ('111', 'Wigan Athletic')
]

class IDPlayerForm(forms.Form):
	id_player = forms.IntegerField(label="ID del jugador")

class SacarWnes(forms.Form):
    uwu = forms.CharField(label="Texto")

class SeleccionarEquipo(forms.Form):
    equipo = forms.CharField(label="Equipo", widget=forms.Select(choices=TEAM_OPTIONS))
