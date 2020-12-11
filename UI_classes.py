from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename, askopenfilenames
from tkinter import ttk
import pickle as pk
from PIL import Image, ImageTk
import numpy as np
from functools import partial


"""import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure"""

# import numpy as np
from os import path,chdir
# from colour import Color
chdir(path.dirname(__file__))
import Perso_class as pc




## Partie 1 -- Widgets de départ

class HomeFrame(Frame):
    """Page d'accueil"""
    def __init__(self,master,**kw):
        Frame.__init__(self,master,**kw)
        self.Char_create=Button(self,text="Créer un personnage",command=self.create_char) # bouton de création de personnage
        self.Char_import=Button(self,text="Importer un personnage",command=self.import_char) # bouton d'import de personnage
        self.Char_modif=Button(self,text="Consulter le personnage",command=self.modify_char) # bouton de consultation/modification de personnage
        self.Char_export=Button(self,text="Exporter le personnage",command=self.export_char) # bouton de consultation/modification de personnage
        self.Char_list=Listbox(self,width=10,activestyle='none', selectbackground='orange') # liste de choix du personnage à consulter

        self.Char_list.grid(row=0,column=0,rowspan=4)
        self.Char_create.grid(row=0,column=1)
        self.Char_import.grid(row=1,column=1)
        self.Char_modif.grid(row=2,column=1)
        self.Char_export.grid(row=3,column=1)

        self.Char_list.bind("<Double-Button-1>",func=self.modify_char)


    def create_char(self,):
        """ Ouvre le panneau de création de personnage"""
        self.master.children['!charcframe'].grid(row=0,column=1)


    def modify_char(self,event=None):
        """ Si un personnage a été sélectionné dans la liste, le définit comme personnage sélectionné
        et ouvre le panneau de consultation de personnage, en fermant le panneau d'accueil """
        if self.Char_list.curselection() !=():
            self.master.CDF.selectedchar=self.master.characlist[self.Char_list.curselection()[0]] # le numéro du personnage dans la liste correspond au numéro du personnage sur l'affichage
            for i in self.master.grid_slaves():
                i.grid_forget()
            self.master.children['!chardframe'].grid(row=0,column=0)


    def import_char(self):
        """ permet d'importer des personnages dans la liste """

        # on demande le fichier de personnage à importer
        filenames=askopenfilenames(title="Choisissez le fichier de personnage",filetypes=[],initialdir=path.dirname(__file__))

        if filenames:
            for filename in filenames:
                with open(filename,"rb") as fichier:
                    # si le fichier importé est bien celui d'un personnage, on le stocke dans la liste des personnages
                    perso=pk.Unpickler(fichier).load()
                    if type(perso) == (pc.player):
                        self.master.characlist.append(perso)
            self.charlist_reload()
            self.master.Menubar.refresh()



    def export_char(self):
        if self.Char_list.curselection():
            perso=self.master.characlist[self.Char_list.curselection()[0]]
            filename=asksaveasfilename(title="Choisissez le fichier de personnage",filetypes=[],initialdir=path.dirname(__file__),initialfile=[perso.name])

            if filename:
                with open(filename,"wb") as fichier:
                    # on enregistre le personnage
                    pk.Pickler(fichier).dump(perso)


    def charlist_reload(self):
        self.Char_list.delete(0,'end')
        for i in self.master.characlist:
            self.Char_list.insert(END,i.name)

    def grid(self,**kwargs):
        Frame.grid(self,kwargs)
        for i in self.master.characlist:
            self.Char_list.insert(END,i.name)

    def grid_forget(self):
        Frame.grid_forget(self)
        self.Char_list.delete(0,"end")





class CharCFrame(Frame):
    """Création du personnage"""

    def __init__(self,master):
        Frame.__init__(self,master)
        self.Name=StringVar()
        self.xp=IntVar()
        self.mage=BooleanVar()

        self.Name_lab=Label(self,text="Nom du personnage")
        self.xp_lab=Label(self,text="Expérience de base")
        self.mage_lab=Label(self,text="Mage")
        self.Name_input=Entry(self,textvariable=self.Name, width=10)
        self.xp_input=Entry(self,textvariable=self.xp,width=5)
        self.mage_input=Checkbutton(self,variable=self.mage,width=5)
        self.Char_Gen = Button(self,text="Créer le personnage",command=self.generate)

        self.Name_lab.grid(row=0,column=0)
        self.xp_lab.grid(row=1,column=0)
        self.mage_lab.grid(row=2,column=0)
        self.Name_input.grid(row=0,column=1)
        self.xp_input.grid(row=1,column=1)
        self.mage_input.grid(row=2,column=1)
        self.Char_Gen.grid(row=3,column=0,columnspan=2)

    def generate(self):
        """ fonction de création du personnage """
        character=pc.player(self.Name.get(),self.xp.get(),self.mage.get())  # on crée un joueur avec le nom et l'xp donnés
        self.master.characlist.append(character)
        with open("characters","wb") as fichier:
            pk.Pickler(fichier).dump(self.master.characlist) # on ajoute le personnage à la liste
        self.master.children["!homeframe"].charlist_reload() # recharge la liste de personnages
        self.master.Menubar.refresh()

        print(character) # affiche une phrase qui présente le personnage




class CharSFrame(Frame):
    """Suppression d'un personnage"""

    def __init__(self,master):
        Frame.__init__(self,master)
        self.charac_list=Listbox(self,activestyle='none', selectbackground='orange')
        self.Suppr_charac=Button(self,text="Supprimer le personnage",command=self.suppr_choose)


        self.charac_list.grid(row=0,column=0)
        self.Suppr_charac.grid(row=0,column=1)

    def refresh(self):
        self.charac_list.delete(0,'end')
        for key in self.master.characlist:
            self.charac_list.insert('end',key.name)

    def suppr_choose(self):
        if self.charac_list.curselection()!=():
            self.master.characlist.pop(self.charac_list.curselection()[0])
        self.refresh()
        self.master.Menubar.refresh()
        with open("characters","wb") as fichier:
            pk.Pickler(fichier).dump(self.master.characlist)


    def grid(self,**kwargs):
        Frame.grid(self,kwargs)
        self.refresh()






## Partie 2 -- Caractéristiques

class CharDFrame(Frame):
    """Affichage des statistiques d'un personnage"""

    def __init__(self,master,**kw):
        Frame.__init__(self,master,**kw)
        self.selectedchar=None
        self.selected="" # Partie des caractéristiques sélectionnée
        self.New_xp=IntVar()
        self.New_GM=IntVar()

        self.subFrame_1=Frame(self)
        Label(self.subFrame_1,text="Personnage").grid(row=0,column=0)
        Label(self.subFrame_1,text="Xp totale").grid(row=1,column=0)
        Label(self.subFrame_1,text="Xp restante").grid(row=2,column=0)
        Label(self.subFrame_1,text="Force").grid(row=3,column=0)
        Label(self.subFrame_1,text="Gagner de l'xp").grid(row=4,column=0)
        Entry(self.subFrame_1,textvariable=self.New_xp,width=3).grid(row=5,column=0)
        Label(self.subFrame_1,text="Gain MJ").grid(row=6,column=0)
        self.GM_wheel=ttk.Combobox(self.subFrame_1,state="readonly")
        Entry(self.subFrame_1,textvariable=self.New_GM,width=3).grid(row=8,column=0)
        self.plus_xp=Button(self.subFrame_1,text="+",command=self.add_xp)
        self.plus_GM=Button(self.subFrame_1,text="+",command=self.add_GM)
        self.legal_scale=Scale(self.subFrame_1,label="Légal",orient="horizontal",from_=-50,to=50,length=150,tickinterval=25,showvalue='yes',command=self.legal_onMove)

        self.restat_choice=Button(self,text="Restat",command=self.reinit_char)
        self.restat_choice.grid(row=1,column=0)

        self.GM_restat_choice=Button(self,text="Restat MJ",command=self.GM_reinit_char)
        self.GM_restat_choice.grid(row=2,column=0)

        self.subFrame_1.grid(row=0,column=0,sticky="N")


        self.NBK=CharNotebook(self)


    def reload(self,event=None):
        Label(self.subFrame_1,text=str(self.selectedchar.totalxp)).grid(row=1,column=1)
        Label(self.subFrame_1,text=str(self.selectedchar.xp)).grid(row=2,column=1)
        Label(self.subFrame_1,text=str(self.selectedchar.secondstats["symb-strength"][0])+"/"+str(self.selectedchar.secondstats["symb-strength"][1])+" ("+str(self.selectedchar.secondstats["symb-strength"][2])+")").grid(row=3,column=1)
        self.GM_wheel["values"]=list(self.selectedchar.GMstats.keys())
        self.GM_wheel.current(0)
        self.GM_wheel.grid(row=7,column=0,columnspan=2,pady="4p")
        self.plus_xp.grid(row=5,column=1)
        self.plus_GM.grid(row=8,column=1)
        self.legal_scale.set(self.selectedchar.passivestats["legal"][0])
        self.legal_scale.grid(row=9,column=0,columnspan=2)
        self.NBK.CharCF.BNDL.SYM.refresh()

    def legal_onMove(self,value):
        self.selectedchar.change_passive("legal",int(value))

    def add_xp(self,event=None):
        self.selectedchar.upxp(self.New_xp.get())
        self.reload()

    def add_GM(self,event=None):
        self.selectedchar.GM_gain(self.GM_wheel.get(),self.New_GM.get())
        self.reload()

    def reinit_char(self):
        self.selectedchar.clearstats()
        self.NBK.refresh()

    def GM_reinit_char(self):
        self.selectedchar.GM_clearstats()
        self.NBK.refresh()

    def grid(self,**kwargs):
        Frame.grid(self,kwargs)
        self.selected=""
        Label(self.subFrame_1,text=self.selectedchar.name).grid(row=0,column=1)
        self.reload()
        self.New_xp.set(0)
        self.NBK.grid(row=0,column=1,rowspan=3)
        self.NBK.CharUF.refresh()

    def grid_forget(self):
        Frame.grid_forget(self)
        for key in self.subFrame_1.grid_slaves(column=1):
            info=key.grid_info()
            if info["row"]<=4:
                key.destroy()
            else:
                key.grid_forget()
        for i in self.grid_slaves(column=1):
            i.grid_forget()




class CharNotebook(ttk.Notebook):
    """ Widget pour alterner entre le résumé, les caractéristiques et l'inventaire """

    def __init__(self,master,**kwargs):
        ttk.Notebook.__init__(self,master,**kwargs)
        self.CharCF=CharCaracFrame(self)
        self.CharUF=CharUsefulFrame(self)
        self.CharIF=CharIFrame(self)
        self.CharCompF=CharCompetFrame(self)
        self.CharSpellF=CharSpellFrame(self)
        self.add(self.CharCF,text="Caractéristiques")
        self.add(self.CharUF,text="Statistiques utiles")
        self.add(self.CharIF,text="Inventaire")
        self.add(self.CharCompF,text="Compétences")


    def refresh(self):
        self.CharCF.refresh()
        if self.master.selectedchar.mage:
            self.CharSpellF.refresh()

    def grid(self,**kwargs):
        ttk.Notebook.grid(self,**kwargs)
        self.CharCF.refresh()
        #self.CharUF=CharUsefulFrame(self)
        #self.CharIF=CharIFrame(self)
        #self.CharCompF=CharCompetFrame(self)
        if self.master.selectedchar.mage:
            self.add(self.CharSpellF,text="Sorts")

    def grid_forget(self):
        ttk.Notebook.grid_forget(self)
        if self.master.selectedchar.mage:
            self.forget(4)




class CharCaracFrame(Frame):
    """ Widget qui contient le widget de bundle et ceux de modification """

    def __init__(self,master,**kwargs):
        Frame.__init__(self,master,**kwargs)
        self.BNDL=CharBundleFrame(self)

        self.MATK=CharAtkMFrame(self)

        self.MDEF=CharDefMFrame(self)

        self.MPHY=CharPhyMFrame(self)

        self.MABI=CharAbiMFrame(self)

        self.MSOC=CharSocMFrame(self)

        self.METH=CharEthMFrame(self)

    def refresh(self):
        for i in self.grid_slaves():
            i.grid_forget()
        self.BNDL.grid(row=0,column=0,sticky="N")










