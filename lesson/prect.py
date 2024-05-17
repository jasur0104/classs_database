def menyu():
    data=input("""
    qaysi odamninng ajratib olgan malumotlari kerak
    1.Alyssa Simmons
    2.Mueller Walton
    3.Deena Bartlett
    >>>>>>>>""")
    if data=='1':
        return a1()
    elif data=='2':
        return a2()
    elif data=='3':
        return a3()
    else:
        print("Error xato malumot kiritdingiz")

def a1():
    import odam1
def a2():
    import odam2
def a3():
    import odam3
if __name__=='__main__':
    menyu()