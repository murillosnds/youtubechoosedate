import webbrowser

pesquisa = input("Pesquisa: ")
ano_inicial = input("Qual ano inicial: ") 
ano_final = input("Qual ano final: ") 
google = f"https://www.google.com/search?q=site%3Ayoutube.com+{pesquisa}&tbm=vid&source=lnt&tbs=cdr%3A1%2Ccd_min%3A1%2F01%2F{ano_inicial}%2Ccd_max%3A1%2F1%2F{ano_final}&tbm=vid"
webbrowser.get("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe").open(google)


