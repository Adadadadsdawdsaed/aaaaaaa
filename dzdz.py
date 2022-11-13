import requests
res_pars_list = []
respose = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
respose_text = respose.text
parse = respose_text.split('<td data-label="Офіційний курс">')
for pars_elem1 in parse:
    if pars_elem1.startswith('3'):
        for pars_elem2 in pars_elem1.split("</td>"):
            if pars_elem2.startswith("3") and pars_elem2[1].isdigit():
                res_pars_list.append(pars_elem2)
USD = res_pars_list[0]
hrywna = int(input('hrywnas: '))
print("значення доллару на сайті нацбанку пишется через кому, а для того щоб воно будл числовим повинно писатися через крапку отже я не можу це зробити точно")
print(hrywna / USD)
