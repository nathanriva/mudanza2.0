from conections import session, ARTTABLE, BUYTABLE

def showAll():
    users = session.query(BUYTABLE).all()
    for user in users:
        print(user.id_compra)
    
def createBuy(id_compra, id_art, cant, in_stock):
    newart = BUYTABLE(id_compra=id_compra, id_art=id_art, cant=cant, in_stock=in_stock)
    session.add(newart)
    session.commit()
    print(newart)

def createArt(name, id):
    newart = ARTTABLE(nombre=name, id=id)
    session.add(newart)
    session.commit()
    print(newart)

def deleteArt(idtodelete):
    session.query(ARTTABLE).filter(
        ARTTABLE.id == idtodelete
    ).delete()
    session.commit()    