class CharAtkFrame(LabelFrame):
    """ Widget d'affichage des caractéristiques d'attaque du personnage"""

    def __init__(self,master,**kwargs):
        LabelFrame.__init__(self,master,**kwargs)
        self.baselist=["hands","light","medium","heavy","throw","shield"]
        self.images={}
        self.images["mastery"]=ImageTk.PhotoImage(Image.open("Images/symb-mastery.png").resize((10,10),Image.ANTIALIAS))
        self.images["parry"]=ImageTk.PhotoImage(Image.open("Images/symb-parry.png").resize((12,15),Image.ANTIALIAS))
        i=0
        for key in self.baselist[:-1]:
            Label(self,image=self.images["mastery"],text=" =",compound="left").grid(row=2*i,column=2)
            Label(self).grid(row=2*i,column=3)
            i+=1
        Label(self,image=self.images["parry"],text=" =",compound="left").grid(row=2*i,column=2)
        Label(self).grid(row=2*i,column=3)

        i=0
        for key in ["Mains nues","Armes légères","Armes moyennes","Armes lourdes","Armes de jet","Bouclier"]:
            Label(self,text=key).grid(row=2*i,column=0)
            Canvas(self,width=100,height=15,bg="white").grid(row=2*i+1,column=0)
            i+=1
        # self.Char_modif.grid(row=2*i,column=0)

        self.bind("<Button-1>",func=self.modifychar)
        for i in self.grid_slaves():
            i.bind("<Button-1>",func=self.modifychar)

    def refresh(self):
        i=0
        for key in self.grid_slaves(column=3):
            if i > 0:
                key["text"]=(str(self.master.master.master.master.selectedchar.secondstats["symb-mastery"][self.baselist[5-i]]))
            else:
                key["text"]=(str(self.master.master.master.master.selectedchar.secondstats["symb-parry"]))
            i+=1

        i=1
        for key in self.baselist:
            self.grid_slaves(row=i,column=0)[0].delete("all")
            self.grid_slaves(row=i,column=0)[0].create_rectangle(0,0,self.master.master.master.master.selectedchar.basestats[key][0]//2,16,fill="black",tag="jauge")
            if self.master.master.master.master.selectedchar.basestats[key][0]<=100:
                self.grid_slaves(row=i,column=0)[0].create_text(self.master.master.master.master.selectedchar.basestats[key][0]//2+10,8,text=str(self.master.master.master.master.selectedchar.basestats[key][0]),tag="stat")
            elif self.master.master.master.master.selectedchar.basestats[key][0]>100:
                self.grid_slaves(row=i,column=0)[0].create_text(self.master.master.master.master.selectedchar.basestats[key][0]//2-10,8,text=str(self.master.master.master.master.selectedchar.basestats[key][0]),fill="white",tag="stat")
            i+=2


    def modifychar(self,event=None):
        """ Affiche la fenêtre de modification du personnage """
        for i in self.master.master.grid_slaves(column=3):
            i.grid_forget()
        self.master.master.MATK.grid(row=0,column=3)

    def grid(self,**kwargs):
        LabelFrame.grid(self,kwargs)
        self.refresh()




class CharAtkMFrame(Frame):
    """ Widget de modification des caractéristiques d'attaque du personnage"""

    def __init__(self,master):
        Frame.__init__(self,master)
        self.New_carac=IntVar()
        self.baselist=["hands","light","medium","heavy","throw","shield"]

        Label(self,text="Utiliser l'XP").grid(row=0,column=0,columnspan=2,sticky=W)

        self.statlist=ttk.Combobox(self,values=["Mains nues","Armes légères","Armes moyennes","Armes lourdes","Armes de jet","Bouclier"],state="readonly")
        self.statlist.current(0)
        self.add_stat=Entry(self,textvariable=self.New_carac)
        self.Register_new=Button(self,text="Ajouter",command=self.register)

        self.statlist.grid(row=1,column=0)
        self.add_stat.grid(row=1,column=1)
        self.Register_new.grid(row=2,column=0,columnspan=2)

    def register(self,event=None):
        """ Transforme l'expérience en points de la caractéristique sélectionnée avec statlist, et enregistre la nouvelle configuration du personnage"""
        self.master.master.master.selectedchar.upstats(self.baselist[self.statlist.current()],self.New_carac.get())
        self.New_carac.set(0)
        self.master.master.master.reload()
        self.master.BNDL.ATK.refresh()
        # with open("characters","wb") as fichier:
        #     pk.Pickler(fichier).dump(self.master.master.master.master.characlist)




class CharDefFrame(LabelFrame):
    """ Widget d'affichage des caractéristiques d'armure du personnage"""

    def __init__(self,master,**kwargs):
        LabelFrame.__init__(self,master,kwargs)
        self.baselist=["armor"]
        self.images={}
        self.images["armor"]=ImageTk.PhotoImage(Image.open("Images/symb-armor.png").resize((12,20),Image.ANTIALIAS))

        i=0
        for key in ["Armure"]:
            Label(self,text=key).grid(row=2*i,column=0)
            Canvas(self,width=100,height=15,bg="white").grid(row=2*i+1,column=0)

            Label(self,text=" =",image=self.images["armor"],compound="left").grid(row=0,column=1)
            Label(self).grid(row=0,column=2)
            i+=1
        Label(self,text="Palier d'armure").grid(row=2*i,column=0)
        Label(self).grid(row=2*i,column=1)

        self.bind("<Button-1>",func=self.modifychar)
        for i in self.grid_slaves():
            i.bind("<Button-1>",func=self.modifychar)


    def refresh(self):
        for i in self.grid_slaves(column=2):
            i["text"]=self.master.master.master.master.selectedchar.secondstats["symb-armor"]

        i=1
        for key in self.baselist:
            self.grid_slaves(row=i,column=0)[0].delete("all")
            self.grid_slaves(row=i,column=0)[0].create_rectangle(0,0,self.master.master.master.master.selectedchar.basestats[key][0]//2,16,fill="black",tag="jauge")
            if self.master.master.master.master.selectedchar.basestats[key][0]<=100:
                self.grid_slaves(row=i,column=0)[0].create_text(self.master.master.master.master.selectedchar.basestats[key][0]//2+10,8,text=str(self.master.master.master.master.selectedchar.basestats[key][0]),tag="stat")
            elif self.master.master.master.master.selectedchar.basestats[key][0]>100:
                self.grid_slaves(row=i,column=0)[0].create_text(self.master.master.master.master.selectedchar.basestats[key][0]//2-10,8,text=str(self.master.master.master.master.selectedchar.basestats[key][0]),fill="white",tag="stat")
            i+=2
        self.grid_slaves(row=2,column=1)[0]["text"]=str(self.master.master.master.master.selectedchar.secondstats["armor-level"])
        # Label(self,text=str(self.master.master.master.selectedchar.secondstats["armor-level"])).grid(row=i-1,column=1)

    def modifychar(self,event=None):
        """ Affiche la fenêtre de modification du personnage """
        for i in self.master.master.grid_slaves(column=3):
            i.grid_forget()
        self.master.master.MDEF.grid(row=0,column=3)

    def grid(self,**kwargs):
        LabelFrame.grid(self,kwargs)
        self.refresh()




class CharDefMFrame(Frame):
    """ Widget de modification des caractéristiques d'armure du personnage"""

    def __init__(self,master):
        Frame.__init__(self,master)
        self.baselist=["armor"]
        self.New_carac=IntVar()
        self.New_third=IntVar()

        Label(self,text="Utiliser l'XP").grid(row=0,column=0,columnspan=2,sticky=W)
        Label(self,text="Utiliser l'Armure").grid(row=3,column=0,columnspan=2,sticky=W)

        self.statlist=ttk.Combobox(self,values=["Armure"],state="readonly")
        self.statlist.current(0)
        self.add_stat=Entry(self,textvariable=self.New_carac)
        self.Register_new=Button(self,text="Ajouter",command=self.register)

        self.statthird=ttk.Combobox(self,values=["Heaume","Spallières","Brassards","Avant-bras","Plastron","Jointures","Tassette","Cuissots","Grèves","Solerets"],state="readonly")
        self.statthird.current(0)
        self.add_third=Entry(self,textvariable=self.New_third)
        self.Register_third=Button(self,text="Ajouter",command=self.register_third)


        self.statlist.grid(row=1,column=0)
        self.add_stat.grid(row=1,column=1)
        self.Register_new.grid(row=2,column=0,columnspan=2)

        self.statthird.grid(row=4,column=0)
        self.add_third.grid(row=4,column=1)
        self.Register_third.grid(row=5,column=0,columnspan=2)

    def register(self,event=None):
        """ Transforme l'expérience en points de la caractéristique sélectionnée avec statlist, et enregistre la nouvelle configuration du personnage"""
        self.master.master.master.selectedchar.upstats(self.baselist[self.statlist.current()],self.New_carac.get())
        self.New_carac.set(0)
        self.master.master.master.reload()
        self.master.BNDL.DEF.refresh()

    def register_third(self,event=None):
        """ Consomme un symbole d'armure pour l'assigner à une pièce d'équipement """
        self.master.master.master.selectedchar.upstats("invested_armor",self.New_third.get(),self.statthird.get())
        self.New_third.set(0)
        self.master.BNDL.DEF.refresh()




class CharPhyFrame(LabelFrame):
    """ Widget d'affichage des caractéristiques physiques du personnage"""

    def __init__(self,master,**kwargs):
        LabelFrame.__init__(self,master,kwargs)
        self.baselist=["training","dexterity","mobility"]
        self.secondlist=["ability","mobility"]
        self.thirdlist=["phys-res"]
        self.images={}
        self.images["ability"]=ImageTk.PhotoImage(Image.open("Images/symb-ability.png").resize((15,15),Image.ANTIALIAS))
        self.images["mobility"]=ImageTk.PhotoImage(Image.open("Images/symb-mobility.png").resize((15,10),Image.ANTIALIAS))

        i=1
        for key in self.secondlist:
            Label(self,text=" =",image=self.images[key],compound="left").grid(row=2*i,column=1)
            Label(self).grid(row=2*i,column=2)
            i+=1
        i=0
        for key in ["Entrainement physique","Dextérité/Habileté","Mobilité","Résistance physique"]:
            Label(self,text=key).grid(row=2*i,column=0)
            Canvas(self,width=100,height=15,bg="white").grid(row=2*i+1,column=0)
            i+=1

        self.bind("<Button-1>",func=self.modifychar)
        for i in self.grid_slaves():
            i.bind("<Button-1>",func=self.modifychar)

    def refresh(self):
        i=1
        for key in self.grid_slaves(column=2):
            if i ==2:
                key["text"]=self.master.master.master.master.selectedchar.secondstats["symb-ability"]
            else:
                key["text"]=self.master.master.master.master.selectedchar.secondstats["symb-mobility"]
            i+=1
        i=1
        for key in self.baselist:
            self.grid_slaves(row=i,column=0)[0].delete("all")
            self.grid_slaves(row=i,column=0)[0].create_rectangle(0,0,self.master.master.master.master.selectedchar.basestats[key][0]//2,16,fill="black",tag="jauge")
            if self.master.master.master.master.selectedchar.basestats[key][0]<=100:
                self.grid_slaves(row=i,column=0)[0].create_text(self.master.master.master.master.selectedchar.basestats[key][0]//2+10,8,text=str(self.master.master.master.master.selectedchar.basestats[key][0]),tag="stat")
            elif self.master.master.master.master.selectedchar.basestats[key][0]>100:
                self.grid_slaves(row=i,column=0)[0].create_text(self.master.master.master.master.selectedchar.basestats[key][0]//2-10,8,text=str(self.master.master.master.master.selectedchar.basestats[key][0]),fill="white",tag="stat")
            i+=2
        for key in self.thirdlist:
            self.grid_slaves(row=i,column=0)[0].delete("all")
            self.grid_slaves(row=i,column=0)[0].create_rectangle(0,0,self.master.master.master.master.selectedchar.thirdstats[key][0]//2,16,fill="black",tag="jauge")
            if self.master.master.master.master.selectedchar.thirdstats[key][0]<=100:
                self.grid_slaves(row=i,column=0)[0].create_text(self.master.master.master.master.selectedchar.thirdstats[key][0]//2+10,8,text=str(self.master.master.master.master.selectedchar.thirdstats[key][0]),tag="stat")
            elif self.master.master.master.master.selectedchar.thirdstats[key][0]>100:
                self.grid_slaves(row=i,column=0)[0].create_text(self.master.master.master.master.selectedchar.thirdstats[key][0]//2-10,8,text=str(self.master.master.master.master.selectedchar.thirdstats[key][0]),fill="white",tag="stat")
            i+=2

    def modifychar(self,event=None):
        """ Affiche la fenêtre de modification du personnage """
        for i in self.master.master.grid_slaves(column=3):
            i.grid_forget()
        self.master.master.MPHY.grid(row=0,column=3)

    def grid(self,**kwargs):
        LabelFrame.grid(self,kwargs)
        self.refresh()




class CharPhyMFrame(Frame):
    """ Widget de modification des caractéristiques physiques du personnage"""

    def __init__(self,master):
        Frame.__init__(self,master)
        self.baselist=["training","dexterity","mobility"]
        self.thirdlist=["phys-res"]
        self.New_carac=IntVar()
        self.New_third=IntVar()

        Label(self,text="Utiliser l'XP").grid(row=0,column=0,columnspan=2,sticky=W)

        self.statlist=ttk.Combobox(self,values=["Entrainement physique","Dextérité/Habileté","Mobilité"],state="readonly",width=21)
        self.statlist.current(0)
        self.add_stat=Entry(self,textvariable=self.New_carac)
        self.Register_new=Button(self,text="Ajouter",command=self.register)

        Label(self,text="Utiliser la force").grid(row=3,column=0,columnspan=2,sticky=W)
        self.statthird=ttk.Combobox(self,values=["Résistance Physique"],state="readonly",width=21)
        self.statthird.current(0)
        self.add_third=Entry(self,textvariable=self.New_third)
        self.Register_third=Button(self,text="Ajouter",command=self.register_third)

        self.statlist.grid(row=1,column=0)
        self.add_stat.grid(row=1,column=1)
        self.Register_new.grid(row=2,column=0,columnspan=2)

        self.statthird.grid(row=4,column=0)
        self.add_third.grid(row=4,column=1)
        self.Register_third.grid(row=5,column=0,columnspan=2)

        Label(self,text="Convertir l'initiative en habileté").grid(row=6,column=0)
        Button(self,text="+1",command=self.launch_convert).grid(row=7,column=0,sticky="w")

    def register(self,event=None):
        """ Transforme l'expérience en points de la caractéristique sélectionnée avec statlist, et enregistre la nouvelle configuration du personnage"""
        self.master.master.master.selectedchar.upstats(self.baselist[self.statlist.current()],self.New_carac.get())
        self.New_carac.set(0)
        self.master.master.master.reload()
        self.master.BNDL.PHY.refresh()

    def register_third(self,event=None):
        """ Transforme l'expérience en points de la caractéristique sélectionnée avec statlist, et enregistre la nouvelle configuration du personnage"""
        self.master.master.master.selectedchar.upstats(self.thirdlist[self.statthird.current()],self.New_third.get())
        self.New_third.set(0)
        self.master.master.master.reload()
        self.master.BNDL.PHY.refresh()

    def launch_convert(self):
        self.master.master.master.selectedchar.convert_init(1)
        self.master.BNDL.PHY.refresh()
        self.master.BNDL.ABI.refresh()



class CharAbiFrame(LabelFrame):
    """ Widget d'affichage des caractéristiques d'habileté du personnage"""

    def __init__(self,master,**kwargs):
        LabelFrame.__init__(self,master,kwargs)
        self.baselist=["perception","stealth","reflex","wit","mental-res"]
        self.secondlist=["perception","S","stealth","T","init","light","mental"]
        self.sizelist={"perception":(12,15),"S":(6,9),"stealth":(18,8),"T":(6,9),"init":(15,10),"light":(12,15),"mental":(12,12)}
        self.images={}
        for key in self.secondlist:
            self.images[key]=ImageTk.PhotoImage(Image.open("Images/symb-"+key+".png").resize(self.sizelist[key],Image.ANTIALIAS))


        i=0
        for key in ["Perception","Furtivité","Réflexes","Intelligence","Résistance mentale"]:
            Label(self,text=key).grid(row=2*i,column=0)
            Canvas(self,width=100,height=15,bg="white").grid(row=2*i+1,column=0)
            if i<2:
                Label(self,text=" =",image=self.images[self.secondlist[2*i]],compound="left").grid(row=2*i,column=1)
                Label(self).grid(row=2*i,column=2)
                Label(self,text=" =",image=self.images[self.secondlist[2*i+1]],compound="left").grid(row=2*i+1,column=1)
                Label(self).grid(row=2*i+1,column=2)
            else:
                Label(self,text=" =",image=self.images[self.secondlist[i+2]],compound="left").grid(row=2*i,column=1)
                Label(self).grid(row=2*i,column=2)
            i+=1


        self.bind("<Button-1>",func=self.modifychar)
        for i in self.grid_slaves():
            i.bind("<Button-1>",func=self.modifychar)

    def refresh(self):
        i=1
        for key in self.grid_slaves(column=2):
            key["text"]=self.master.master.master.master.selectedchar.secondstats["symb-"+self.secondlist[len(self.secondlist)-i]]
            i+=1
        i=1
        for key in self.baselist:
            self.grid_slaves(row=i,column=0)[0].delete("all")
            self.grid_slaves(row=i,column=0)[0].create_rectangle(0,0,self.master.master.master.master.selectedchar.basestats[key][0]//2,16,fill="black",tag="jauge")
            if self.master.master.master.master.selectedchar.basestats[key][0]<=100:
                self.grid_slaves(row=i,column=0)[0].create_text(self.master.master.master.master.selectedchar.basestats[key][0]//2+10,8,text=str(self.master.master.master.master.selectedchar.basestats[key][0]),tag="stat")
            elif self.master.master.master.master.selectedchar.basestats[key][0]>100:
                self.grid_slaves(row=i,column=0)[0].create_text(self.master.master.master.master.selectedchar.basestats[key][0]//2-10,8,text=str(self.master.master.master.master.selectedchar.basestats[key][0]),fill="white",tag="stat")
            i+=2

    def modifychar(self,event=None):
        """ Affiche la fenêtre de modification du personnage """
        for i in self.master.master.grid_slaves(column=3):
            i.grid_forget()
        self.master.master.MABI.grid(row=0,column=3)


    def grid(self,**kwargs):
        LabelFrame.grid(self,kwargs)
        self.refresh()




class CharAbiMFrame(Frame):
    """ Widget de modification des caractéristiques d'habileté du personnage"""

    def __init__(self,master):
        Frame.__init__(self,master)
        self.baselist=["perception","stealth","reflex","wit","mental-res"]
        self.addlist={}
        self.perceplist=[["intention","thing-info","bestiary"],["trap","find","tracking"],["ennemies","threat","curse"]]
        self.furtiflist=[["ground","moving","assassination"],["shadow","not-moving","identity"],["smell","disguise","nature-field"]]

        self.New_carac=IntVar()

        Label(self,text="Utiliser l'XP").grid(row=0,column=0,columnspan=2,sticky=W)

        self.statlist=ttk.Combobox(self,values=["Perception","Furtivité","Réflexes","Intelligence","Résistance mentale"],state="readonly")
        self.statlist.current(0)
        self.add_stat=Entry(self,textvariable=self.New_carac)
        self.Register_new=Button(self,text="Ajouter",command=self.register)

        self.statlist.grid(row=1,column=0,sticky="e")
        self.add_stat.grid(row=1,column=1,sticky="w")
        self.Register_new.grid(row=2,column=0,columnspan=2)


        # sens
        ttk.Separator(self,orient="horizontal").grid(row=3,column=0,columnspan=2,sticky="we",pady="4p")

        self.senseFrame=Frame(self)
        self.senseFrame.grid(row=4,column=0,columnspan=2,sticky="w")
        Label(self.senseFrame,text="Améliorer ses sens").grid(row=0,column=0)
        i=1
        for key in ["Vue : ","Ouïe : ","Odorat : "]:
            Label(self.senseFrame,text=key).grid(row=i,column=0,sticky="e")
            i+=1

        self.add_sight=Button(self.senseFrame,text="+",command=partial(self.add_sense,"sight"),state="disabled")
        self.add_hearing=Button(self.senseFrame,text="+",command=partial(self.add_sense,"hearing"),state="disabled")
        self.add_smell=Button(self.senseFrame,text="+",command=partial(self.add_sense,"smell"),state="disabled")

        self.add_sight.grid(row=1,column=2,sticky="e")
        self.add_hearing.grid(row=2,column=2,sticky="e")
        self.add_smell.grid(row=3,column=2,sticky="e")


        ttk.Separator(self,orient="horizontal").grid(row=5,column=0,columnspan=2,sticky="we",pady="4p")

        # perception
        self.percepFrame=Frame(self)
        self.percepFrame.grid(row=6,column=0,columnspan=2)
        Label(self.percepFrame,text="Perception").grid(row=0,column=0)
        i=0
        for key in ["Indice : ","Terrain : ","Embuscade : "]:
            Label(self.percepFrame,text=key).grid(row=1,column=3*i,sticky="w")
            i+=1

        i=2
        for key in ["Intention : ","Objet-info : ","Bestiaire : "]:
            Label(self.percepFrame,text=key).grid(row=i,column=0,sticky="e")
            i+=1

        i=2
        for key in ["Piège : ","Trouver Objets : ","Pistage : "]:
            Label(self.percepFrame,text=key).grid(row=i,column=3,sticky="e")
            i+=1

        i=2
        for key in ["Adversaires : ","Menace : ","Malédiction : "]:
            Label(self.percepFrame,text=key).grid(row=i,column=6,sticky="e")
            i+=1

        for j in range(3):
            i=2
            for stat in self.perceplist[j]:
                self.addlist[stat]=Button(self.percepFrame,text="+",command=partial(self.invest_furtif,stat),state="disabled")
                self.addlist[stat].grid(row=i,column=3*j+2)
                i+=1


        ttk.Separator(self,orient="horizontal").grid(row=7,column=0,columnspan=2,sticky="we",pady="4p")

        # furtivité
        self.stealthFrame=Frame(self)
        self.stealthFrame.grid(row=8,column=0,columnspan=2)
        Label(self.stealthFrame,text="Furtivité").grid(row=0,column=0)
        i=0
        for key in ["Silence : ","Dissimulation : ","Camouflage : "]:
            Label(self.stealthFrame,text=key).grid(row=1,column=3*i,sticky="w")
            i+=1

        i=2
        for key in ["Sol : ","Déplacement : ","Assassinat : "]:
            Label(self.stealthFrame,text=key).grid(row=i,column=0,sticky="e")
            i+=1

        i=2
        for key in ["Ombre : ","Immobilité : ","Identité : "]:
            Label(self.stealthFrame,text=key).grid(row=i,column=3,sticky="e")
            i+=1

        i=2
        for key in ["Odeur : ","Déguisement : ","Nature/Terrain : "]:
            Label(self.stealthFrame,text=key).grid(row=i,column=6,sticky="e")
            i+=1

        for j in range(3):
            i=2
            for stat in self.furtiflist[j]:
                self.addlist[stat]=Button(self.stealthFrame,text="+",command=partial(self.invest_furtif,stat),state="disabled")
                self.addlist[stat].grid(row=i,column=3*j+2)
                i+=1

        ttk.Separator(self,orient="horizontal").grid(row=9,column=0,columnspan=2,sticky="we",pady="4p")

        # action dissimulée
        self.hiddenFrame=Frame(self)
        self.hiddenFrame.grid(row=10,column=0,columnspan=2)
        Label(self.hiddenFrame,text="Action dissimulée").grid(row=0,column=0)
        i=0
        for key in ["Vol à la tire : ","Embuscade : ","Fuite : "]:
            Label(self.hiddenFrame,text=key).grid(row=1,column=3*i,sticky="e")
            i+=1


        j=0
        for stat in ["thievery","ambush","escape"]:
            self.addlist[stat]=Button(self.hiddenFrame,text="+",command=partial(self.invest_furtif,stat),state="disabled")
            self.addlist[stat].grid(row=1,column=3*j+2)
            j+=1




    def register(self,event=None):
        """ Transforme l'expérience en points de la caractéristique sélectionnée avec statlist, et enregistre la nouvelle configuration du personnage"""
        self.master.master.master.selectedchar.upstats(self.baselist[self.statlist.current()],self.New_carac.get())
        self.New_carac.set(0)
        self.master.master.master.reload()
        self.master.BNDL.ABI.refresh()
        self.refresh()



    def refresh(self):
        """ Fonction qui rafraichit toutes les zones de tier 3 """
        for i in self.senseFrame.grid_slaves():
            info=i.grid_info()
            if info["row"]>=1 and info["column"]==1:
                i.destroy()
            elif info["row"]==0 and info["column"]==3:
                i.destroy()

        for i in self.stealthFrame.grid_slaves():
            info=i.grid_info()
            if info["row"]>=2 and info["column"] in [1,4,7]:
                i.destroy()
            elif info["row"]==0 and info["column"]==9:
                i.destroy()

        for i in self.percepFrame.grid_slaves():
            info=i.grid_info()
            if info["row"]>=2 and info["column"] in [1,4,7]:
                i.destroy()
            elif info["row"]==0 and info["column"]==9:
                i.destroy()

        # sens
        if self.master.master.master.selectedchar.secondstats["symb-S"]:
            Label(self.senseFrame,text="Points restants : "+str(self.master.master.master.selectedchar.secondstats["symb-S"])).grid(row=0,column=3,sticky="w")
            self.add_sight["state"]="normal"
            self.add_hearing["state"]="normal"
            self.add_smell["state"]="normal"
        else:
            self.add_sight["state"]="disabled"
            self.add_hearing["state"]="disabled"
            self.add_smell["state"]="disabled"

        i=1
        for key in ["sight","hearing","smell"]:
            Label(self.senseFrame,text=self.master.master.master.selectedchar.thirdstats[key]).grid(row=i,column=1)
            i+=1

        # furtivité
        if self.master.master.master.selectedchar.secondstats["symb-T"]+self.master.master.master.selectedchar.secondstats["symb-stealth"][0]+self.master.master.master.selectedchar.secondstats["symb-stealth"][1]:
            Label(self.stealthFrame,text="Points restants : "+str(self.master.master.master.selectedchar.secondstats["symb-T"]+self.master.master.master.selectedchar.secondstats["symb-stealth"][0]+self.master.master.master.selectedchar.secondstats["symb-stealth"][1])).grid(row=0,column=9,sticky="w")
            for j in range(3):
                for key in self.furtiflist[j]:
                    self.addlist[key]["state"]="normal"
        else:
            for j in range(3):
                for key in self.furtiflist[j]:
                    self.addlist[key]["state"]="disabled"

        j=0
        for key in ["silence","hiding","camo"]:
            i=2
            for stat in self.furtiflist[j]:
                Label(self.stealthFrame,text=self.master.master.master.selectedchar.thirdstats[key][stat]).grid(row=i,column=3*j+1)
                i+=1

            j+=1

        # perception
        if self.master.master.master.selectedchar.secondstats["symb-perception"]:
            Label(self.percepFrame,text="Points restants : "+str(self.master.master.master.selectedchar.secondstats["symb-perception"])).grid(row=0,column=9,sticky="w")
            for j in range(3):
                for key in self.perceplist[j]:
                    self.addlist[key]["state"]="normal"
        else:
            for j in range(3):
                for key in self.perceplist[j]:
                    self.addlist[key]["state"]="disabled"

        j=0
        for key in ["clue","field","ambush"]:
            i=2
            for stat in self.perceplist[j]:
                Label(self.percepFrame,text=self.master.master.master.selectedchar.thirdstats[key][stat]).grid(row=i,column=3*j+1)
                i+=1

            j+=1

        # action dissimulée
        if self.master.master.master.selectedchar.secondstats["symb-ability"][0]+self.master.master.master.selectedchar.secondstats["symb-ps_T"][0]+self.master.master.master.selectedchar.secondstats["symb-T"]:
            Label(self.hiddenFrame,text="Points restants : "+str(self.master.master.master.selectedchar.secondstats["symb-ability"][0]+self.master.master.master.selectedchar.secondstats["symb-ps_T"][0]+self.master.master.master.selectedchar.secondstats["symb-T"])).grid(row=0,column=9,sticky="w")
            for key in ["thievery","ambush","escape"]:
                self.addlist[key]["state"]="normal"
        else:
            for key in ["thievery","ambush","escape"]:
                self.addlist[key]["state"]="disabled"

        j=0
        for stat in ["thievery","ambush","escape"]:
            Label(self.hiddenFrame,text=self.master.master.master.selectedchar.thirdstats["hidden_action"][stat]).grid(row=1,column=3*j+1)
            j+=1




    def add_sense(self,stat):
        self.master.master.master.selectedchar.upstats(stat,1)
        self.refresh()
        self.master.BNDL.ABI.refresh()

    def invest_furtif(self,stat):
        """ Permet de consommer le tier 2 et obtenir du tier 3 """
        self.master.master.master.selectedchar.upstats(stat,1)
        self.refresh()
        self.master.BNDL.ABI.refresh()


    def grid(self,**kw):
        #self.refresh()
        Frame.grid(self,**kw)






class CharSocFrame(LabelFrame):
    """ Widget d'affichage des caractéristiques sociales du personnage"""

    def __init__(self,master,**kwargs):
        LabelFrame.__init__(self,master,kwargs)
        self.baselist=["charisma","trading","luck"]
        self.secondlist=["charisma","trading","luck"]
        self.sizelist={"charisma":(12,12),"trading":(15,13),"luck":(12,18)}
        self.images={}
        for key in self.secondlist:
            self.images[key]=ImageTk.PhotoImage(Image.open("Images/symb-"+key+".png").resize(self.sizelist[key],Image.ANTIALIAS))
        i=0
        for key in ["Charisme","Commerce","Chance"]:
            Label(self,text=key).grid(row=2*i,column=0)
            Canvas(self,width=100,height=15,bg="white").grid(row=2*i+1,column=0)
            Label(self,text=" =",image=self.images[self.secondlist[i]],compound="left").grid(row=2*i,column=1)
            Label(self).grid(row=2*i,column=2)
            i+=1



        self.bind("<Button-1>",func=self.modifychar)
        for i in self.grid_slaves():
            i.bind("<Button-1>",func=self.modifychar)

    def refresh(self):
        i=1
        for key in self.grid_slaves(column=2):
            key["text"]=self.master.master.master.master.selectedchar.secondstats["symb-"+self.secondlist[len(self.secondlist)-i]]
            i+=1
        i=1
        for key in self.baselist:
            self.grid_slaves(row=i,column=0)[0].delete("all")
            self.grid_slaves(row=i,column=0)[0].create_rectangle(0,0,self.master.master.master.master.selectedchar.basestats[key][0]//2,16,fill="black",tag="jauge")
            if self.master.master.master.master.selectedchar.basestats[key][0]<=100:
                self.grid_slaves(row=i,column=0)[0].create_text(self.master.master.master.master.selectedchar.basestats[key][0]//2+10,8,text=str(self.master.master.master.master.selectedchar.basestats[key][0]),tag="stat")
            elif self.master.master.master.master.selectedchar.basestats[key][0]>100:
                self.grid_slaves(row=i,column=0)[0].create_text(self.master.master.master.master.selectedchar.basestats[key][0]//2-10,8,text=str(self.master.master.master.master.selectedchar.basestats[key][0]),fill="white",tag="stat")
            i+=2

    def modifychar(self,event=None):
        """ Affiche la fenêtre de modification du personnage """
        for i in self.master.master.grid_slaves(column=3):
            i.grid_forget()
        self.master.master.MSOC.grid(row=0,column=3)

    def grid(self,**kwargs):
        LabelFrame.grid(self,kwargs)
        self.refresh()




class CharSocMFrame(Frame):
    """ Widget de modification des caractéristiques sociales du personnage"""

    def __init__(self,master):
        Frame.__init__(self,master)
        self.baselist=["charisma","trading","luck"]
        self.New_carac=IntVar()

        Label(self,text="Utiliser l'XP").grid(row=0,column=0,columnspan=2,sticky=W)

        self.statlist=ttk.Combobox(self,values=["Charisme","Commerce","Chance"],state="readonly")
        self.statlist.current(0)
        self.add_stat=Entry(self,textvariable=self.New_carac)
        self.Register_new=Button(self,text="Ajouter",command=self.register)

        self.statlist.grid(row=1,column=0)
        self.add_stat.grid(row=1,column=1)
        self.Register_new.grid(row=2,column=0,columnspan=2)

    def register(self,event=None):
        """ Transforme l'expérience en points de la caractéristique sélectionnée avec statlist, et enregistre la nouvelle configuration du personnage"""
        self.master.master.master.selectedchar.upstats(self.baselist[self.statlist.current()],self.New_carac.get())
        self.New_carac.set(0)
        self.master.master.master.reload()
        self.master.BNDL.SOC.refresh()




class CharEthFrame(LabelFrame):
    """ Widget d'affichage des caractéristiques d'Ether si le personnage est un mage"""

    def __init__(self,master,**kwargs):
        LabelFrame.__init__(self,master,kwargs)
        self.baselist=["power","mastery","sensitivity"]
        self.secondlist=["lightning","sensi","aura"]
        self.sizelist={"lightning":(12,15),"sensi":(12,15),"aura":(15,15)}
        self.images={}
        for key in self.secondlist:
            if key!="":
                self.images[key]=ImageTk.PhotoImage(Image.open("Images/symb-"+key+".png").resize(self.sizelist[key],Image.ANTIALIAS))
        i=0
        for key in ["Puissance","Maîtrise","Sensibilité","Aura"]:
            Label(self,text=key).grid(row=2*i,column=0)
            Canvas(self,width=100,height=15,bg="white").grid(row=2*i+1,column=0)
            if i!=1:
                if i>1:
                    Label(self,text=" =",image=self.images[self.secondlist[i-1]],compound="left").grid(row=2*i,column=1)
                    Label(self).grid(row=2*i,column=2)
                else:
                    Label(self,text=" =",image=self.images[self.secondlist[i]],compound="left").grid(row=2*i,column=1)
                    Label(self).grid(row=2*i,column=2)

            i+=1

        self.bind("<Button-1>",func=self.modifychar)
        for i in self.grid_slaves():
            i.bind("<Button-1>",func=self.modifychar)

    def refresh(self):
        i=1
        for key in self.grid_slaves(column=2):
            key["text"]=self.master.master.master.master.selectedchar.secondstats["symb-"+self.secondlist[len(self.secondlist)-i]]
            i+=1
        i=1
        for key in self.baselist:
            self.grid_slaves(row=i,column=0)[0].delete("all")
            self.grid_slaves(row=i,column=0)[0].create_rectangle(0,0,self.master.master.master.master.selectedchar.basestats[key][0]//2,16,fill="black",tag="jauge")
            if self.master.master.master.master.selectedchar.basestats[key][0]<=100:
                self.grid_slaves(row=i,column=0)[0].create_text(self.master.master.master.master.selectedchar.basestats[key][0]//2+10,8,text=str(self.master.master.master.master.selectedchar.basestats[key][0]),tag="stat")
            elif self.master.master.master.master.selectedchar.basestats[key][0]>100:
                self.grid_slaves(row=i,column=0)[0].create_text(self.master.master.master.master.selectedchar.basestats[key][0]//2-10,8,text=str(self.master.master.master.master.selectedchar.basestats[key][0]),fill="white",tag="stat")
            i+=2

        self.grid_slaves(row=i,column=0)[0].delete("all")
        self.grid_slaves(row=i,column=0)[0].create_rectangle(0,0,self.master.master.master.master.selectedchar.secondstats["aura"][0]//2,16,fill="black",tag="jauge")
        if self.master.master.master.master.selectedchar.secondstats["aura"][0]<=100:
            self.grid_slaves(row=i,column=0)[0].create_text(self.master.master.master.master.selectedchar.secondstats["aura"][0]//2+10,8,text=str(self.master.master.master.master.selectedchar.secondstats["aura"][0]),tag="stat")
        elif self.master.master.master.master.selectedchar.secondstats["aura"][0]>100:
            self.grid_slaves(row=i,column=0)[0].create_text(self.master.master.master.master.selectedchar.secondstats["aura"][0]//2-10,8,text=str(self.master.master.master.master.selectedchar.secondstats["aura"][0]),fill="white",tag="stat")
        i+=2

    def modifychar(self,event=None):
        """ Affiche la fenêtre de modification du personnage """
        for i in self.master.master.grid_slaves(column=3):
            i.grid_forget()
        self.master.master.METH.grid(row=0,column=3)

    def grid(self,**kwargs):
        LabelFrame.grid(self,kwargs)
        self.refresh()




class CharEthMFrame(Frame):
    """ Widget de modification des caractéristiques d'Ether si le personnage est un mage"""

    def __init__(self,master):
        Frame.__init__(self,master)
        self.baselist=["power","mastery","sensitivity"]
        self.New_carac=IntVar()

        Label(self,text="Utiliser l'XP").grid(row=0,column=0,columnspan=2,sticky=W)

        self.statlist=ttk.Combobox(self,values=["Puissance","Maîtrise","Sensibilité"],state="readonly")
        self.statlist.current(0)
        self.add_stat=Entry(self,textvariable=self.New_carac)
        self.Register_new=Button(self,text="Ajouter",command=self.register)

        self.statlist.grid(row=1,column=0)
        self.add_stat.grid(row=1,column=1)
        self.Register_new.grid(row=2,column=0,columnspan=2)

    def register(self,event=None):
        """ On modifie les caractéristiques du personnage, grâce à l'xp, et on recharge le widget qui les affiche """
        self.master.master.master.selectedchar.upstats(self.baselist[self.statlist.current()],self.New_carac.get())
        self.New_carac.set(0)
        self.master.master.master.reload()
        self.master.BNDL.ETH.refresh()
        self.master.BNDL.ABI.refresh()
        # with open("characters","wb") as fichier:
        #     pk.Pickler(fichier).dump(self.master.master.master.master.characlist)




class CharSymbFrame(LabelFrame):

    def __init__(self,master,**kwargs):
        LabelFrame.__init__(self,master,kwargs)
        self.baselist=["parry","armor","ability","mobility","perception","stealth","init","T","ps_T","S","light","mental","luck","charisma","trading","lightning","sensi","aura"]
        i=0
        self.images={}

        for key in self.baselist:
            self.images[key]=ImageTk.PhotoImage(Image.open('Images/symb-'+key+'.png').resize((12,15),Image.ANTIALIAS))
            Label(self,text=" = ",image=self.images[key],compound="left").grid(row=i,column=0)
            i+=1

    def refresh(self):
        i=0
        for key in self.baselist:
            Label(self,text=self.master.master.master.master.selectedchar.secondstats["symb-"+key]).grid(row=i,column=1)
            i+=1

    def grid(self,**kwargs):
        LabelFrame.grid(self,kwargs)
        self.refresh()




class CharBundleFrame(Frame):
    """ Widget d'affichage de toutes les caractéristiques """

    def __init__(self,master):
        Frame.__init__(self,master)

        self.ATK=CharAtkFrame(self,text=" Combat ",relief="groove")
        self.DEF=CharDefFrame(self,text=" Armure ",relief="groove")
        self.PHY=CharPhyFrame(self,text=" Physique ",relief="groove")
        self.ABI=CharAbiFrame(self,text=" Habileté ",relief="groove")
        self.SOC=CharSocFrame(self,text=" Social ",relief="groove")
        self.ETH=CharEthFrame(self,text=" Ether ",relief="groove")
        self.SYM=CharSymbFrame(self,text=" Bignous ",relief="groove")


    def refresh(self):
        for i in self.grid_slaves():
            i.refresh()

    def grid(self,**kwargs):

        for i in self.grid_slaves():
            i.grid_forget()
        self.ATK.grid(row=0,column=0,rowspan=2,padx="4p",sticky="NEW",pady="2p",ipadx="4p",ipady="4p")
        self.DEF.grid(row=0,column=1,padx="4p",sticky="NSEW",pady="2p",ipadx="4p",ipady="4p")
        self.PHY.grid(row=1,column=1,padx="4p",sticky="NSEW",pady="2p",ipadx="4p",ipady="4p")
        if self.master.master.master.selectedchar.mage:
            self.ABI.grid(row=2,column=0,rowspan=2,sticky="NEW",padx="4p",pady="2p",ipadx="4p",ipady="4p")
            self.SOC.grid(row=2,column=1,padx="4p",sticky="NSEW",pady="2p",ipadx="4p",ipady="4p")
            self.ETH.grid(row=3,column=1,padx="4p",sticky="NSEW",pady="2p",ipadx="4p",ipady="4p")
        else:
            self.ABI.grid(row=2,column=0,sticky="NEW",padx="4p",pady="2p",ipadx="4p",ipady="4p")
            self.SOC.grid(row=2,column=1,padx="4p",sticky="NEW",pady="2p",ipadx="4p",ipady="4p")
        self.SYM.grid(row=0,column=2,rowspan=4,padx="4p",sticky="NSEW",pady="2p",ipadx="4p",ipady="4p")
        self.refresh()
        Frame.grid(self, kwargs)



## Partie 5 Utiles
class CharUsefulFrame(Frame):
    """ Fiche personnage résumée """

    def __init__(self,master,**kwargs):
        Frame.__init__(self,master,**kwargs)

        #self.oui = 0
        self.CharFSymF=CharFirstSymbFrame(self)
        self.CharFSymF.grid(row=0,column=0,sticky="we",padx="4p")

        self.CharPercepF=CharPercepFrame(self)
        self.CharPercepF.grid(row=1,column=0,rowspan=2)

        self.CharStealthF=CharStealthFrame(self)
        self.CharStealthF.grid(row=3,column=0,sticky="we")

        self.CharHiddenF=CharHiddenFrame(self)
        self.CharHiddenF.grid(row=4,column=0,sticky="we")

        self.CharUCompF=CharUseCompetFrame(self,text=" Compétences ")
        self.CharUCompF.grid(row=5,column=0,padx="4p",rowspan=2,sticky="nswe")

        Frame(self,width=3,bg="black").grid(row=0,column=3,rowspan=7,padx="4p",pady="4p",sticky="ns")

        self.CharMelF=CharMelFrame(self,text=" Mélée ")
        self.CharMelF.grid(row=0,column=4,sticky="we",padx="4p",ipadx='2p',ipady='2p',rowspan=2)

        self.CharThrF=CharThrFrame(self,text=" Jet ")
        self.CharThrF.grid(row=2,column=4,sticky="we",padx="4p",ipadx='2p',ipady='2p')

        self.CharArmF=CharArmFrame(self,text=" Armure ")
        self.CharArmF.grid(row=3,column=4,sticky="we",padx="4p",ipadx='2p',ipady='2p',rowspan=3)

        self.PercFrame=CharPercFrame(self,text=" Pourcentages ",relief="groove")
        self.PercFrame.grid(row=6,column=4,padx="4p",pady="4p",sticky="we")

        self.bind("<Visibility>",func=self.refresh)


    def refresh(self,event=None):

        self.CharFSymF.refresh()
        self.CharPercepF.refresh()
        self.CharStealthF.refresh()
        self.CharHiddenF.refresh()
        self.CharUCompF.refresh()

        self.CharArmF.refresh()
        self.CharMelF.refresh()
        self.CharThrF.refresh()
        self.PercFrame.refresh()






class CharFirstSymbFrame(Frame):

    def __init__(self,master,**kw):
        Frame.__init__(self,master,**kw)
        self.SymbList=["strength","mobility","init"]
        self.sizelist={"strength":(24,40),"mobility":(30,20),"init":(30,20)}

        self.images={}
        i=0
        for key in self.SymbList:
            self.images[key]=ImageTk.PhotoImage(Image.open('Images/symb-'+key+'.png').resize(self.sizelist[key],Image.ANTIALIAS))
            Label(self,image=self.images[key],compound="left").grid(row=0,column=2*i)
            i+=1

        for i in range(6):
            self.columnconfigure(i,weight=1)


    def refresh(self):
        for i in self.grid_slaves():
            if i.grid_info()["column"]%2==1:
                i.destroy()

        i=0
        for key in self.SymbList:
            if key=="strength":
                Label(self,text=self.master.master.master.selectedchar.secondstats["symb-"+key][0]).grid(row=0,column=2*i+1,sticky="w")
            else:
                Label(self,text=self.master.master.master.selectedchar.secondstats["symb-"+key]).grid(row=0,column=2*i+1,sticky="w")
            i+=1




class CharPercepFrame(Frame):
    """ Widget qui affiche les investissements dans les sens et l'analyse sur la fiche résumé """

    def __init__(self,master,**kw):
        Frame.__init__(self,master,**kw)
        self.perceplist=[["intention","thing-info","bestiary"],["trap","find","tracking"],["ennemies","threat","curse"]]
        self.percep_image=ImageTk.PhotoImage(Image.open('Images/symb-perception.png').resize((12,15),Image.ANTIALIAS))
        Label(self,text="Analyse/Perception ",image=self.percep_image,compound="right").grid(row=0,column=0,columnspan=3)

        i=2
        for key in ["Vue :","Ouïe :","Odorat :"]:
            Label(self,text=key).grid(row=i,column=0,sticky="e")
            i+=1

        ttk.Separator(self,orient="vertical").grid(row=1,column=2,rowspan=4,sticky="ns",padx="4p",pady="2p")

        i=0
        for key in ["Indice : ","Terrain : ","Embuscade : "]:
            Label(self,text=key).grid(row=1,column=2*i+3,sticky="w")
            i+=1

        i=2
        for key in ["Intention : ","Objet-info : ","Bestiaire : "]:
            Label(self,text=key).grid(row=i,column=3,sticky="e")
            i+=1

        i=2
        for key in ["Piège : ","Trouver Objets : ","Pistage : "]:
            Label(self,text=key).grid(row=i,column=5,sticky="e")
            i+=1

        i=2
        for key in ["Adversaires : ","Menace : ","Malédiction : "]:
            Label(self,text=key).grid(row=i,column=7,sticky="e")
            i+=1


    def refresh(self):

        for i in self.grid_slaves():
            info=i.grid_info()
            if info["row"]>=2 and info["column"] in [1,4,6,8]:
                i.destroy()

        i=2
        for key in ["sight","hearing","smell"]:
            Label(self,text=self.master.master.master.selectedchar.thirdstats[key]).grid(row=i,column=1)
            i+=1

        j=0
        for key in ["clue","field","ambush"]:
            i=2
            for stat in self.perceplist[j]:
                Label(self,text=self.master.master.master.selectedchar.thirdstats[key][stat]).grid(row=i,column=2*j+4)
                i+=1

            j+=1





class CharStealthFrame(Frame):
    """ Widget qui affiche l'investissement de la furtivité dans la fiche résumé """

    def __init__(self,master,**kw):
        Frame.__init__(self,master,**kw)
        self.furtiflist=[["ground","moving","assassination"],["shadow","not-moving","identity"],["smell","disguise","nature-field"]]
        self.stealth_image=ImageTk.PhotoImage(Image.open('Images/symb-stealth.png').resize((18,8),Image.ANTIALIAS))

        Label(self,text="Furtivité ",image=self.stealth_image,compound="right").grid(row=0,column=0,columnspan=2)
        i=0
        for key in ["Silence : ","Dissimulation : ","Camouflage : "]:
            Label(self,text=key).grid(row=1,column=3*i,sticky="w")
            i+=1

        i=2
        for key in ["Sol : ","Déplacement : ","Assassinat : "]:
            Label(self,text=key).grid(row=i,column=0,sticky="e")
            i+=1

        i=2
        for key in ["Ombre : ","Immobilité : ","Identité : "]:
            Label(self,text=key).grid(row=i,column=3,sticky="e")
            i+=1

        i=2
        for key in ["Odeur : ","Déguisement : ","Nature/Terrain : "]:
            Label(self,text=key).grid(row=i,column=6,sticky="e")
            i+=1

        for i in range(2):
            self.columnconfigure(3*i+2,weight=1)



    def refresh(self):

        for i in self.grid_slaves():
            info=i.grid_info()
            if info["row"]>=2 and info["column"] in [1,4,7]:
                i.destroy()

        j=0
        for key in ["silence","hiding","camo"]:
            i=2
            for stat in self.furtiflist[j]:
                Label(self,text=self.master.master.master.selectedchar.thirdstats[key][stat]).grid(row=i,column=3*j+1)
                i+=1

            j+=1






class CharPercFrame(LabelFrame):
    """ cadre d'affichage des pourcentages du personnage """

    def __init__(self,master,**kw):
        LabelFrame.__init__(self,master,**kw)
        self.perclist=["Mains nues","Armes légères","Armes moyennes","Armes lourdes","Armes de jet","Bouclier","Résistance physique","Dextérité","Mobilité","Perception","Furtivité","Résistance mentale","Charisme","Commerce","Sorts","Perception magique"]



    def refresh(self):
        """ fonction qui réaffiche les statistiques de pourcentages du personnage """

        for key in self.grid_slaves():
            key.destroy()
        i=0
        j=0
        k=0
        for key in self.master.master.master.selectedchar.percentages.keys():
            if self.master.master.master.selectedchar.percentages[key]!=0:
                Label(self,text=self.perclist[j]+" : "+str(self.master.master.master.selectedchar.percentages[key])+"%").grid(row=i,column=2*k)
                i+=1

                if i==4:
                    k+=1
                    i=0
                if i==0:
                    ttk.Separator(self,orient="vertical").grid(row=0,column=2*k-1,rowspan=4,sticky="ns",pady="2p")
            j+=1




class CharHiddenFrame(Frame):
    """ Widget qui affiche ce qui a été investi dans action dissimulée """

    def __init__(self,master,**kw):
        Frame.__init__(self,master,**kw)

        Label(self,text="Action dissimulée").grid(row=0,column=0)
        i=0
        for key in ["Vol à la tire : ","Embuscade : ","Fuite : "]:
            Label(self,text=key).grid(row=1,column=3*i,sticky="e")
            i+=1

        for i in range(2):
            self.columnconfigure(3*i+2,weight=1)



    def refresh(self):

        for i in self.grid_slaves():
            info=i.grid_info()
            if info["row"]==1 and info["column"] in [1,4,7]:
                i.destroy()

        j=0
        for stat in ["thievery","ambush","escape"]:
            Label(self,text=self.master.master.master.selectedchar.thirdstats["hidden_action"][stat]).grid(row=1,column=3*j+1)
            j+=1




class CharMelFrame(LabelFrame):
    """ Cadre d'affichage des équipements de mélée du personnage """

    def __init__(self,master,**kw):
        LabelFrame.__init__(self,master,**kw)
        # on ouvre l'icône de la maitrise pour pouvoir l'afficher aisément
        self.mastery_image=ImageTk.PhotoImage(Image.open("Images/symb-mastery.png").resize((10,10),Image.ANTIALIAS))

        for i in range(1,9):
            self.grid_columnconfigure(i,weight=1)

    def refresh(self):
        """ Fonction pour rafraîchir les équipements de mélée du personnage """
        Meleelist=["dgt_tr","dgt_ctd","estoc","vit","mastery","quality","solid"]
        Shieldlist=["close","dist","mobi","vit","mastery","quality","solid"]
        for i in self.grid_slaves():
            i.destroy()

        i=1
        # si l'objet est équipé, on met ses caractéristiques, sinon, on met des "..."
        # disjonction de cas si c'est une arme ou un bouclier
        if self.master.master.master.selectedchar.playerequipment["left_melee"]:
            Label(self,text=self.master.master.master.selectedchar.playerequipment["left_melee"].name).grid(row=1,column=1)
            if self.master.master.master.selectedchar.playerequipment["left_melee"].carac["hand"]==2:
                Label(self,text="2 mains").grid(row=0,column=0,rowspan=2)
                if type(self.master.master.master.selectedchar.playerequipment["left_melee"])==pc.MeleeEquip:
                    i=1
                    for key in ["Nom","Dég. Tr.","Dég. Ctd.","Estoc","Vit.","Maîtr.","Qual.","Sol."]:
                        if key=="Vit." and self.master.master.master.selectedchar.playerequipment["left_melee"].carac["hast"]:
                            Label(self,text="Bon. Hast").grid(row=0,column=i)
                        else:
                            Label(self,text=key).grid(row=0,column=i)
                        i+=1
                    i=2
                    for key in Meleelist:
                        if key=="vit" and self.master.master.master.selectedchar.playerequipment["left_melee"].carac["hast"]:
                            Label(self,text=self.master.master.master.selectedchar.playerequipment["left_melee"].carac["hast_bonus"]).grid(row=0,column=i)
                        else:
                            Label(self,text=self.master.master.master.selectedchar.playerequipment["left_melee"].carac[key]).grid(row=1,column=i)
                        i+=1

                elif type(self.master.master.master.selectedchar.playerequipment["left_melee"])==pc.ShieldEquip:
                    i=1
                    for key in ["Nom","Par. CàC","Par. Dist.","Mobi.","Vit.","Maîtr.","Qual.","Sol."]:
                        Label(self,text=key).grid(row=3,column=i)
                        i+=1
                    i=2
                    for key in Shieldlist:
                        Label(self,text=self.master.master.master.selectedchar.playerequipment["left_melee"].carac[key]).grid(row=4,column=i)
                        i+=1

            else:
                Label(self,text="Main gauche").grid(row=0,column=0,rowspan=2)
                if type(self.master.master.master.selectedchar.playerequipment["left_melee"])==pc.MeleeEquip:
                    i=1
                    for key in ["Nom","Dég. Tr.","Dég. Ctd.","Estoc","Vit.","Maîtr.","Qual.","Sol."]:
                        if key=="Vit." and self.master.master.master.selectedchar.playerequipment["left_melee"].carac["hast"]:
                            Label(self,text="Bon. Hast").grid(row=0,column=i)
                        else:
                            Label(self,text=key).grid(row=0,column=i)
                        i+=1
                    i=2
                    for key in Meleelist:
                        if key=="vit" and self.master.master.master.selectedchar.playerequipment["left_melee"].carac["hast"]:
                            Label(self,text=self.master.master.master.selectedchar.playerequipment["left_melee"].carac["hast_bonus"]).grid(row=0,column=i)
                        else:
                            Label(self,text=self.master.master.master.selectedchar.playerequipment["left_melee"].carac[key]).grid(row=1,column=i)
                        i+=1

                elif type(self.master.master.master.selectedchar.playerequipment["left_melee"])==pc.ShieldEquip:
                    i=1
                    for key in ["Nom","Par. CàC","Par. Dist.","Mobi.","Vit.","Maîtr.","Qual.","Sol."]:
                        Label(self,text=key).grid(row=0,column=i)
                        i+=1
                    i=2
                    for key in Shieldlist:
                        Label(self,text=self.master.master.master.selectedchar.playerequipment["left_melee"].carac[key]).grid(row=1,column=i)
                        i+=1

                ttk.Separator(self,orient="horizontal").grid(row=2,column=0,columnspan=10,sticky="we",padx="4p",pady="4p")

                Label(self,text="Main droite").grid(row=3,column=0,rowspan=2)

                if self.master.master.master.selectedchar.playerequipment["right_melee"]:
                    Label(self,text=self.master.master.master.selectedchar.playerequipment["right_melee"].name).grid(row=4,column=1)
                    if type(self.master.master.master.selectedchar.playerequipment["right_melee"])==pc.MeleeEquip:
                        i=1
                        for key in ["Nom","Dég. Tr.","Dég. Ctd.","Estoc","Vit.","Maîtr.","Qual.","Sol."]:
                            if key=="Vit." and self.master.master.master.selectedchar.playerequipment["right_melee"].carac["hast"]:
                               Label(self,text="Bon. Hast").grid(row=3,column=i)
                            else:
                                Label(self,text=key).grid(row=3,column=i)
                            i+=1
                        i=2
                        for key in Meleelist:
                            if key=="vit" and self.master.master.master.selectedchar.playerequipment["right_melee"].carac["hast"]:
                                Label(self,text=self.master.master.master.selectedchar.playerequipment["right_melee"].carac["hast_bonus"]).grid(row=4,column=i)
                            else:
                                Label(self,text=self.master.master.master.selectedchar.playerequipment["right_melee"].carac[key]).grid(row=4,column=i)
                            i+=1

                    elif type(self.master.master.master.selectedchar.playerequipment["right_melee"])==pc.ShieldEquip:
                        i=1
                        for key in ["Nom","Par. CàC","Par. Dist.","Mobi.","Vit.","Maîtr.","Qual.","Sol."]:
                            Label(self,text=key).grid(row=3,column=i)
                            i+=1
                        i=2
                        for key in Shieldlist:
                            Label(self,text=self.master.master.master.selectedchar.playerequipment["right_melee"].carac[key]).grid(row=4,column=i)
                            i+=1

                    Button(self,text="+",image=self.mastery_image,compound="right",command=partial(self.up_mastery,"right",1),takefocus=0).grid(row=3,column=9,padx="4p",sticky="we")
                    Button(self,text="-",image=self.mastery_image,compound="right",command=partial(self.up_mastery,"right",-1),takefocus=0).grid(row=4,column=9,padx="4p",sticky="we")

                else:
                    for i in range(1,9):
                        Label(self,text="...").grid(row=3,column=i)
                        Label(self,text="...").grid(row=4,column=i)

            Button(self,text="+",image=self.mastery_image,compound="right",command=partial(self.up_mastery,"left",1),takefocus=0).grid(row=0,column=9,padx="4p",sticky="we")
            Button(self,text="-",image=self.mastery_image,compound="right",command=partial(self.up_mastery,"left",-1),takefocus=0).grid(row=1,column=9,padx="4p",sticky="we")

        else:
            Label(self,text="Main gauche").grid(row=0,column=0,rowspan=2)
            for i in range(1,9):
                Label(self,text="...").grid(row=1,column=i)
                Label(self,text="...").grid(row=0,column=i)

            ttk.Separator(self,orient="horizontal").grid(row=2,column=0,columnspan=10,sticky="we",padx="4p",pady="4p")

            Label(self,text="Main droite").grid(row=3,column=0,rowspan=2)

            if self.master.master.master.selectedchar.playerequipment["right_melee"]:
                Label(self,text=self.master.master.master.selectedchar.playerequipment["right_melee"].name).grid(row=4,column=1)
                if type(self.master.master.master.selectedchar.playerequipment["right_melee"])==pc.MeleeEquip:
                    i=1
                    for key in ["Nom","Dég. Tr.","Dég. Ctd.","Estoc","Vit.","Maîtr.","Qual.","Sol."]:
                        if key=="Vit." and self.master.master.master.selectedchar.playerequipment["right_melee"].carac["hast"]:
                            Label(self,text="Bon. Hast").grid(row=3,column=i)
                        else:
                            Label(self,text=key).grid(row=3,column=i)
                        i+=1
                    i=2
                    for key in Meleelist:
                        if key=="vit" and self.master.master.master.selectedchar.playerequipment["right_melee"].carac["hast"]:
                            Label(self,text=self.master.master.master.selectedchar.playerequipment["right_melee"].carac["hast_bonus"]).grid(row=4,column=i)
                        else:
                            Label(self,text=self.master.master.master.selectedchar.playerequipment["right_melee"].carac[key]).grid(row=4,column=i)
                        i+=1

                elif type(self.master.master.master.selectedchar.playerequipment["right_melee"])==pc.ShieldEquip:
                    i=1
                    for key in ["Nom","Par. CàC","Par. Dist.","Mobi.","Vit.","Maîtr.","Qual.","Sol."]:
                        Label(self,text=key).grid(row=3,column=i)
                        i+=1
                    i=2
                    for key in Shieldlist:
                        Label(self,text=self.master.master.master.selectedchar.playerequipment["right_melee"].carac[key]).grid(row=4,column=i)
                        i+=1

                Button(self,text="+",image=self.mastery_image,compound="right",command=partial(self.up_mastery,"right",1),takefocus=0).grid(row=3,column=9,padx="4p",sticky="we")
                Button(self,text="-",image=self.mastery_image,compound="right",command=partial(self.up_mastery,"right",-1),takefocus=0).grid(row=4,column=9,padx="4p",sticky="we")



            else:
                for i in range(1,9):
                    Label(self,text="...").grid(row=3,column=i)
                    Label(self,text="...").grid(row=4,column=i)


    def up_mastery(self,where,number):
        self.master.master.master.selectedchar.playerequipment[where+"_melee"].upmastery(number)

        if where=="left":
            item = self.grid_slaves(1,6)
        else:
            item = self.grid_slaves(4, 6)
        item[0]["text"]=str(self.master.master.master.selectedchar.get_weapon(where, "melee").get_stats_aslist(["mastery"])[0])



class CharThrFrame(LabelFrame):
    """ Cadre d'affichage des armes de jet du personnage """

    def __init__(self,master,**kw):
        LabelFrame.__init__(self,master,**kw)
        self.mastery_image=ImageTk.PhotoImage(Image.open("Images/symb-mastery.png").resize((10,10),Image.ANTIALIAS))

        for i in range(1,7):
            self.grid_columnconfigure(i,weight=1)
        self.grid_columnconfigure(8,weight=2)

    def refresh(self):
        """ Fonction pour rafraîchir les armes de jet du personnage """
        Throwlist=["dgt","pa","cord","mastery","solid"]
        for i in self.grid_slaves():
            i.destroy()

        i=1
        # si l'objet est équipé, on met ses caractéristiques, sinon, on met des "..."
        if self.master.master.master.selectedchar.playerequipment["left_throw"]:
            Label(self,text=self.master.master.master.selectedchar.playerequipment["left_throw"].name).grid(row=1,column=1)
            if self.master.master.master.selectedchar.playerequipment["left_throw"].carac["hand"]==2:
                Label(self,text="2 mains").grid(row=0,column=0,rowspan=2)
                i=1
                for key in ["Nom","Dég.","P.-Arm.","Cordes","Maîtr.","Sol."]:
                    if key !="Cordes" or self.master.master.master.selectedchar.playerequipment["left_throw"].carac["cord"]:
                        Label(self,text=key).grid(row=0,column=i)
                        i+=1
                i=2
                for key in Throwlist:
                    if key !="cord":
                        Label(self,text=self.master.master.master.selectedchar.playerequipment["left_throw"].carac[key]).grid(row=1,column=i)
                        i+=1

                    elif self.master.master.master.selectedchar.playerequipment["left_throw"].carac["cord"]:
                        Label(self,text=str(self.master.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][0])+" - "+str(self.master.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1])+"%").grid(row=1,column=i)
                        i+=1

                scopeFrame=Frame(self)
                scopeFrame.grid(row=0,column=7,rowspan=2)
                Label(scopeFrame,text="Préc.").grid(row=1,column=0)
                Label(scopeFrame,text="Vit.").grid(row=2,column=0)
                Label(scopeFrame,text=0).grid(row=0,column=1)
                ttk.Separator(scopeFrame,orient="vertical").grid(row=1,column=1,rowspan=2,sticky="ns")

                for i in range(len(self.master.master.master.selectedchar.playerequipment["left_throw"].carac["scope"])):
                    Label(scopeFrame,text=self.master.master.master.selectedchar.playerequipment["left_throw"].carac["scope"][i][0]).grid(row=0,column=3+2*i)
                    ttk.Separator(scopeFrame,orient="vertical").grid(row=1,column=3+2*i,rowspan=2,sticky="NS")
                    Label(scopeFrame,text=self.master.master.master.selectedchar.playerequipment["left_throw"].carac["scope"][i][2]).grid(row=1,column=2+2*i)
                    Label(scopeFrame,text=self.master.master.master.selectedchar.playerequipment["left_throw"].carac["scope"][i][1]).grid(row=2,column=2+2*i)



            else:
                Label(self,text="Main gauche").grid(row=0,column=0,rowspan=2)
                i=1
                for key in ["Nom","Dég.","P.-Arm.","Cordes","Maîtr.","Sol."]:
                    if key !="Cordes" or self.master.master.master.selectedchar.playerequipment["left_throw"].carac["cord"]:
                        Label(self,text=key).grid(row=0,column=i)
                        i+=1
                i=2
                for key in Throwlist:
                    if key !="cord":
                        Label(self,text=self.master.master.master.selectedchar.playerequipment["left_throw"].carac[key]).grid(row=1,column=i)
                        i+=1

                    elif self.master.master.master.selectedchar.playerequipment["left_throw"].carac["cord"]:
                        Label(self,text=str(self.master.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][0])+" - "+str(self.master.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1])+"%").grid(row=1,column=i)
                        i+=1

                scopeFrame=Frame(self)
                scopeFrame.grid(row=0,column=7,rowspan=2)
                Label(scopeFrame,text="Vit.").grid(row=1,column=0)
                Label(scopeFrame,text="Préc.").grid(row=2,column=0)
                Label(scopeFrame,text=0).grid(row=0,column=1)
                ttk.Separator(scopeFrame,orient="vertical").grid(row=1,column=1,rowspan=2,sticky="ns")

                for i in range(len(self.master.master.master.selectedchar.playerequipment["left_throw"].carac["scope"])):
                    Label(scopeFrame,text=self.master.master.master.selectedchar.playerequipment["left_throw"].carac["scope"][i][0]).grid(row=0,column=3+2*i)
                    ttk.Separator(scopeFrame,orient="vertical").grid(row=1,column=3+2*i,rowspan=2,sticky="NS")
                    Label(scopeFrame,text=self.master.master.master.selectedchar.playerequipment["left_throw"].carac["scope"][i][1]).grid(row=1,column=2+2*i)
                    Label(scopeFrame,text=self.master.master.master.selectedchar.playerequipment["left_throw"].carac["scope"][i][2]).grid(row=2,column=2+2*i)



                ttk.Separator(self,orient="horizontal").grid(row=2,column=0,columnspan=9,sticky="we",padx="4p",pady="4p")

                Label(self,text="Main droite").grid(row=3,column=0,rowspan=2)

                if self.master.master.master.selectedchar.playerequipment["right_throw"]:
                    Label(self,text=self.master.master.master.selectedchar.playerequipment["right_throw"].name).grid(row=4,column=1)
                    i=1
                    for key in ["Nom","Dég.","P.-Arm.","Cordes","Maîtr.","Sol."]:
                        if key !="Cordes" or self.master.master.master.selectedchar.playerequipment["right_throw"].carac["cord"]:
                            Label(self,text=key).grid(row=3,column=i)
                            i+=1
                    i=2
                    for key in Throwlist:
                        if key !="cord":
                            Label(self,text=self.master.master.master.selectedchar.playerequipment["right_throw"].carac[key]).grid(row=4,column=i)
                            i+=1
                        elif self.master.master.master.selectedchar.playerequipment["right_throw"].carac["cord"]:
                            Label(self,text=str(self.master.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][0])+" - "+str(self.master.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1])+"%").grid(row=4,column=i)
                            i+=1

                    scopeFrame=Frame(self)
                    scopeFrame.grid(row=3,column=7,rowspan=2)
                    Label(scopeFrame,text="Vit.").grid(row=1,column=0)
                    Label(scopeFrame,text="Préc.").grid(row=2,column=0)
                    Label(scopeFrame,text=0).grid(row=0,column=1)
                    ttk.Separator(scopeFrame,orient="vertical").grid(row=1,column=1,rowspan=2,sticky="ns")

                    for i in range(len(self.master.master.master.selectedchar.playerequipment["right_throw"].carac["scope"])):
                        Label(scopeFrame,text=self.master.master.master.selectedchar.playerequipment["right_throw"].carac["scope"][i][0]).grid(row=0,column=3+2*i)
                        ttk.Separator(scopeFrame,orient="vertical").grid(row=1,column=3+2*i,rowspan=2,sticky="NS")
                        Label(scopeFrame,text=self.master.master.master.selectedchar.playerequipment["right_throw"].carac["scope"][i][1]).grid(row=1,column=2+2*i)
                        Label(scopeFrame,text=self.master.master.master.selectedchar.playerequipment["right_throw"].carac["scope"][i][2]).grid(row=2,column=2+2*i)


                    Button(self,text="+",image=self.mastery_image,compound="right",command=partial(self.up_mastery,"right",1)).grid(sticky="we",row=3,column=8,padx="4p")
                    Button(self,text="-",image=self.mastery_image,compound="right",command=partial(self.up_mastery,"right",-1)).grid(sticky="we",row=4,column=8,padx="4p")

                else:
                    for i in range(1,8):
                        Label(self,text="...").grid(row=3,column=i)
                        Label(self,text="...").grid(row=4,column=i)

            Button(self,text="+",image=self.mastery_image,compound="right",command=partial(self.up_mastery,"left",1)).grid(sticky="we",row=0,column=8,padx="4p")
            Button(self,text="-",image=self.mastery_image,compound="right",command=partial(self.up_mastery,"left",-1)).grid(sticky="we",row=1,column=8,padx="4p")


        else:
            Label(self,text="Main gauche").grid(row=0,column=0,rowspan=2)
            for i in range(1,8):
                Label(self,text="...").grid(row=1,column=i)
                Label(self,text="...").grid(row=0,column=i)

            ttk.Separator(self,orient="horizontal").grid(row=2,column=0,columnspan=9,sticky="we",padx="4p",pady="4p")

            Label(self,text="Main droite").grid(row=3,column=0,rowspan=2)

            if self.master.master.master.selectedchar.playerequipment["right_throw"]:
                Label(self,text=self.master.master.master.selectedchar.playerequipment["right_throw"].name).grid(row=4,column=1)
                i=1
                for key in ["Nom","Dég.","P.-Arm.","Cordes","Maîtr.","Sol."]:
                    if key !="Cordes" or self.master.master.master.selectedchar.playerequipment["right_throw"].carac["cord"]:
                        Label(self,text=key).grid(row=3,column=i)
                        i+=1

                i=2
                for key in Throwlist:
                    if key !="cord":
                        Label(self,text=self.master.master.master.selectedchar.playerequipment["right_throw"].carac[key]).grid(row=4,column=i)
                        i+=1

                    elif self.master.master.master.selectedchar.playerequipment["right_throw"].carac["cord"]:
                        Label(self,text=str(self.master.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][0])+" - "+str(self.master.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1])+"%").grid(row=4,column=i)
                        i+=1


                scopeFrame=Frame(self)
                scopeFrame.grid(row=3,column=7,rowspan=2)
                Label(scopeFrame,text="Vit.").grid(row=1,column=0)
                Label(scopeFrame,text="Préc.").grid(row=2,column=0)
                Label(scopeFrame,text=0).grid(row=0,column=1)
                ttk.Separator(scopeFrame,orient="vertical").grid(row=1,column=1,rowspan=2,sticky="ns")

                for i in range(len(self.master.master.master.selectedchar.playerequipment["right_throw"].carac["scope"])):
                    Label(scopeFrame,text=self.master.master.master.selectedchar.playerequipment["right_throw"].carac["scope"][i][0]).grid(row=0,column=3+2*i)
                    ttk.Separator(scopeFrame,orient="vertical").grid(row=1,column=3+2*i,rowspan=2,sticky="NS")
                    Label(scopeFrame,text=self.master.master.master.selectedchar.playerequipment["right_throw"].carac["scope"][i][1]).grid(row=1,column=2+2*i)
                    Label(scopeFrame,text=self.master.master.master.selectedchar.playerequipment["right_throw"].carac["scope"][i][2]).grid(row=2,column=2+2*i)

                Button(self,text="+",image=self.mastery_image,compound="right",command=partial(self.up_mastery,"right",1)).grid(sticky="we",row=3,column=8,padx="4p")
                Button(self,text="-",image=self.mastery_image,compound="right",command=partial(self.up_mastery,"right",-1)).grid(sticky="we",row=4,column=8,padx="4p")

            else:
                for i in range(1,8):
                    Label(self,text="...").grid(row=3,column=i)
                    Label(self,text="...").grid(row=4,column=i)

    def up_mastery(self,where,number):
        self.master.master.master.selectedchar.get_weapon(where,"throw").upmastery(number)

        if self.master.master.master.selectedchar.get_weapon(where,"throw").get_stats_aslist(["type"])[0]=="Tir":
            col=5
        else:
            col=4

        if where=="left":
            item = self.grid_slaves(1,col)
        else:
            item = self.grid_slaves(4, col)
        item[0]["text"]=str(self.master.master.master.selectedchar.get_weapon(where, "throw").get_stats_aslist(["mastery"])[0])


class CharArmFrame(LabelFrame):

    def __init__(self, master, **kw):
        LabelFrame.__init__(self, master, **kw)

        self.threshold_types=["Arm. Légère","Arm. Moyenne","Arm. Lourde"]
        self.Threshold_View=ttk.Treeview(self,height=3)
        self.Threshold_View.grid(row=0,column=0,sticky="we",padx="4p",pady="4p")
        
        self.Threshold_View["columns"]=("0","1","2")
        self.Threshold_View.column("#0",width=150,anchor="c")
        self.Threshold_View.column("0",width=120,anchor="c")
        self.Threshold_View.column("1",width=120,anchor="c")
        self.Threshold_View.column("2",width=120,anchor="c")

        self.Threshold_View.heading("0",text="Val. d'Arm.")
        self.Threshold_View.heading("1",text="Vit.")
        self.Threshold_View.heading("2",text="Mobi.")

        for key in self.threshold_types:
            self.Threshold_View.insert("","end",key,text=key)

        ttk.Separator(self,orient="horizontal").grid(row=1,column=0,columnspan=8,sticky="we",padx="4p",pady="4p")

        self.armor_image = ImageTk.PhotoImage(Image.open("Images/symb-armor.png").resize((12, 20), Image.ANTIALIAS))
        self.armor_attr = ["Nom","Prot.","Amort.","Mobi.","Vit.","Sol."]

        self.Armorlist = ["Heaume", "Spallières", "Brassards", "Avant-bras", "Plastron", "Jointures", "Tassette",
                          "Cuissots", "Grèves", "Solerets"]

        self.Armor_View=ttk.Treeview(self,height=len(self.Armorlist))
        self.Armor_View.grid(row=2,column=0,sticky="we",padx="4p",pady="4p")

        self.Armor_View["columns"]=("0","1","2","3","4","5","6")
        self.Armor_View.column("#0", width=100)

        i=0
        for key in self.armor_attr:
            self.Armor_View.heading(str(i),text=key)
            if i==0:
                self.Armor_View.column(str(i), width=100,anchor="c")
            else:
                self.Armor_View.column(str(i), width=50,anchor="c")
            i+=1

        self.Armor_View.heading("6",image=self.armor_image)
        self.Armor_View.column("6",width=30,anchor="e")

        for key in self.Armorlist:
            self.Armor_View.insert("","end",key,text=key)

    def refresh(self):
        palier = np.array([[[-10, -4, -8], [-8, -8, -10], [-4, -20, -12]], [[-8, -2, -6], [-4, -4, -6], [-2, -10, -10]],
                           [[-6, 0, -4], [-3, -4, -6], [-1, -8, -8]], [[-4, 0, -2], [-1, -4, -4], [0, -6, -6]],
                           [[-2, 0, 0], [0, -2, -2], [0, -4, -4]], [[0, 2, 0], [0, 0, -1], [0, -2, -2]],
                           [[0, 4, 0], [0, 2, -1], [2, 0, -2]], [[2, 6, 2], [4, 2, 1], [6, 0, 0]],
                           [[4, 8, 4], [6, 3, 2], [8, 0, 0]]])
        armor_level = self.master.master.master.selectedchar.get_armor_level()
        self.Threshold_View.heading("#0",text="Palier d'armure "+str(armor_level))
        i=0
        for item in self.Threshold_View.get_children():
            for j in range(3):
                self.Threshold_View.set(item,column=str(j),value=("+"*int(palier[armor_level,i,j]>0))+str(palier[armor_level,i,j]))
            i+=1

        for item in self.Armor_View.get_children():
            self.Armor_View.set(item,"6",self.master.master.master.selectedchar.get_invested_armor(item))
            linked_equip=self.master.master.master.selectedchar.get_current_armor(item)
            if linked_equip:
                valuelist=linked_equip.get_stats_aslist(["name","prot", "amort", "mobi", "vit", "solid"])
                for i in range(6):
                    self.Armor_View.set(item,str(i),value=valuelist[i])

            else:

                for i in range(6):
                    self.Armor_View.set(item,str(i),value="...")



class CharUseCompetFrame(LabelFrame):

    def __init__(self,master,**kw):
        LabelFrame.__init__(self,master,**kw)


    def refresh(self):
        for i in self.grid_slaves():
            i.destroy()

        i=0
        for compet in self.master.master.master.selectedchar.competences:
            Message(self,text=compet.name+" : "+compet.effect,width=500).grid(row=i,column=0)
            i+=1


## Partie 4 Inventaire

class CharIFrame(Frame):
    """Inventaire d'un personnage"""

    def __init__(self,master):
        Frame.__init__(self,master)
        self.Objlist=[]
        self.Meleelist=[]
        self.Throwlist=[]
        self.Shieldlist=[]
        self.Armorlist=[]
        self.id=None
        self.selected_item=None

        self.ObjCLabel=Label(self,text="Créer un objet")
        self.Import=Button(self,text="Importer",command=self.import_obj)
        self.ObjCF=ObjCreatorFrame(self)

        # tableaux d'affichage des objets --> _view
        # rester sur un objet déclenche l'affichage d'un popup d'information sur l'objet
        # un clic gauche sur une ligne d'objet permet de l'équiper/retirer/supprimer/changer son nombre

        self.Obj_view=ttk.Treeview(self,height=4)
        self.Obj_view["columns"]=("0")
        self.Obj_view.heading("#0",text="Nom")
        self.Obj_view.heading("0",text="Nombre")
        self.Obj_view.column("#0",width=100)
        self.Obj_view.column("0",anchor="c",width=60)
        self.Obj_pop=ObjPopup(self.Obj_view)
        self.Obj_firstindex=1
        self.Obj_view.bind("<Motion>",func=self.obj_schedule)
        self.Obj_view.bind("<Leave>",func=self.unschedule)
        self.Obj_view.bind("<Button-1>",func=self.obj_options)

        self.Melee_view=ttk.Treeview(self,height=4)
        self.Melee_view["columns"]=("0","1","2")
        self.Melee_view.heading("#0",text="Nom")
        self.Melee_view.heading("0",text="Type")
        self.Melee_view.heading("1",text="Taille")
        self.Melee_view.heading("2",text="Nombre")
        self.Melee_view.column("#0",width=100)
        self.Melee_view.column("0",width=100,anchor="c")
        self.Melee_view.column("1",width=60,anchor="c")
        self.Melee_view.column("2",anchor="c",width=60)
        self.Melee_pop=MeleePopup(self.Melee_view)
        self.Melee_firstindex=1
        self.Melee_view.bind("<Motion>",func=self.melee_schedule)
        self.Melee_view.bind("<Leave>",func=self.unschedule)
        self.Melee_view.bind("<Button-1>",func=self.melee_options)

        self.Throw_view=ttk.Treeview(self,height=4)
        self.Throw_view["columns"]=("0","1")
        self.Throw_view.heading("#0",text="Nom")
        self.Throw_view.heading("0",text="Taille")
        self.Throw_view.heading("1",text="Nombre")
        self.Throw_view.column("#0",width=100)
        self.Throw_view.column("0",anchor="c",width=60)
        self.Throw_view.column("1",anchor="c",width=60)
        self.Throw_pop=ThrowPopup(self.Throw_view)
        self.Throw_firstindex=1
        self.Throw_view.bind("<Motion>",func=self.throw_schedule)
        self.Throw_view.bind("<Leave>",func=self.unschedule)
        self.Throw_view.bind("<Button-1>",func=self.throw_options)

        self.Shield_view=ttk.Treeview(self,height=4)
        self.Shield_view["columns"]=("0","1")
        self.Shield_view.heading("#0",text="Nom")
        self.Shield_view.heading("0",text="Taille")
        self.Shield_view.heading("1",text="Nombre")
        self.Shield_view.column("#0",width=100)
        self.Shield_view.column("0",anchor="c",width=60)
        self.Shield_view.column("1",anchor="c",width=60)
        self.Shield_pop=ShieldPopup(self.Shield_view)
        self.Shield_firstindex=1
        self.Shield_view.bind("<Motion>",func=self.shield_schedule)
        self.Shield_view.bind("<Leave>",func=self.unschedule)
        self.Shield_view.bind("<Button-1>",func=self.shield_options)

        self.Armor_view=ttk.Treeview(self,height=4)
        self.Armor_view["columns"]=("0","1")
        self.Armor_view.heading("#0",text="Nom")
        self.Armor_view.heading("0",text="Position")
        self.Armor_view.heading("1",text="Nombre")
        self.Armor_view.column("#0",width=100)
        self.Armor_view.column("0",width=100,anchor="c")
        self.Armor_view.column("1",anchor="c",width=60)
        self.Armor_pop=ArmorPopup(self.Armor_view)
        self.Armor_firstindex=1
        self.Armor_view.bind("<Motion>",func=self.armor_schedule)
        self.Armor_view.bind("<Leave>",func=self.unschedule)
        self.Armor_view.bind("<Button-1>",func=self.armor_options)

        # boutons pour équiper les objets, gauche/droite pour les armes; boutons pour changer les nombres/supprimer, etc
        self.Left_Cord=Button(self,text="Corder (gauche)",state="disabled",command=partial(self.equip_cord,"left"))
        self.Right_Cord=Button(self,text="Corder (droite)",state="disabled",command=partial(self.equip_cord,"right"))
        self.Left_Melee=Button(self,text="Equiper (gauche)",state="disabled",command=partial(self.equip_item,"left"))
        self.Right_Melee=Button(self,text="Equiper (droite)",state="disabled",command=partial(self.equip_item,"right"))
        self.Left_Throw=Button(self,text="Equiper (gauche)",state="disabled",command=partial(self.equip_item,"left"))
        self.Right_Throw=Button(self,text="Equiper (droite)",state="disabled",command=partial(self.equip_item,"right"))
        self.Left_Shield=Button(self,text="Equiper (gauche)",state="disabled",command=partial(self.equip_item,"left"))
        self.Right_Shield=Button(self,text="Equiper (droite)",state="disabled",command=partial(self.equip_item,"right"))
        self.Armor_Equip=Button(self,text="Equiper",state="disabled",command=self.equip_item)
        self.Obj_suppr=Button(self,text="Supprimer",state="disabled",command=self.suppr_obj)
        self.Obj_add=Button(self,text="+",state="disabled",command=partial(self.change_number,1))
        self.Obj_remove=Button(self,text="-",state="disabled",command=partial(self.change_number,-1))
        self.Obj_transfer=Button(self,text="Exporter",state="disabled",command=self.export_obj)
        self.Equip_remove=Button(self,text="Retirer",state="disabled",command=self.unequip_item)
        self.Solid_add=Button(self,text="+ Sol.",state="disabled",command=partial(self.change_solid,1))
        self.Solid_remove=Button(self,text="- Sol.",state="disabled",command=partial(self.change_solid,-1))


        self.Obj_view.grid(row=0,column=0,padx="4p",pady="4p",columnspan=3,rowspan=2,sticky="we")
        self.Melee_view.grid(row=2,column=0,padx="4p",pady="4p",rowspan=2,columnspan=3,sticky="we")
        self.Throw_view.grid(row=4,column=0,padx="4p",pady="4p",columnspan=3,rowspan=2,sticky="we")
        self.Shield_view.grid(row=6,column=0,padx="4p",pady="4p",rowspan=2,columnspan=3,sticky="we")
        self.Armor_view.grid(row=8,column=0,padx="4p",pady="4p",columnspan=3,sticky="we")

        self.Left_Cord.grid(row=0,column=3,columnspan=2,padx="2p")
        self.Right_Cord.grid(row=1,column=3,columnspan=2,padx="2p")
        self.Left_Melee.grid(row=2,column=3,columnspan=2,padx="2p")
        self.Right_Melee.grid(row=3,column=3,columnspan=2,padx="2p")
        self.Left_Throw.grid(row=4,column=3,columnspan=2,padx="2p")
        self.Right_Throw.grid(row=5,column=3,columnspan=2,padx="2p")
        self.Left_Shield.grid(row=6,column=3,columnspan=2,padx="2p")
        self.Right_Shield.grid(row=7,column=3,columnspan=2,padx="2p")
        self.Armor_Equip.grid(row=8,column=3,columnspan=2,padx="2p")
        self.Obj_suppr.grid(row=9,column=2,rowspan=2)
        self.Obj_add.grid(row=9,column=1,sticky="w")
        self.Obj_remove.grid(row=9,column=0,sticky="e")
        self.Obj_transfer.grid(row=10,column=0,columnspan=2)
        self.Equip_remove.grid(row=9,column=3,columnspan=2)
        self.Solid_add.grid(row=10,column=3)
        self.Solid_remove.grid(row=10,column=4)

        ttk.Separator(self,orient="vertical").grid(row=0,column=5,rowspan=11,sticky="ns",pady="2p")

        self.ObjCLabel.grid(row=0,column=6,sticky="w",padx="4p")
        self.Import.grid(row=0,column=7,sticky="e",padx="4p")
        self.ObjCF.grid(row=1,column=6,rowspan=10,columnspan=2,sticky="n")

        self.bind("<Visibility>",func=self.refresh)

    def refresh(self,event=None):
        """ fonction qui rafraîchit l'inventaire """
        # self.master.master.selectedchar.inventory={}
        self.Objlist=[]
        self.Meleelist=[]
        self.Throwlist=[]
        self.Shieldlist=[]
        self.Armorlist=[]

        # on supprime tout l'affichage dans chaque tableau
        for item in self.Obj_view.get_children():
            self.Obj_view.delete(item)

        for item in self.Melee_view.get_children():
            self.Melee_view.delete(item)

        for item in self.Throw_view.get_children():
            self.Throw_view.delete(item)

        for item in self.Shield_view.get_children():
            self.Shield_view.delete(item)

        for item in self.Armor_view.get_children():
            self.Armor_view.delete(item)

        # on reprend la liste complète des objets dans l'inventaire et on les trie par type, puis on les affiche
        for i in self.master.master.selectedchar.inventory.keys():
            if type(i)==pc.Obj or type(i)==pc.Cord:
                self.Obj_view.insert("","end",text=i.name,values=[self.master.master.selectedchar.inventory[i]])
                self.Objlist.append(i)

            elif type(i)==pc.MeleeEquip:
                self.Melee_view.insert("","end",text=i.name,values=[i.carac["weight"],str(i.carac["hand"])+" Main(s)",self.master.master.selectedchar.inventory[i]])
                self.Meleelist.append(i)

            elif type(i)==pc.ThrowEquip:
                self.Throw_view.insert("","end",text=i.name,values=[str(i.carac["hand"])+" Main(s)",self.master.master.selectedchar.inventory[i]])
                self.Throwlist.append(i)

            elif type(i)==pc.ShieldEquip:
                self.Shield_view.insert("","end",text=i.name,values=[str(i.carac["hand"])+" Main(s)",self.master.master.selectedchar.inventory[i]])
                self.Shieldlist.append(i)

            elif type(i)==pc.ArmorEquip:
                self.Armor_view.insert("","end",text=i.name,values=[i.location,self.master.master.selectedchar.inventory[i]])
                self.Armorlist.append(i)


        # si des objets sont affichés dans les tableaux, on regarde quel est l'indice le plus bas donné aux objets
        if self.Obj_view.get_children():
            self.Obj_firstindex=int(self.Obj_view.get_children()[0][1:],base=16)

        if self.Melee_view.get_children():
            self.Melee_firstindex=int(self.Melee_view.get_children()[0][1:],base=16)

        if self.Throw_view.get_children():
            self.Throw_firstindex=int(self.Throw_view.get_children()[0][1:],base=16)

        if self.Shield_view.get_children():
            self.Shield_firstindex=int(self.Shield_view.get_children()[0][1:],base=16)

        if self.Armor_view.get_children():
            self.Armor_firstindex=int(self.Armor_view.get_children()[0][1:],base=16)


    # les popups n'apparaissent que si la souris ne bouge pas
    def obj_schedule(self,event=None):
        """ Prépare à l'affichage du popup pour l'objet """
        self.unschedule()
        if self.Obj_view.identify_row(event.y):
            self.id=self.after("500",self.Obj_pop.showinfo,self.Objlist[int(self.Obj_view.identify_row(event.y)[1:],base=16)-self.Obj_firstindex],event)


    def melee_schedule(self,event=None):
        """ Prépare à l'affichage du popup pour l'arme de mélée """
        self.unschedule()
        if self.Melee_view.identify_row(event.y):
            self.id=self.after("500",self.Melee_pop.showinfo,self.Meleelist[int(self.Melee_view.identify_row(event.y)[1:],base=16)-self.Melee_firstindex],event)


    def throw_schedule(self,event=None):
        """ Prépare à l'affichage du popup pour l'arme de jet """
        self.unschedule()
        if self.Throw_view.identify_row(event.y):
            self.id=self.after("500",self.Throw_pop.showinfo,self.Throwlist[int(self.Throw_view.identify_row(event.y)[1:],base=16)-self.Throw_firstindex],event)


    def shield_schedule(self,event=None):
        """ Prépare à l'affichage du popup pour le bouclier """
        self.unschedule()
        if self.Shield_view.identify_row(event.y):
            self.id=self.after("500",self.Shield_pop.showinfo,self.Shieldlist[int(self.Shield_view.identify_row(event.y)[1:],base=16)-self.Shield_firstindex],event)


    def armor_schedule(self,event=None):
        """ Prépare à l'affichage du popup pour l'armure """
        self.unschedule()
        if self.Armor_view.identify_row(event.y):
            self.id=self.after("500",self.Armor_pop.showinfo,self.Armorlist[int(self.Armor_view.identify_row(event.y)[1:],base=16)-self.Armor_firstindex],event)


    def unschedule(self,event=None):
        """ Arrête l'attente pour afficher le popup, et efface le popup s'il est présent """
        if self.id:
            self.after_cancel(self.id)
            self.id=None
        self.Obj_pop.hideinfo()
        self.Melee_pop.hideinfo()
        self.Throw_pop.hideinfo()
        self.Shield_pop.hideinfo()
        self.Armor_pop.hideinfo()


    def unselect_previous(self):
        """ Désélectionne l'item précédent """

        # on désactive tous les boutons
        if self.selected_item:
            self.Obj_suppr["state"]="disabled"
            self.Obj_add["state"]="disabled"
            self.Obj_remove["state"]="disabled"
            self.Obj_transfer["state"]="disabled"
            self.Equip_remove["state"]="disabled"

            self.Solid_add["state"]="disabled"
            self.Solid_remove["state"]="disabled"


            if type(self.selected_item)==pc.MeleeEquip:
                self.Left_Melee["state"]="disabled"
                self.Right_Melee["state"]="disabled"

            elif type(self.selected_item)==pc.ThrowEquip:
                self.Left_Throw["state"]="disabled"
                self.Right_Throw["state"]="disabled"

            elif type(self.selected_item)==pc.ShieldEquip:
                self.Left_Shield["state"]="disabled"
                self.Right_Shield["state"]="disabled"

            elif type(self.selected_item)==pc.ArmorEquip:
                self.Armor_Equip["state"]="disabled"

            elif type(self.selected_item)==pc.Cord:
                self.Left_Cord["state"]="disabled"
                self.Right_Cord["state"]="disabled"

            self.selected_item=None


    def obj_options(self,event=None):
        """ fonction qui affiche les boutons adéquats à l'objet sélectionné """

        self.unselect_previous()

        if self.Obj_view.identify_row(event.y):
            self.selected_item=self.Objlist[int(self.Obj_view.identify_row(event.y)[1:],base=16)-self.Obj_firstindex]
            self.Obj_suppr["state"]="normal"
            self.Obj_transfer["state"]="normal"

            if self.selected_item.is_stackable:
                self.Obj_add["state"]="normal"
                self.Obj_remove["state"]="normal"

                if not self.master.master.selectedchar.inventory[self.selected_item]:
                    self.Obj_remove["state"]="disabled"

            else:
                if self.master.master.selectedchar.inventory[self.selected_item]:
                    self.Obj_remove["state"]="normal"
                else:
                    self.Obj_add["state"]="normal"

            # si l'objet est une corde, on dévérouille les boutons de cordage si les conditions les permettent
            if type(self.selected_item)==pc.Cord:
                # on commence par vérifier si l'arme de jet gauche existe, puis si elle nécessite une corde
                if self.master.master.selectedchar.playerequipment["left_throw"] and self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"]:
                    # si l'arme est à 2 mains, on vérifier juste qu'on a assez de cordes pour en "corder" une de plus
                    if self.master.master.selectedchar.playerequipment["left_throw"].carac["hand"]==2:
                        if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][0] or self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]!=self.selected_item.perc:
                            self.Left_Cord["state"]="normal"
                            self.Right_Cord["state"]="normal"
                    # sinon, on vérifie si la deuxième arme existe, puis si elle a besoin d'une corde
                    elif self.master.master.selectedchar.playerequipment["right_throw"] and self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"]:

                        if (self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]==self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]==self.selected_item.perc) or (self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]==self.selected_item.perc and self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]==0) or (self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]==self.selected_item.perc and self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]==0) or (self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]==self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]==0):
                            if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerquipment["left_throw"].carac["cord"][0]+self.master.master.selectedchar.playerquipment["right_throw"].carac["cord"][0]:
                                self.Left_Cord["state"]="normal"
                                self.Right_Cord["state"]="normal"

                        elif (self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]==self.selected_item.perc and self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]!=self.selected_item.perc):
                            if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerquipment["left_throw"].carac["cord"][0]:
                                self.Left_Cord["state"]="normal"
                                self.Right_Cord["state"]="normal"

                        elif self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]==self.selected_item.perc and self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]!=self.selected_item.perc:
                            if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerquipment["right_throw"].carac["cord"][0]:
                                self.Left_Cord["state"]="normal"
                                self.Right_Cord["state"]="normal"

                        else:
                            self.Left_Cord["state"]="normal"
                            self.Right_Cord["state"]="normal"

                    else:
                        if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][0] or self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]!=self.selected_item.perc:
                            self.Left_Cord["state"]="normal"


                # sinon, on regarde pour la droite, qui est alors forcément à une main si elle existe
                elif self.master.master.selectedchar.playerequipment["right_throw"] and self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"]:
                    # si on a assez de corde pour corder à droite, on dévérouille le bouton
                    if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][0] or self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]!=self.selected_item.perc:
                        self.Right_Cord["state"]="normal"


    def melee_options(self,event=None):
        """ fonction qui affiche les boutons adéquats à l'objet sélectionné """

        self.unselect_previous()

        if self.Melee_view.identify_row(event.y):
            self.selected_item=self.Meleelist[int(self.Melee_view.identify_row(event.y)[1:],base=16)-self.Melee_firstindex]
            self.Left_Melee["state"]="normal"
            self.Right_Melee["state"]="normal"

            self.Obj_suppr["state"]="normal"
            self.Obj_transfer["state"]="normal"

            self.Solid_add["state"]="normal"
            self.Solid_remove["state"]="normal"

            if self.selected_item.is_stackable:
                self.Obj_add["state"]="normal"
                self.Obj_remove["state"]="normal"

                if not self.master.master.selectedchar.inventory[self.selected_item]:
                    self.Obj_remove["state"]="disabled"

            else:
                if self.master.master.selectedchar.inventory[self.selected_item]:
                    self.Obj_remove["state"]="normal"
                else:
                    self.Obj_add["state"]="normal"

            if self.selected_item in self.master.master.selectedchar.playerequipment.values():
                self.Equip_remove["state"]="normal"


    def throw_options(self,event=None):
        """ fonction qui affiche les boutons adéquats à l'objet sélectionné """

        self.unselect_previous()

        if self.Throw_view.identify_row(event.y):
            self.selected_item=self.Throwlist[int(self.Throw_view.identify_row(event.y)[1:],base=16)-self.Throw_firstindex]
            self.Left_Throw["state"]="normal"
            self.Right_Throw["state"]="normal"
            self.Obj_suppr["state"]="normal"
            self.Obj_transfer["state"]="normal"

            self.Solid_add["state"]="normal"
            self.Solid_remove["state"]="normal"

            if self.selected_item.is_stackable:
                self.Obj_add["state"]="normal"
                self.Obj_remove["state"]="normal"

                if not self.master.master.selectedchar.inventory[self.selected_item]:
                    self.Obj_remove["state"]="disabled"

            else:
                if self.master.master.selectedchar.inventory[self.selected_item]:
                    self.Obj_remove["state"]="normal"
                else:
                    self.Obj_add["state"]="normal"

            if self.selected_item in self.master.master.selectedchar.playerequipment.values():
                self.Equip_remove["state"]="normal"




    def shield_options(self,event=None):
        """ fonction qui affiche les boutons adéquats à l'objet sélectionné """

        self.unselect_previous()

        if self.Shield_view.identify_row(event.y):
            self.selected_item=self.Shieldlist[int(self.Shield_view.identify_row(event.y)[1:],base=16)-self.Shield_firstindex]
            self.Left_Shield["state"]="normal"
            self.Right_Shield["state"]="normal"
            self.Obj_suppr["state"]="normal"
            self.Obj_transfer["state"]="normal"

            self.Solid_add["state"]="normal"
            self.Solid_remove["state"]="normal"

            if self.selected_item.is_stackable:
                self.Obj_add["state"]="normal"
                self.Obj_remove["state"]="normal"

                if not self.master.master.selectedchar.inventory[self.selected_item]:
                    self.Obj_remove["state"]="disabled"

            else:
                if self.master.master.selectedchar.inventory[self.selected_item]:
                    self.Obj_remove["state"]="normal"
                else:
                    self.Obj_add["state"]="normal"

            if self.selected_item in self.master.master.selectedchar.playerequipment.values():
                self.Equip_remove["state"]="normal"


    def armor_options(self,event=None):
        """ fonction qui affiche les boutons adéquats à l'objet sélectionné """

        self.unselect_previous()

        if self.Armor_view.identify_row(event.y):
            self.selected_item=self.Armorlist[int(self.Armor_view.identify_row(event.y)[1:],base=16)-self.Armor_firstindex]
            self.Armor_Equip["state"]="normal"
            self.Obj_suppr["state"]="normal"
            self.Obj_transfer["state"]="normal"

            self.Solid_add["state"]="normal"
            self.Solid_remove["state"]="normal"

            if self.selected_item.is_stackable:
                self.Obj_add["state"]="normal"
                self.Obj_remove["state"]="normal"

                if not self.master.master.selectedchar.inventory[self.selected_item]:
                    self.Obj_remove["state"]="disabled"

            else:
                if self.master.master.selectedchar.inventory[self.selected_item]:
                    self.Obj_remove["state"]="normal"
                else:
                    self.Obj_add["state"]="normal"

            if self.selected_item in self.master.master.selectedchar.playerequipment.values():
                self.Equip_remove["state"]="normal"

    def import_obj(self):
        """ Fonction pour équiper un objet venant des fichier"""
        # on demande le fichier d'équipement à importer
        filenames=askopenfilenames(title="Choisissez le fichier d'objet",filetypes=[],initialdir=path.dirname(__file__))

        if filenames:
            for filename in filenames:
                with open(filename,"rb") as fichier:
                    # si le fichier importé est bien celui d'un objet, on le stocke dans l'inventaire
                    obj=pk.Unpickler(fichier).load()
                    if type(obj) in (pc.Obj,pc.MeleeEquip,pc.ThrowEquip,pc.ArmorEquip,pc.ShieldEquip):
                        self.master.master.selectedchar.inventory[obj]=1
            self.refresh()

    def export_obj(self):
        """ fonction pour exporter un objet de l'inventaire """
        # on demande le nom d'exoprtation du importer
        filename=asksaveasfilename(title="Enregistrez l'objet",filetypes=[],defaultextension=[],initialfile=[self.selected_item.name],initialdir=path.dirname(__file__))

        selected_item = self.selected_item.copy()

        if type(self.selected_item)==pc.ThrowEquip:
            selected_item.del_cord()

        if filename:
            with open(filename,"wb") as fichier:
                pk.Pickler(fichier).dump(selected_item)

    def change_number(self,number):
        """ fonction pour changer le nombre d'instances d'un objet dans l'inventaire """
        self.master.master.selectedchar.change_invent_number(self.selected_item,number)
        self.refresh()

        # si l'objet n'est pas stackable, on change les boutons disponibles
        if self.master.master.selectedchar.inventory[self.selected_item] and not self.selected_item.is_stackable:
            self.Obj_add["state"]="disabled"
            self.Obj_remove["state"]="normal"

        elif self.master.master.selectedchar.inventory[self.selected_item] and self.selected_item.is_stackable:
            self.Obj_remove["state"]="normal"

        # si le nombre atteint 0, on enlève la posiibilité de retirer un objet
        if not self.master.master.selectedchar.inventory[self.selected_item]:
            self.Obj_remove["state"]="disabled"
            self.Obj_add["state"]="normal"

            # si l'objet est équipé, on le déséquipe
            if self.selected_item in self.master.master.selectedchar.playerequipment.values():
                self.unequip_item()

    def suppr_obj(self):
        """ fonction pour supprimer un objet de l'inventaire """
        # on retire l'objet de l'inventaire
        self.master.master.selectedchar.invent_suppr(self.selected_item)
        self.refresh()

        # si l'objet est équipé, on le déséquipe
        if self.selected_item in self.master.master.selectedchar.playerequipment.values():
            self.unequip_item()

        # on désélectionne l'objet, car il n'est plus censé exister
        self.unselect_previous()

    def equip_item(self,where=""):
        """ fonction pour équiper l'objet sélectionné """

        # on équipe l'objet et on rafraichit le cadre qui affiche l'objet équipé. Si c'est une arme, on dit de quel côté l'équiper
        if type(self.selected_item)==pc.ArmorEquip:
            self.master.master.selectedchar.equip_obj(self.selected_item)
        elif type(self.selected_item)==pc.ThrowEquip:
            self.master.master.selectedchar.equip_obj(self.selected_item,where)
        else:
            self.master.master.selectedchar.equip_obj(self.selected_item,where)

        # on peut alors déséquiper l'objet du personnage
        self.Equip_remove["state"]="normal"

        # print(self.master.master.selectedchar.playerequipment["left_melee"]==self.master.master.selectedchar.playerequipment["right_melee"])

    def unequip_item(self):
        """ fonction pour déséquiper l'objet sélectionné """
        self.master.master.selectedchar.unequip_obj(self.selected_item)
        self.Equip_remove["state"]="disabled"

        # on rafraîchit le cadre qui affichait l'objet déséquipé
        if type(self.selected_item)==pc.ThrowEquip:
            self.selected_item.del_cord()


    def equip_cord(self,where):
        """ fonction pour équiper une corde sur un arc/ une arbalète """
        if self.master.master.selectedchar.playerequipment["left_throw"] and self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"]:
            # si l'arme est à 2 mains, on vérifier juste qu'on a assez de cordes pour en "corder" une de plus
            if self.master.master.selectedchar.playerequipment["left_throw"].carac["hand"]==2:
                if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][0] or self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]!=self.selected_item.perc:
                    self.master.master.selectedchar.playerequipment[where+"_throw"].load_cord(self.selected_item)

            # sinon, on vérifie si la deuxième arme existe, puis si elle a besoin d'une corde
            elif self.master.master.selectedchar.playerequipment["right_throw"] and self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"]:

                if (self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]==self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]==self.selected_item.perc) or (self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]==self.selected_item.perc and self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]==0) or (self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]==self.selected_item.perc and self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]==0) or (self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]==self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]==0):
                    if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerquipment["left_throw"].carac["cord"][0]+self.master.master.selectedchar.playerquipment["right_throw"].carac["cord"][0]:
                        self.master.master.selectedchar.playerequipment[where+"_throw"].load_cord(self.selected_item)

                elif (self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]==self.selected_item.perc and self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]!=self.selected_item.perc):
                    if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerquipment["left_throw"].carac["cord"][0]:
                        self.master.master.selectedchar.playerequipment[where+"_throw"].load_cord(self.selected_item)

                elif self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]==self.selected_item.perc and self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]!=self.selected_item.perc:
                    if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerquipment["right_throw"].carac["cord"][0]:
                        self.master.master.selectedchar.playerequipment[where+"_throw"].load_cord(self.selected_item)

                else:
                    self.master.master.selectedchar.playerequipment[where+"_throw"].load_cord(self.selected_item)

            else:
                if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][0] or self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]!=self.selected_item.perc:
                    if where == "left":
                        self.master.master.selectedchar.playerequipment[where+"_throw"].load_cord(self.selected_item)


        # sinon, on regarde pour la droite, qui est alors forcément à une main si elle existe
        elif self.master.master.selectedchar.playerequipment["right_throw"] and self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"]:
            # si on a assez de corde pour corder à droite, on dévérouille le bouton
            if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][0] or self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]!=self.selected_item.perc:
                if where == "right":
                    self.master.master.selectedchar.playerequipment[where+"_throw"].load_cord(self.selected_item)



    def change_solid(self,number):
        if self.selected_item:
            self.selected_item.upsolid(number)

            if self.selected_item in self.master.master.selectedchar.playerequipment.values():
                self.CharArmF.refresh()
                self.CharMelF.refresh()
                self.CharThrF.refresh()

            self.refresh()





