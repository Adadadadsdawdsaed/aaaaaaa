import requests
import datetime
res_pars_list = []
respose = requests.get("https://sinoptik.ua/")
respose_text = respose.text
parse1 = respose_text.split('<p class="today-temp">')
for pars_elem1 in parse1:
    if pars_elem1.startswith('+') or pars_elem1.startswith('-') :
        for pars_elem2 in pars_elem1.split("&deg;C</p>"):
            if pars_elem2.startswith("+") or pars_elem2.startswith("-") and pars_elem2[1].isdigit():
                res_pars_list.append(pars_elem2)
timee = datetime.datetime.today()
aasdfsfa =res_pars_list[0]
print(aasdfsfa)
print(timee)