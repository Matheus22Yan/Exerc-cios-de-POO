import json
from modelo_site import Site


class GerenteDeSites:
    def __init__(self):
        self.sites = {}

    def carrega(self, nome_do_arquivo):
        with open(nome_do_arquivo) as arquivo:
            dados = json.load(arquivo)
        self.sites.clear()
        for dado in dados:
            site = Site(
                id=dado.get("id"),
                categoria=dado.get("categoria"),
                data=dado["data"],
                url=dado["url"],
                notas=dado.get("notas"),
            )
            self.sites[site.id] = site


g = GerenteDeSites()
g.carrega("dados.json")
g.sites