class ObjPopup(object):
    """ Popup d'information lorsqu'on survole un objet"""

    def __init__(self,master):
        self.master=master
        self.infowindow=None


    def showinfo(self,obj,event=None):
        """ Fonction qui crée et fait apparaitre le popup de description de l'objet """

        if not self.infowindow:
            x = event.x_root + 10
            y = event.y_root + 10
            self.infowindow =Toplevel(self.master,highlightbackground="black",highlightthickness=1)
            self.infowindow.wm_overrideredirect(1)
            self.infowindow.wm_geometry('+%d+%d' % (x, y))
            self.Description=Message(self.infowindow,text=obj.description,width=500)
            self.Description.grid(row=0,column=0)

            # si l'objet est une corde, on affiche le pourcentage de casse
            if type(obj)==pc.Cord:
                Label(self.infowindow,text="Casse à "+str(obj.perc)+"%").grid(row=0,column=1)

    def hideinfo(self,event=None):
        """ fonction qui détruit le popup """
        if self.infowindow:
            self.infowindow.destroy()
            self.infowindow=None




class MeleePopup(object):
    """ Popup d'information lorsqu'on survole une arme de mélée"""

    def __init__(self,master,**kwargs):
        object.__init__(self)
        self.keylist=["dgt_tr","dgt_ctd","estoc","hast","mastery","quality","solid"]
        self.labellist=["Dgt tr","Dgt ctd","Estoc","Hast","vit","Maîtr.","Qual.","Sol."]
        self.master=master
        self.infowindow=None


    def showinfo(self,obj,event=None):
        """ Fonction qui crée et fait apparaitre le popup de description de l'objet, et des caractéristiques """

        if not self.infowindow:
            x = event.x_root + 10
            y = event.y_root + 10
            self.infowindow =Toplevel(self.master,highlightbackground="black",highlightthickness=1)
            self.infowindow.wm_overrideredirect(1) #supprime les ornements de la Toplevel
            self.infowindow.wm_geometry('+%d+%d' % (x, y))
            self.Description=Message(self.infowindow,text=obj.description,width=500)
            self.Description.grid(row=0,column=0,columnspan=8)
            i=0
            for key in self.keylist:

                if key=="hast":
                    Label(self.infowindow,text=self.labellist[i]).grid(row=1,column=i)
                    Label(self.infowindow,text="Non"*(not obj.carac[key])+"Oui"*(obj.carac[key])).grid(row=2,column=i)
                    i+=1
                    Label(self.infowindow,text="Vit."*(not obj.carac[key])+"Bon. Hast"*(obj.carac[key])).grid(row=1,column=i)
                    Label(self.infowindow,text=obj.carac["vit"*(not obj.carac[key])+"hast_bonus"*(obj.carac[key])]).grid(row=2,column=i)
                else:
                    Label(self.infowindow,text=self.labellist[i]).grid(row=1,column=i)
                    Label(self.infowindow,text=obj.carac[key]).grid(row=2,column=i)
                i+=1


    def hideinfo(self,event=None):
        """ fonction qui détruit le popup """
        if self.infowindow:
            self.infowindow.destroy()
            self.infowindow=None




