import bottle
import Stiri_v_vrsto

Igra=Stiri_v_vrsto.Igra()
Naslov = Stiri_v_vrsto.Igra()

@bottle.get("/")
def tece() :
    return bottle.template("template.html", Igra = Igra)

@bottle.post("/<stolpec:int>/")
def vstavljanje(stolpec):
    Igra.potek(stolpec)
    bottle.redirect("/")


@bottle.post("/nova/")
def nova():
    Igra.nova_igra()
    bottle.redirect("/")

@bottle.post("/nazaj/")
def nazaj():
    Igra.nazaj()
    bottle.redirect("/")

         
    
bottle.run(reloader=True , debug=True)