import requests
res_pars_list = []
respose = requests.get("https://coinmarketcap.com/")
respose_text = respose.text
parse = respose_text.split("<span>")
for pars_elem1 in parse:
    if pars_elem1.startswith('$'):
        for pars_elem2 in pars_elem1.split("</span>"):
            if pars_elem2.startswith("$") and pars_elem2[1].isdigit():
                res_pars_list.append(pars_elem2)
bitcoin = res_pars_list[0]
dogecoin = res_pars_list[7]
print(bitcoin, dogecoin)