class ThrowPopup(object):
    """ Popup d'information lorsqu'on survole une arme de jet"""

    def __init__(self,master,**kwargs):
        object.__init__(self)
        self.keylist=["dgt","pa","mastery","solid"]
        self.labellist=["Dég.","P.-Arm.","Maîtr.","Sol."]
        self.master=master
        self.infowindow=None


    def showinfo(self,obj,event=None):
        """ Fonction qui crée et fait apparaitre le popup de description de l'objet, et des caractéristiques """

        if not self.infowindow:
            x = event.x_root + 10
            y = event.y_root + 10
            self.infowindow =Toplevel(self.master,highlightbackground="black",highlightthickness=1)
            self.infowindow.wm_overrideredirect(1)
            self.infowindow.wm_geometry('+%d+%d' % (x, y))
            self.Description=Message(self.infowindow,text=obj.description,width=500)
            self.Description.grid(row=0,column=0,columnspan=8)

            i=0
            for key in self.keylist:
                Label(self.infowindow,text=self.labellist[i]).grid(row=1,column=i)
                Label(self.infowindow,text=obj.carac[key]).grid(row=2,column=i)
                i+=1

            self.scopeFrame=Frame(self.infowindow)
            self.scopeFrame.grid(row=1,column=5,rowspan=2)
            Label(self.scopeFrame,text="Préc.").grid(row=1,column=0)
            Label(self.scopeFrame,text="Vit.").grid(row=2,column=0)
            Label(self.scopeFrame,text=0).grid(row=0,column=1)
            ttk.Separator(self.scopeFrame,orient="vertical").grid(row=1,column=1,rowspan=2,sticky="ns")

            for i in range(len(obj.carac["scope"])):
                Label(self.scopeFrame,text=obj.carac["scope"][i][0]).grid(row=0,column=3+2*i)
                ttk.Separator(self.scopeFrame,orient="vertical").grid(row=1,column=3+2*i,rowspan=2,sticky="NS")
                Label(self.scopeFrame,text=obj.carac["scope"][i][2]).grid(row=1,column=2+2*i)
                Label(self.scopeFrame,text=obj.carac["scope"][i][1]).grid(row=2,column=2+2*i)

    def hideinfo(self,event=None):
        """ fonction qui détruit le popup """
        if self.infowindow:
            self.infowindow.destroy()
            self.infowindow=None




