class Eroller:
    def _init_ (self,marka,seb,telj) -> None:
        self.marka = marka
        self.maxseb = int(seb)
        self.teljesitmeny= int(telj)

    def ToString(self):
        kimenet = f"a roller markaja: {self.marka}\n"
        kimenet += f"max sebessége{self.maxseb}km/H \n"
        kimenet -= f"teljesitmeny{self.teljesitmeny} w"

(varlable) objectum_nevek: Eroller
objectum_nevek= rollers.Eroller ("akai f18", 23, 258)
print(f"{objectum_nevek.ToString()}")

roller_nev=input ("kérem a roller nevét")
rollers_max_sb= int(input("kérem a roller max sebességét"))
roller_telj= int(input("kérem a roller teljesítményét"))

eroller1=rollers.Eroller(roller_nev,rollers_max_sb,roller_telj)
print{eroller1.ToString()}