class ShieldPopup(object):
    """ Popup d'information lorsqu'on survole un bouclier"""

    def __init__(self,master,**kwargs):
        object.__init__(self)
        self.keylist=["close","dist","mastery","mobi","vit","quality","solid"]
        self.labellist=["Par. CàC","Par. Dist.","Maîtr.","Mobi.","Vit.","Quali.","Sol."]
        self.master=master
        self.infowindow=None


    def showinfo(self,obj,event=None):
        """ Fonction qui crée et fait apparaitre le popup de description de l'objet, et des caractéristiques """

        if not self.infowindow:
            x = event.x_root + 10
            y = event.y_root + 10
            self.infowindow =Toplevel(self.master,highlightbackground="black",highlightthickness=1)
            self.infowindow.wm_overrideredirect(1)
            self.infowindow.wm_geometry('+%d+%d' % (x, y))
            self.Description=Message(self.infowindow,text=obj.description,width=500)
            self.Description.grid(row=0,column=0,columnspan=8)
            i=0
            for key in self.keylist:
                Label(self.infowindow,text=self.labellist[i]).grid(row=1,column=i)
                Label(self.infowindow,text=obj.carac[key]).grid(row=2,column=i)
                i+=1

    def hideinfo(self,event=None):
        """ fonction qui détruit le popup """
        if self.infowindow:
            self.infowindow.destroy()
            self.infowindow=None




class ArmorPopup(object):
    """ Popup d'information lorsqu'on survole une armure"""

    def __init__(self,master,**kwargs):
        object.__init__(self)
        self.keylist=["prot","amort","mobi","vit","solid"]
        self.labellist=["Prot.","Amort.","Mobi.","Vit.","Sol."]
        self.master=master
        self.infowindow=None


    def showinfo(self,obj,event=None):
        """ Fonction qui crée et fait apparaitre le popup de description de l'objet, et des caractéristiques """

        if not self.infowindow:
            x = event.x_root + 10
            y = event.y_root + 10
            self.infowindow =Toplevel(self.master,highlightbackground="black",highlightthickness=1)
            self.infowindow.wm_overrideredirect(1)
            self.infowindow.wm_geometry('+%d+%d' % (x, y))
            self.Description=Message(self.infowindow,text=obj.description,width=500)
            self.Description.grid(row=0,column=0,columnspan=8)
            i=0
            for key in self.keylist:
                Label(self.infowindow,text=self.labellist[i]).grid(row=1,column=i)
                Label(self.infowindow,text=obj.carac[key]).grid(row=2,column=i)
                i+=1

    def hideinfo(self,event=None):
        """ fonction qui détruit le popup """
        if self.infowindow:
            self.infowindow.destroy()
            self.infowindow=None




class ObjCreatorFrame(Frame):
    """ Widget de création des objets pour l'inventaire du personnage """

    def __init__(self,master,**kwargs):
        Frame.__init__(self,master,kwargs)

        # Widgets et variables nécessaires à la création de tout type d'objet
        self.New_name=StringVar()
        self.New_description=StringVar()
        self.New_stackable=BooleanVar()

        self.Name_entry=Entry(self,width=25,textvariable=self.New_name)
        self.Description_entry=Text(self,width=60,height=5,font=("TkDefaultFont", 9))#,textvariable=self.New_description)
        self.Stackable_entry=Checkbutton(self,variable=self.New_stackable)
        self.ObjType=ttk.Combobox(self,width=15,values=["Objet","Arme de mélée","Arme de jet","Corde","Bouclier","Armure"],state="readonly")
        self.ObjType.current(0)
        self.ObjType.bind("<<ComboboxSelected>>",func=self.change_obj_type)
        self.Register=Button(self,text="Ajouter",command=self.inventory_add)

        self.Name_label=Label(self,text="Nom de l'objet")
        self.Description_label=Label(self,text="Description")
        self.Stackable_label=Label(self,text="Stackable")

        self.Name_label.grid(row=0,column=0,sticky="W",columnspan=2)
        self.Description_label.grid(row=0,column=2,sticky="W",columnspan=6)
        self.Stackable_label.grid(row=0,column=8,columnspan=2)
        self.Name_entry.grid(row=1,column=0,sticky="N",padx="4p",columnspan=2)
        self.ObjType.grid(row=2,column=0,columnspan=2)
        self.Description_entry.grid(row=1,column=2,padx="4p",rowspan=2,columnspan=6)
        self.Stackable_entry.grid(row=1,column=8,sticky="N",padx="4p",columnspan=2)
        self.Register.grid(row=2,column=8,columnspan=2)

        # dictionnaire de tous les widgets et variables pour la création d'arme de mélée
        self.Melee={}

        self.Melee["tr_var"]=IntVar()
        self.Melee["ctd_var"]=IntVar()
        self.Melee["estoc_var"]=IntVar()
        self.Melee["hast_var"]=BooleanVar()
        self.Melee["vit_var"]=IntVar()
        self.Melee["quality_var"]=StringVar()
        self.Melee["solidity_var"]=IntVar()

        self.Melee["weight_label"]=Label(self,text="Type d'arme")
        self.Melee["hand_label"]=Label(self,text="Taille")
        self.Melee["tr_label"]=Label(self,text="Tranchant")
        self.Melee["ctd_label"]=Label(self,text="Contondant")
        self.Melee["estoc_label"]=Label(self,text="Estoc")
        self.Melee["hast_label"]=Label(self,text="Hast")
        self.Melee["hast_bonus_label"]=Label(self,text="Bonus de hast")
        self.Melee["vit_label"]=Label(self,text="Vitesse")
        self.Melee["quality_label"]=Label(self,text="Qualité")
        self.Melee["solidity_label"]=Label(self,text="Solidité")

        self.Melee["weight_entry"]=ttk.Combobox(self,values=["Poings","Légère","Moyenne","Lourde"],state="readonly",width=9)
        self.Melee["weight_entry"].current(0)
        self.Melee["hand_entry"]=ttk.Combobox(self,values=["1 main","2 mains"],state="readonly",width=8)
        self.Melee["hand_entry"].current(0)
        self.Melee["tr_entry"]=Entry(self,textvariable=self.Melee["tr_var"],width=9)
        self.Melee["ctd_entry"]=Entry(self,textvariable=self.Melee["ctd_var"],width=10)
        self.Melee["estoc_entry"]=Entry(self,textvariable=self.Melee["estoc_var"],width=5)
        self.Melee["hast_entry"]=Checkbutton(self,variable=self.Melee["hast_var"],command=self.hast_change)
        self.Melee["vit_entry"]=Entry(self,textvariable=self.Melee["vit_var"],width=13)
        self.Melee["quality_entry"]=Entry(self,textvariable=self.Melee["quality_var"],width=7)
        self.Melee["solidity_entry"]=Entry(self,textvariable=self.Melee["solidity_var"],width=8)

        # dictionnaire de tous les widgets et variables pour la création d'arme de jet
        self.Throw={}

        self.Throw["dgt_var"]=IntVar()
        self.Throw["pa_var"]=IntVar()
        self.Throw["quality_var"]=StringVar()
        self.Throw["solidity_var"]=IntVar()

        self.Throw["hand_label"]=Label(self,text="Taille")
        self.Throw["type_label"]=Label(self,text="Type")
        self.Throw["dgt_label"]=Label(self,text="Dégats")
        self.Throw["pa_label"]=Label(self,text="Perce-armure")
        self.Throw["solidity_label"]=Label(self,text="Solidité")
        self.Throw["scope"]=Frame(self)
        Label(self.Throw["scope"],text="Max palier portée").grid(row=0,column=0)
        Label(self.Throw["scope"],text="Vitesse").grid(row=0,column=1)
        Label(self.Throw["scope"],text="Précision").grid(row=0,column=2)
        Entry(self.Throw["scope"],textvariable=IntVar(value=2),width=16).grid(row=1,column=0,padx="4p")
        Entry(self.Throw["scope"],textvariable=IntVar(),width=6).grid(row=1,column=1,padx="4p")
        Entry(self.Throw["scope"],textvariable=IntVar(),width=9).grid(row=1,column=2,padx="4p")

        self.Throw["scope"].bind("<Button-3>",func=self.choose_scope)
        for i in self.Throw["scope"].grid_slaves():
            i.bind("<Button-3>",func=self.choose_scope)
        self.Throw["popup"]=Menu(self,tearoff=0)
        self.Throw["popup"].add_command(label="Ajouter une ligne",command=self.scope_add)
        self.Throw["popup"].add_command(label="Retirer une ligne",command=self.del_scope)

        self.Throw["hand_entry"]=ttk.Combobox(self,values=["1 main","2 mains"],state="readonly",width=8)
        self.Throw["hand_entry"].current(0)
        self.Throw["type_entry"]=ttk.Combobox(self,values=["Lancer","Tir"],state="readonly",width=8)
        self.Throw["type_entry"].current(1)
        self.Throw["dgt_entry"]=Entry(self,textvariable=self.Throw["dgt_var"],width=6)
        self.Throw["pa_entry"]=Entry(self,textvariable=self.Throw["pa_var"],width=12)
        self.Throw["solidity_entry"]=Entry(self,textvariable=self.Throw["solidity_var"],width=8)

        #widget pour le pourcentage de la corde
        self.Cord_var=IntVar()
        self.Cord_label=Label(self,text="Casse (en %)")
        self.Cord_entry=Entry(self,textvariable=self.Cord_var,width=4)

        # dictionnaire de tous les widgets et variables pour la création de bouclier
        self.Shield={}

        self.Shield["close_var"]=IntVar()
        self.Shield["dist_var"]=IntVar()
        self.Shield["mobi_var"]=IntVar()
        self.Shield["vit_var"]=IntVar()
        self.Shield["quality_var"]=StringVar()
        self.Shield["solidity_var"]=IntVar()

        self.Shield["hand_label"]=Label(self,text="Taille")
        self.Shield["close_label"]=Label(self,text="Parade CàC")
        self.Shield["dist_label"]=Label(self,text="Parade distance")
        self.Shield["mobi_label"]=Label(self,text="Mobilité")
        self.Shield["vit_label"]=Label(self,text="Vitesse")
        self.Shield["quality_label"]=Label(self,text="Qualité")
        self.Shield["solidity_label"]=Label(self,text="Solidité")

        self.Shield["hand_entry"]=ttk.Combobox(self,values=["1 main","2 mains"],state="readonly",width=8)
        self.Shield["hand_entry"].current(0)
        self.Shield["close_entry"]=Entry(self,textvariable=self.Shield["close_var"],width=10)
        self.Shield["dist_entry"]=Entry(self,textvariable=self.Shield["dist_var"],width=15)
        self.Shield["mobi_entry"]=Entry(self,textvariable=self.Shield["mobi_var"],width=8)
        self.Shield["vit_entry"]=Entry(self,textvariable=self.Shield["vit_var"],width=6)
        self.Shield["quality_entry"]=Entry(self,textvariable=self.Shield["quality_var"],width=7)
        self.Shield["solidity_entry"]=Entry(self,textvariable=self.Shield["solidity_var"],width=8)

        # dictionnaire de tous les widgets et variables pour la création d'armure
        self.Armor={}

        self.Armor["prot_var"]=IntVar()
        self.Armor["amort_var"]=IntVar()
        self.Armor["mobi_var"]=IntVar()
        self.Armor["vit_var"]=IntVar()
        self.Armor["solidity_var"]=IntVar()

        self.Armor["location_label"]=Label(self,text="Localisation")
        self.Armor["prot_label"]=Label(self,text="Protection")
        self.Armor["amort_label"]=Label(self,text="Amortissement")
        self.Armor["mobi_label"]=Label(self,text="Mobilité")
        self.Armor["vit_label"]=Label(self,text="Vitesse")
        self.Armor["solidity_label"]=Label(self,text="Solidité")

        self.Armor["location_entry"]=ttk.Combobox(self,values=["Heaume","Spallières","Brassards","Avant-bras","Plastron","Jointures","Tassette","Cuissots","Grèves","Solerets"],state="readonly",width=10)
        self.Armor["location_entry"].current(0)
        self.Armor["prot_entry"]=Entry(self,textvariable=self.Armor["prot_var"],width=10)
        self.Armor["amort_entry"]=Entry(self,textvariable=self.Armor["amort_var"],width=13)
        self.Armor["mobi_entry"]=Entry(self,textvariable=self.Armor["mobi_var"],width=8)
        self.Armor["vit_entry"]=Entry(self,textvariable=self.Armor["vit_var"],width=6)
        self.Armor["solidity_entry"]=Entry(self,textvariable=self.Armor["solidity_var"],width=8)


    def change_obj_type(self,event=None):
        """Fonction pour alterner entre les différents types d'objets et faire changer les widgets"""
        for i in self.grid_slaves(row=3):
            i.grid_forget()

        for i in self.grid_slaves(row=4):
            i.grid_forget()

        val=self.ObjType.get()

        # listes des caractéristiques demandées pour chaque objet
        meleelist=["weight","hand","tr","ctd","estoc","hast","quality","solidity"]
        throwlist=["hand","type","dgt","pa","solidity"]
        shieldlist=["hand","close","dist","mobi","vit","quality","solidity"]
        armorlist=["location","prot","amort","mobi","vit","solidity"]

        if val=="Arme de mélée":
            i=0
            for key in meleelist:
                self.Melee[key+"_label"].grid(row=3,column=i,padx="4p")
                self.Melee[key+"_entry"].grid(row=4,column=i,padx="4p")
                i+=1
                if key=="hast":
                    if self.Melee["hast_var"].get():
                        key="hast_bonus"
                        self.Melee[key+"_label"].grid(row=3,column=i,padx="4p")
                        self.Melee[key+"_entry"].grid(row=4,column=i,padx="4p")
                    else:
                        key="vit"
                        self.Melee[key+"_label"].grid(row=3,column=i,padx="4p")
                        self.Melee[key+"_entry"].grid(row=4,column=i,padx="4p")
                    i+=1

        elif val=="Arme de jet":
            i=0
            for key in throwlist:
                self.Throw[key+"_label"].grid(row=3,column=i,padx="4p")
                self.Throw[key+"_entry"].grid(row=4,column=i,padx="4p")
                i+=1
            self.Throw["scope"].grid(row=3,column=i,rowspan=3)


        elif val=="Bouclier":
            i=0
            for key in shieldlist:
                self.Shield[key+"_label"].grid(row=3,column=i,padx="4p")
                self.Shield[key+"_entry"].grid(row=4,column=i,padx="4p")
                i+=1
        elif val=="Armure":
            i=0
            for key in armorlist:
                self.Armor[key+"_label"].grid(row=3,column=i,padx="4p")
                self.Armor[key+"_entry"].grid(row=4,column=i,padx="4p")
                i+=1
        elif val=="Corde":
            self.Cord_label.grid(row=3,column=0)
            self.Cord_entry.grid(row=3,column=1)


    def hast_change(self):
        """Fonction pour passer du titre vitesse au titre bonus de hast """

        if self.Melee["hast_var"].get():
            self.Melee["vit_label"].grid_forget()

            self.Melee["hast_bonus_label"].grid(row=3,column=5,padx="4p")

        else:
            self.Melee["hast_bonus_label"].grid_forget()

            self.Melee["vit_label"].grid(row=3,column=5,padx="4p")


    def choose_scope(self,event=None):
        """Fonction d'apparition du popup pour ajouter/supprimer des lignes du tableau de portée """

        self.Throw["popup"].tk_popup(event.x_root,event.y_root+20,0)

    def del_scope(self,event=None):
        """ Fonction de suppression d'une ligne du tableau de portée """
        i=self.Throw["scope"].grid_size()[1]
        if i>2:
            for i in self.Throw["scope"].grid_slaves(row=i-1):
                i.destroy()


    def scope_add(self,event=None):
        """ Fonction d'ajout d'une ligne au tableau de portée"""
        i=self.Throw["scope"].grid_size()[1]
        Entry(self.Throw["scope"],textvariable=IntVar(),width=16).grid(row=i,column=0,padx="4p")
        Entry(self.Throw["scope"],textvariable=IntVar(),width=6).grid(row=i,column=1,padx="4p")
        Entry(self.Throw["scope"],textvariable=IntVar(),width=9).grid(row=i,column=2,padx="4p")

        for key in self.Throw["scope"].grid_slaves(row=i):
            key.bind("<Button-3>",self.choose_scope)



    def inventory_add(self):
        """ Fonction qui ajoute l'objet au personnage selectionné dans CharDFrame """
        val=self.ObjType.get()

        if val=="Objet":
            new_obj=pc.Obj(self.New_name.get(),self.Description_entry.get(0.0,"end"),self.New_stackable.get())

        elif val=="Arme de mélée":
            new_obj=pc.MeleeEquip(self.New_name.get(),self.Description_entry.get(0.0,"end"),self.New_stackable.get(),self.Melee["weight_entry"].get(),self.Melee["hast_var"].get())
            new_obj.upstats(self.Melee["hand_entry"].current()+1,self.Melee["tr_var"].get(),self.Melee["ctd_var"].get(),self.Melee["estoc_var"].get(),self.Melee["vit_var"].get())
            new_obj.newquali(self.Melee["quality_var"].get())
            new_obj.upsolid(self.Melee["solidity_var"].get())


        elif val=="Arme de jet":
            new_obj=pc.ThrowEquip(self.New_name.get(),self.Description_entry.get(0.0,"end"),self.New_stackable.get(),self.Throw["type_entry"].get())
            new_obj.upstats(self.Throw["hand_entry"].current()+1,self.Throw["dgt_var"].get(),self.Throw["pa_var"].get())
            new_obj.upsolid(self.Throw["solidity_var"].get())

            scopelist=[]
            for i in range(1,self.Throw["scope"].grid_size()[1]):
                sublist=[]
                for key in self.Throw["scope"].grid_slaves(row=i):
                    sublist.insert(0,int(key.get()))
                scopelist.append(sublist)
            new_obj.newscope(scopelist)

        elif val=="Armure":
            new_obj=pc.ArmorEquip(self.New_name.get(),self.Description_entry.get(0.0,"end"),self.New_stackable.get(),self.Armor["location_entry"].get())
            new_obj.upstats(self.Armor["prot_var"].get(),self.Armor["amort_var"].get(),self.Armor["mobi_var"].get(),self.Armor["vit_var"].get())
            new_obj.upsolid(self.Armor["solidity_var"].get())


        elif val=="Bouclier":
            new_obj=pc.ShieldEquip(self.New_name.get(),self.Description_entry.get(0.0,"end"),self.New_stackable.get())
            new_obj.upstats(self.Shield["hand_entry"].current()+1,self.Shield["close_var"].get(),self.Shield["dist_var"].get(),self.Shield["mobi_var"].get(),self.Shield["vit_var"].get())
            new_obj.upsolid(self.Shield["solidity_var"].get())
            new_obj.newquali(self.Shield["quality_var"].get())

        elif val=="Corde":
            new_obj=pc.Cord(self.New_name.get(),self.Description_entry.get(0.0,"end"),self.New_stackable.get(),self.Cord_var.get())


        self.master.master.master.selectedchar.inventory[new_obj]=1 #par défaut, on gagne 1 objet et il n'est pas équipé
        # print(self.master.master.master.selectedchar.inventory)
        self.master.refresh()




## Partie 6 Compétences

class CompetCreatorFrame(Frame):
    """ Widget de création des compétences """

    def __init__(self,master,**kw):
        Frame.__init__(self,master,**kw)
        Label(self,text="Créer une compétence").grid(row=0,column=0,sticky="w",columnspan=2)
        self.categlist=["Lore","Mélée","Jet","Combat vétéran","Armure"]
        self.Name_var=StringVar()

        Label(self,text="Catégorie").grid(row=1,column=0,sticky="w")
        Label(self,text="Sous-catégorie").grid(row=1,column=1,sticky="w")
        Label(self,text="Intitulé").grid(row=1,column=2)
        Label(self,text="Effets").grid(row=1,column=3,sticky="w")

        self.Categ_entry=ttk.Combobox(self,values=self.categlist,state="readonly")
        self.Categ_entry.current(0)
        self.Subcateg_entry=ttk.Combobox(self,values=[],state="disabled")
        self.Name_entry=Entry(self,textvariable=self.Name_var)
        self.Effect_entry=Text(self,width=100,height=5)
        self.Register_choice=Button(self,text="Enregistrer",command=self.register)
        self.suppr_choice=Button(self,text="Supprimer",command=self.suppr,state="disabled")

        self.Categ_entry.grid(row=2,column=0,sticky="n",padx='4p')
        self.Subcateg_entry.grid(row=2,column=1,sticky="n",padx='4p')
        self.Name_entry.grid(row=2,column=2,sticky="n",padx='4p')
        self.Effect_entry.grid(row=2,column=3,padx='4p')
        self.Register_choice.grid(row=1,column=4,rowspan=2,padx='4p')
        self.suppr_choice.grid(row=3,column=5,padx='4p')

        self.Categ_entry.bind("<<ComboboxSelected>>",self.subcateg_roll)

        # les compétences qui existent déjà
        self.Compet_view=ttk.Treeview(self)
        self.Compet_view["columns"]=("0","1")
        self.Compet_view.heading("#0",text="Catégorie")
        self.Compet_view.heading("0",text="Nom")
        self.Compet_view.heading("1",text="Effet")
        self.Compet_view.column("#0",width=110)
        self.Compet_view.column("0",width=200)
        self.Compet_view.column("1",width=1000)
        # les catégories
        for key in self.categlist:
            self.Compet_view.insert("","end",key,text=key)

        for key in ["Mains nues","Une main","Doubles","Deux mains","Bouclier"]:
            self.Compet_view.insert("Mélée","end",key,text=key)

        for key in ["Lancer","Arc","Arbalète"]:
            self.Compet_view.insert("Jet","end",key,text=key)

        self.Compet_view.grid(row=3,column=0,columnspan=5,pady="8p",sticky="w")
        self.Compet_view.bind("<Button-1>",func=self.select_compet)

    def subcateg_roll(self,event=None):
        """ Méthode pour faire changer les sous-catégories proposées en fonction de la catégorie choisie """
        val=self.Categ_entry.get()

        if val =="Mélée":
            self.Subcateg_entry["values"]=["Mains nues","Une main","Doubles","Deux mains","Bouclier"]
            self.Subcateg_entry.current(0)
            self.Subcateg_entry["state"]="readonly"

        elif val=="Jet":
            self.Subcateg_entry["values"]=["Lancer","Arc","Arbalète"]
            self.Subcateg_entry["state"]="readonly"
            self.Subcateg_entry.current(0)

        elif val=="Armure":
            self.Subcateg_entry.set("")
            self.Subcateg_entry["values"]=[]
            self.Subcateg_entry["state"]="disabled"

        else:
            self.Subcateg_entry.set("")
            self.Subcateg_entry["values"]=[]
            self.Subcateg_entry["state"]="disabled"



    def register(self):
        """ Méthode qui crée la nouvelle compétence """
        new_compet=pc.Competence(self.Categ_entry.get(),self.Subcateg_entry.get(),self.Name_var.get(),self.Effect_entry.get(0.0,"end"))

        self.master.competlist.append(new_compet)
        if new_compet.subcateg:
            self.Compet_view.insert(new_compet.subcateg,"end",(len(self.master.competlist)),values=[new_compet.name,new_compet.effect])
        else:
            self.Compet_view.insert(new_compet.categ,"end",(len(self.master.competlist)),values=[new_compet.name,new_compet.effect])

    def refresh(self):
        """ Méthode qui rafraîchit la liste des compétences """

        for key in ["Lore","Mains nues","Une main","Doubles","Deux mains","Bouclier","Lancer","Arc","Arbalète","Combat vétéran","Armure"]:
            for i in self.Compet_view.get_children(key):
                self.Compet_view.delete(i)

        if self.master.competlist:
            i=1
            for key in self.master.competlist:
                if key.subcateg:
                    self.Compet_view.insert(key.subcateg,"end",i,values=[key.name,key.effect])
                else:
                    self.Compet_view.insert(key.categ,"end",i,values=[key.name,key.effect])

                i+=1

    def select_compet(self,event):
        """ Méthode qui est appelée quand on sélectionne une compétence, pour ensuite la supprimer si besoin """
        if self.Compet_view.identify_row(event.y):

            try:
                self.selected_item=int(self.Compet_view.identify_row(event.y))
                self.suppr_choice["state"]="normal"

            except:
                self.selected_item=None
                self.suppr_choice["state"]="disabled"

        else:
            self.selected_item=None
            self.suppr_choice["state"]="disabled"

    def suppr(self):
        """ Méthode qui supprime la compétence sélectionnée """
        if type(self.selected_item)==int:
            self.master.competlist.pop(self.selected_item-1)
            self.refresh()
            self.selected_item=None
            self.suppr_choice["state"]="disabled"

    def grid(self,**kw):
        Frame.grid(self,**kw)
        self.refresh()




class CharCompetFrame(Frame):
    """ Widget pour attribuer des compétences au personnage """

    def __init__(self,master,**kw):
        Frame.__init__(self,master,**kw)
        self.selected_item=None
        self.selected_charitem=None
        self.modif_compet=None
        self.categlist=["Lore","Mélée","Jet","Combat vétéran","Armure"]


        # les compétences du personnage

        Label(self,text="Compétences du personnage").grid(row=0,column=0,sticky="w",padx="4p",pady='4p')
        self.modify_choice=Button(self,state="disabled",text="Modifier",command=self.modify_compet)
        self.suppr_choice=Button(self,state="disabled",text="Retirer",command=self.suppr_compet)

        self.CharCompet_view=ttk.Treeview(self)
        self.CharCompet_view["columns"]=("0","1")
        self.CharCompet_view.heading("#0",text="Catégorie")
        self.CharCompet_view.heading("0",text="Nom")
        self.CharCompet_view.heading("1",text="Effet")
        self.CharCompet_view.column("#0",width=110)
        self.CharCompet_view.column("0",width=200)
        self.CharCompet_view.column("1",width=500)
        for key in self.categlist:
            self.CharCompet_view.insert("","end",key,text=key)

        for key in ["Mains nues","Une main","Doubles","Deux mains","Bouclier"]:
            self.CharCompet_view.insert("Mélée","end",key,text=key)

        for key in ["Lancer","Arc","Arbalète"]:
            self.CharCompet_view.insert("Jet","end",key,text=key)

        self.CharCompet_view.grid(row=1,column=0,columnspan=5,rowspan=2,pady="8p",sticky="wn",padx="4p")
        self.modify_choice.grid(row=1,column=5)
        self.suppr_choice.grid(row=2,column=5)
        self.CharCompet_view.bind("<Button-1>",func=self.select_charcompet)


        # les compétences qui existent déjà

        Label(self,text="Compétences disponibles").grid(row=3,column=0,sticky="ws",padx="4p",pady="4p")
        self.transfer_choice=Button(self,state="disabled",text="Prendre",command=self.transfer_compet)

        self.Compet_view=ttk.Treeview(self)
        self.Compet_view["columns"]=("0","1")
        self.Compet_view.heading("#0",text="Catégorie")
        self.Compet_view.heading("0",text="Nom")
        self.Compet_view.heading("1",text="Effet")
        self.Compet_view.column("#0",width=110)
        self.Compet_view.column("0",width=200)
        self.Compet_view.column("1",width=500)
        for key in self.categlist:
            self.Compet_view.insert("","end",key,text=key)

        for key in ["Mains nues","Une main","Doubles","Deux mains","Bouclier"]:
            self.Compet_view.insert("Mélée","end",key,text=key)

        for key in ["Lancer","Arc","Arbalète"]:
            self.Compet_view.insert("Jet","end",key,text=key)

        self.Compet_view.grid(row=4,column=0,columnspan=5,pady="8p",sticky="w",padx="4p")
        self.transfer_choice.grid(row=4,column=5)
        self.Compet_view.bind("<Button-1>",func=self.select_compet)


        # widgets de modification
        ttk.Separator(self,orient="vertical").grid(row=0,column=6,rowspan=5,sticky="ns",padx="4p",pady="4p")
        self.modif_var=StringVar()
        self.modif_name=Entry(self,textvariable=self.modif_var)
        self.modif_effect=Text(self,width=50,height=6)
        self.modif_validate=Button(self,text="Enregistrer",command=self.modif_register)

        self.bind("<Visibility>",func=self.refresh)


    def transfer_compet(self):
        """ Méthode qui associe la compétence sélectionnée dans le général au personnage """
        if self.selected_item:
            self.master.master.selectedchar.competences.append(self.master.master.master.competlist[self.selected_item-1].copy())
            self.refresh_char()

    def refresh(self,event=None):
        """ Méthode qui rafraîchit tout """
        self.refresh_char()
        self.refresh_general()


    def refresh_char(self):
        """ Méthode qui rafraîchit la liste des compétences du personnage """

        for key in ["Lore","Mains nues","Une main","Doubles","Deux mains","Bouclier","Lancer","Arc","Arbalète","Combat vétéran","Armure"]:
            for i in self.CharCompet_view.get_children(key):
                self.CharCompet_view.delete(i)

        for i in self.grid_slaves(column=7):
            i.grid_forget()

        if self.master.master.selectedchar.competences:
            i=1
            for key in self.master.master.selectedchar.competences:
                if key.subcateg:
                    self.CharCompet_view.insert(key.subcateg,"end",i,values=[key.name,key.effect])
                else:
                    self.CharCompet_view.insert(key.categ,"end",i,values=[key.name,key.effect])

                i+=1

    def refresh_general(self):
        """ Méthode qui rafraîchit la liste des compétences """

        for key in ["Lore","Mains nues","Une main","Doubles","Deux mains","Bouclier","Lancer","Arc","Arbalète","Combat vétéran","Armure"]:
            for i in self.Compet_view.get_children(key):
                self.Compet_view.delete(i)

        if self.master.master.master.competlist:
            i=1
            for key in self.master.master.master.competlist:
                if key.subcateg:
                    self.Compet_view.insert(key.subcateg,"end",i,values=[key.name,key.effect])
                else:
                    self.Compet_view.insert(key.categ,"end",i,values=[key.name,key.effect])

                i+=1

    def select_compet(self,event):
        """ Méthode qui sélectionne une compétence de la liste générale """

        if self.Compet_view.identify_row(event.y):

            try:
                self.selected_item=int(self.Compet_view.identify_row(event.y))
                self.transfer_choice["state"]="normal"

            except:
                self.selected_item=None
                self.transfer_choice["state"]="disabled"

        else:
            self.selected_item=None
            self.transfer_choice["state"]="disabled"

    def select_charcompet(self,event):
        """ Méthode qui sélectionne une compétence du personnage """
        if self.CharCompet_view.identify_row(event.y):

            try:
                self.selected_charitem=int(self.CharCompet_view.identify_row(event.y))
                self.selected_compet=None
                self.suppr_choice["state"]="normal"
                self.modify_choice["state"]="normal"

            except:
                self.selected_charitem=None
                self.selected_compet=None
                self.suppr_choice["state"]="disabled"
                self.modify_choice["state"]="disabled"

        else:
            self.selected_charitem=None
            self.selected_compet=None
            self.suppr_choice["state"]="disabled"
            self.modify_choice["state"]="disabled"

    def modify_compet(self):
        """ Méthode qui permet d'éditer la compétence du personnage sélectionnée """
        if self.selected_charitem:
            self.selected_compet=self.master.master.selectedchar.competences[self.selected_charitem-1]
            Label(self,text="Modifications").grid(row=0,column=7)
            self.modif_name.grid(row=1,column=7,sticky="w")
            self.modif_effect.grid(row=2,column=7,sticky="w")
            self.modif_validate.grid(row=3,column=7)
            self.modif_var.set(self.selected_compet.name)
            self.modif_effect.delete(0.0,"end")
            self.modif_effect.insert("end",self.selected_compet.effect)

    def suppr_compet(self):
        """ Méthode qui retire la compétence de personnage sélectionnée """
        if self.selected_charitem:
            self.master.master.selectedchar.competences.pop(self.selected_charitem-1)
            self.suppr_choice["state"]="disabled"
            self.modify_choice["state"]="disabled"
            self.refresh_char()

    def modif_register(self):
        """ Méthode qui permet d'enregistrer les modifications apportées """
        self.selected_compet.name=self.modif_var.get()
        self.selected_compet.effect=self.modif_effect.get(0.0,"end")
        self.refresh_char()




## Partie 7 Les sorts

class SpellCreatorFrame(Frame):
    """ Widget de création des sorts """

    def __init__(self,master,**kw):
        Frame.__init__(self,master,**kw)
        Label(self,text="Créer un sort").grid(row=0,column=0,sticky="w",columnspan=2)
        self.selected_item=None
        self.elemlist=["Foudre"]
        self.subcateglist=["Emprise","Appel","Altération","Transfert","Divination","Lien"]
        self.Name_var=StringVar()
        self.Cost_var=IntVar()

        Label(self,text="Elément").grid(row=1,column=0,sticky="w")
        Label(self,text="Sous-catégorie").grid(row=1,column=1,sticky="w")
        Label(self,text="Nom").grid(row=1,column=2,sticky="w")
        Label(self,text="Effets").grid(row=3,column=0,sticky="w")
        Label(self,text="Description").grid(row=3,column=2,sticky="w")
        Label(self,text="Coût").grid(row=1,column=3,sticky="w")

        self.Elem_entry=ttk.Combobox(self,values=self.elemlist,state="readonly")
        self.Elem_entry.current(0)
        self.Subcateg_entry=ttk.Combobox(self,values=self.subcateglist,state="readonly")
        self.Subcateg_entry.current(0)
        self.Name_entry=Entry(self,textvariable=self.Name_var)
        self.Effect_entry=Text(self,width=50,height=5)
        self.Description_entry=Text(self,width=50,height=5)
        self.Cost_entry=Entry(self,textvariable=self.Cost_var)
        self.Register_choice=Button(self,text="Enregistrer",command=self.register)
        self.suppr_choice=Button(self,text="Supprimer",command=self.suppr,state="disabled")

        self.Elem_entry.grid(row=2,column=0,sticky="w",padx='4p')
        self.Subcateg_entry.grid(row=2,column=1,sticky="w",padx='4p')
        self.Name_entry.grid(row=2,column=2,sticky="w",padx='4p')
        self.Effect_entry.grid(row=4,column=0,padx='4p',columnspan=2,sticky="w")
        self.Cost_entry.grid(row=2,column=3,padx="4p",sticky="w")
        self.Description_entry.grid(row=4,column=2,padx='4p',columnspan=2,sticky="w")
        self.Register_choice.grid(row=2,column=4,rowspan=3,padx='4p')
        self.suppr_choice.grid(row=5,column=4,padx='4p')


        # les sorts qui existent déjà
        self.Spell_view=ttk.Treeview(self)
        self.Spell_view["columns"]=("0","1","2")
        self.Spell_view.heading("0",text="Effet")
        self.Spell_view.heading("1",text="Description")
        self.Spell_view.heading("2",text="Coût")
        self.Spell_view.column("#0",width=110)
        self.Spell_view.column("0",width=400)
        self.Spell_view.column("1",width=400)
        self.Spell_view.column("2",width=50)
        # les catégories
        for key in self.elemlist:
            self.Spell_view.insert("","end",key,text=key)

            for kkey in self.subcateglist:
                self.Spell_view.insert(key, "end", key+kkey, text=kkey)


        self.Spell_view.grid(row=5,column=0,columnspan=4,pady="8p",sticky="w")
        self.Spell_view.bind("<Button-1>",func=self.select_spell)


    def register(self):
        """ Méthode qui crée le nouveau sort """
        new_spell=pc.Spell(self.Elem_entry.get(),self.Subcateg_entry.get(),self.Name_var.get(),self.Effect_entry.get(0.0,"end"),self.Description_entry.get(0.0,"end"),self.Cost_var.get())

        self.master.spelllist.append(new_spell)
        self.Spell_view.insert(new_spell.elem+new_spell.subcateg,"end",(len(self.master.spelllist)),text=new_spell.name,values=[new_spell.effect,new_spell.description,new_spell.cost])

    def refresh(self):
        """ Méthode qui rafraîchit la liste des sorts """

        for key in self.elemlist:
            for kkey in self.subcateglist:
                for i in self.Spell_view.get_children(key+kkey):
                    self.Spell_view.delete(i)

        if self.master.spelllist:
            i=1
            for key in self.master.spelllist:
                self.Spell_view.insert(key.elem+key.subcateg,"end",i,text=key.name,values=[key.effect,key.description,key.cost])

                i+=1

    def select_spell(self,event):
        """ Méthode qui est appelée quand on sélectionne une compétence, pour ensuite la supprimer si besoin """
        if self.Spell_view.identify_row(event.y):

            try:
                self.selected_item=int(self.Spell_view.identify_row(event.y))
                self.suppr_choice["state"]="normal"

            except:
                self.selected_item=None
                self.suppr_choice["state"]="disabled"

        else:
            self.selected_item=None
            self.suppr_choice["state"]="disabled"

    def suppr(self):
        """ Méthode qui supprime la compétence sélectionnée """
        if type(self.selected_item)==int:
            self.master.spelllist.pop(self.selected_item-1)
            self.refresh()
            self.selected_item=None
            self.suppr_choice["state"]="disabled"

    def grid(self,**kw):
        Frame.grid(self,**kw)
        self.refresh()




class CharSpellFrame(Frame):
    """ Widget de création des sorts """

    def __init__(self,master,**kw):
        Frame.__init__(self,master,**kw)
        self.selected_item=None
        self.selected_charitem=None
        self.spells_list=[]
        self.lightning_image=ImageTk.PhotoImage(Image.open("Images/symb-lightning.png").resize((12,15),Image.ANTIALIAS))

        self.elemlist=["Foudre"]
        self.subcateglist=["Emprise","Appel","Altération","Transfert","Divination","Lien"]

        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=1)

        Label(self,text="Sorts du personnage").grid(row=0,column=0,sticky="w",padx="4p")
        self.plus_lightning=Button(self,text="+",image=self.lightning_image,compound="right",command=partial(self.modif_lightning,1),state="disabled")
        self.plus_lightning.grid(row=1,column=1)
        self.min_lightning=Button(self,text="-",image=self.lightning_image,compound="right",command=partial(self.modif_lightning,-1),state="disabled")
        self.min_lightning.grid(row=1,column=2,sticky="e")
        self.suppr_choice=Button(self,text="Retirer",command=self.suppr)
        self.suppr_choice.grid(row=2,column=1,columnspan=2)
        # les sorts que le personnage a déjà
        self.CharSpell_view=ttk.Treeview(self,height=5)
        self.CharSpell_view["columns"]=("0","1","2","3")
        self.CharSpell_view.heading("0",text="Effet")
        self.CharSpell_view.heading("1",text="Description")
        self.CharSpell_view.heading("2",text="Coût")
        self.CharSpell_view.heading("3",text="Eclairs")
        self.CharSpell_view.column("#0",width=110)
        self.CharSpell_view.column("0",width=400)
        self.CharSpell_view.column("1",width=400)
        self.CharSpell_view.column("2",width=50,anchor="c")
        self.CharSpell_view.column("3",width=50,anchor="c")

        # les catégories
        for key in self.elemlist:
            self.CharSpell_view.insert("","end",key,text=key)

            for kkey in self.subcateglist:
                self.CharSpell_view.insert(key,"end",key+kkey,text=kkey)


        self.CharSpell_view.grid(row=1,column=0,rowspan=3,pady="8p",sticky="w")
        self.CharSpell_view.bind("<Button-1>",func=self.select_charspell)


        Label(self,text="Sorts disponibles").grid(row=4,column=0,sticky="w",padx="4p")
        self.transfer_choice=Button(self,text="Prendre",command=self.transfer_spell)
        self.transfer_choice.grid(row=5,column=1,columnspan=2)
        # les sorts qui existent
        self.Spell_view=ttk.Treeview(self,height=5)
        self.Spell_view["columns"]=("0","1","2")
        self.Spell_view.heading("0",text="Effet")
        self.Spell_view.heading("1",text="Description")
        self.Spell_view.heading("2",text="Coût")
        self.Spell_view.column("#0",width=110)
        self.Spell_view.column("0",width=400)
        self.Spell_view.column("1",width=400)
        self.Spell_view.column("2",width=50)
        # les catégories
        for key in self.elemlist:
            self.Spell_view.insert("","end",key,text=key)

            for kkey in self.subcateglist:
                self.Spell_view.insert(key,"end",key+kkey,text=kkey)


        self.Spell_view.grid(row=5,column=0,pady="8p",sticky="w")
        self.Spell_view.bind("<Button-1>",func=self.select_spell)

        # la FUUUU-SIOOOON de sorts

        ttk.Separator(self,orient="horizontal").grid(row=6,column=0,columnspan=4,sticky="we",pady='4p',padx="4p")
        self.fusionFrame=Frame(self)
        self.fusionFrame.grid(row=7,column=0,columnspan=4,sticky="w")
        Label(self.fusionFrame,text="Sort spécial").grid(row=0,column=0,sticky="w") # ,font=("TkDefault","10")
        Label(self.fusionFrame,text="Elément").grid(row=1,column=0,sticky="w")
        Label(self.fusionFrame,text="Sous-catégorie").grid(row=1,column=1,sticky="w")
        Label(self.fusionFrame,text="Nom").grid(row=1,column=2,sticky="w")
        Label(self.fusionFrame,text="Coût").grid(row=1,column=3,sticky="w")
        Label(self.fusionFrame,text="Effets").grid(row=3,column=0,sticky="w")
        Label(self.fusionFrame,text="Description").grid(row=3,column=2,sticky="w")
        self.Name_var=StringVar()
        self.Cost_var=IntVar()
        self.Elem_entry=ttk.Combobox(self.fusionFrame,values=self.elemlist)
        self.Elem_entry.current(0)
        self.Subcateg_entry=ttk.Combobox(self.fusionFrame,values=self.subcateglist)
        self.Subcateg_entry.current(0)
        self.Name_entry=Entry(self.fusionFrame,textvariable=self.Name_var)
        self.Cost_entry=Entry(self.fusionFrame,textvariable=self.Cost_var)
        self.Effect_entry=Text(self.fusionFrame,width=50,height=5)
        self.Description_entry=Text(self.fusionFrame,width=50,height=5)
        self.Special_register=Button(self.fusionFrame,text="Enregistrer",command=self.special_create)

        self.Elem_entry.grid(row=2,column=0,sticky="w",padx='4p')
        self.Subcateg_entry.grid(row=2,column=1,sticky="w",padx='4p')
        self.Name_entry.grid(row=2,column=2,sticky="w",padx='4p')
        self.Cost_entry.grid(row=2,column=3,padx="4p",sticky="w")
        self.Effect_entry.grid(row=4,column=0,padx='4p',columnspan=2,sticky="w")
        self.Description_entry.grid(row=4,column=2,padx='4p',columnspan=2,sticky="w")
        self.Special_register.grid(row=2,column=4,rowspan=3,padx="4p")


        self.bind("<Visibility>",func=self.refresh)

    def special_create(self):
        if self.Name_var.get() and self.Cost_var.get():
            new_spell=pc.Spell(self.Elem_entry.get(),self.Subcateg_entry.get(),self.Name_var.get(),self.Effect_entry.get(0.0,"end"),self.Description_entry.get(0.0,"end"),self.Cost_var.get())
            self.master.master.selectedchar.spells[new_spell]=0

            self.spells_list.append(new_spell)
            self.CharSpell_view.insert(new_spell.elem+new_spell.subcateg,"end",(len(self.spells_list)),text=new_spell.name,values=[new_spell.effect,new_spell.description,new_spell.cost,0])


    def transfer_spell(self):
        """ Méthode pour attribuer le sort sélectionné au personnage """
        if self.selected_item:
            new_spell = self.master.master.master.spelllist[self.selected_item-1].copy()
            self.master.master.selectedchar.spells[new_spell]=0

            self.spells_list.append(new_spell)
            self.CharSpell_view.insert(new_spell.elem+new_spell.subcateg,"end",(len(self.spells_list)),text=new_spell.name,values=[new_spell.effect,new_spell.description,new_spell.cost,0])

    def refresh(self,event=None):
        self.refresh_general()
        self.refresh_char()
        self.suppr_choice["state"]="disabled"
        self.transfer_choice["state"]="disabled"
        self.plus_lightning["state"]="disabled"
        self.min_lightning["state"]="disabled"

    def refresh_char(self):
        """ Méthode qui rafraîchit la liste des sorts du personnage """

        self.spells_list=[]

        for key in self.elemlist:
            for kkey in self.subcateglist:
                for i in self.CharSpell_view.get_children(key+kkey):
                    self.CharSpell_view.delete(i)

        if self.master.master.selectedchar.spells:
            i=1
            for key in self.master.master.selectedchar.spells.keys():
                self.spells_list.append(key)
                self.CharSpell_view.insert(key.elem+key.subcateg,"end",i,text=key.name,values=[key.effect,key.description,key.cost,self.master.master.selectedchar.spells[key]])

                i+=1



    def refresh_general(self):
        """ Méthode qui rafraîchit la liste générale des sorts """

        for key in self.elemlist:
            for kkey in self.subcateglist:
                for i in self.Spell_view.get_children(key+kkey):
                    self.Spell_view.delete(i)


        if self.master.master.master.spelllist:
            i=1
            for key in self.master.master.master.spelllist:
                self.Spell_view.insert(key.elem+key.subcateg,"end",i,text=key.name,values=[key.effect,key.description,key.cost])

                i+=1

    def select_charspell(self,event):
        """ Méthode qui est appelée quand on sélectionne une compétence, pour retirer la supprimer si besoin """
        if self.CharSpell_view.identify_row(event.y):

            try:
                self.selected_charitem=int(self.CharSpell_view.identify_row(event.y))
                self.suppr_choice["state"]="normal"
                self.plus_lightning["state"]="normal"
                self.min_lightning["state"]="normal"

            except:
                self.selected_charitem=None
                self.suppr_choice["state"]="disabled"
                self.plus_lightning["state"]="disabled"
                self.min_lightning["state"]="disabled"

        else:
            self.selected_charitem=None
            self.suppr_choice["state"]="disabled"
            self.plus_lightning["state"]="disabled"
            self.min_lightning["state"]="disabled"

    def select_spell(self,event):
        """ Méthode qui est appelée quand on sélectionne une compétence, pour la transférer si besoin """
        if self.Spell_view.identify_row(event.y):

            try:
                self.selected_item=int(self.Spell_view.identify_row(event.y))
                self.transfer_choice["state"]="normal"

            except:
                self.selected_item=None
                self.transfer_choice["state"]="disabled"

        else:
            self.selected_item=None
            self.transfer_choice["state"]="disabled"


    def suppr(self):
        """ Méthode qui supprime la compétence sélectionnée """
        if type(self.selected_charitem)==int:
            self.master.master.spelllist.pop(self.selected_item-1)
            self.refresh_char()
            self.selected_charitem=None
            self.suppr_choice["state"]="disabled"

    def modif_lightning(self,number):
        """ Méthode qui permet de consommer des éclairs """
        if self.selected_charitem:
            selected_spell=self.spells_list[self.selected_charitem-1]
            self.master.master.selectedchar.use_lightning(selected_spell,number)
            self.refresh_char()
            self.master.CharCF.BNDL.ETH.refresh()

    def grid(self,**kw):
        Frame.grid(self,**kw)
        self.refresh()




## Fenêtre pricipale




class CharMenu(Menu):
    """ Widget menu permettant d'accéder aux personnages ou la suppresion de personnage """

    def __init__(self,master):
        Menu.__init__(self,master)
        self.submenu_1=Menu(self,tearoff=0)
        self.add_cascade(label="Changer de perso",menu=self.submenu_1)
        self.submenu_1.add_command(label="Créer",command=self.goto_create)
        self.submenu_1.add_separator()
        for i in range(len(self.master.characlist)):
            self.submenu_1.add_command(label=self.master.characlist[i].name,command=partial(self.goto_other,i))
        self.add_separator()
        self.add_command(label="Supprimer",command=self.goto_suppr)
        self.add_separator()
        self.add_command(label="Compétences",command=self.goto_compet)
        self.add_separator()
        self.add_command(label="Sorts",command=self.goto_spell)

    def refresh(self):
        """ fonction pour rafraîchir la liste des personnages disponibles """

        for i in range(2,2+len(self.submenu_1._tclCommands[1:])): # le séparateur occupe l'indice 1
            self.submenu_1.delete(self.submenu_1.entrycget(i,"label"))

        for i in range(len(self.master.characlist)):
            self.submenu_1.add_command(label=self.master.characlist[i].name,command=partial(self.goto_other,i))


    def goto_create(self):
        """ Renvoie dans l'environnement de création de personnage"""
        for i in self.master.grid_slaves():
            i.grid_forget()
        self.master.children["!homeframe"].grid(row=0,column=0)
        self.master.children["!charcframe"].grid(row=0,column=1)

    def goto_other(self,number):
        """ Emène vers la page caractéristique de l'autre personnage selectionné """

        for i in self.master.grid_slaves():
            i.grid_forget()

        self.master.CDF.selectedchar=self.master.characlist[number]
        self.master.children['!chardframe'].grid(row=0,column=0)

    def goto_suppr(self):
        """ Emmène vers la page de suppresion des personnages """
        for i in self.master.grid_slaves():
            i.grid_forget()
        self.master.children["!charsframe"].grid(row=0,column=0)

    def goto_compet(self):
        for i in self.master.grid_slaves():
            i.grid_forget()
        self.master.children["!competcreatorframe"].grid(row=0,column=0)

    def goto_spell(self):
        for i in self.master.grid_slaves():
            i.grid_forget()
        self.master.children["!spellcreatorframe"].grid(row=0,column=0)



class UI_Window(Tk):
    """ Fenêtre de base, ne contient que le nécessaire """

    def __init__(self):
        Tk.__init__(self)
        self.titre="Solo Leveling"
        self.title(self.titre)
        with open("characters","rb") as fichier:
            self.characlist = pk.Unpickler(fichier).load()

        with open("competences","rb") as fichier:
            self.competlist = pk.Unpickler(fichier).load()

        with open("spells","rb") as fichier:
            self.spelllist=pk.Unpickler(fichier).load()


        self.Menubar=CharMenu(self)
        self.HF=HomeFrame(self)
        self.HF.grid(row=0,column=0)
        self.CCF=CharCFrame(self)
        self.CDF=CharDFrame(self)
        self.CSF=CharSFrame(self)
        self.OCF=ObjCreatorFrame(self)
        self.CompCF=CompetCreatorFrame(self)
        self.SpellCF=SpellCreatorFrame(self)
        self.configure(menu=self.Menubar)
        self.protocol("WM_DELETE_WINDOW",self.destroy)

    def destroy(self):
        """ Fonction de destruction de la fenêtre, on sauvegarde les personnages avant de la détruire """
        with open("characters","wb") as fichier:
            pk.Pickler(fichier).dump(self.characlist) # on enregistre la liste

        with open("competences","wb") as fichier:
            pk.Pickler(fichier).dump(self.competlist)

        with open("spells","wb") as fichier:
            pk.Pickler(fichier).dump(self.spelllist)
        Tk.destroy(self)
        
    
        
