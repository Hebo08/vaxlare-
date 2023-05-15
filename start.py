import os
import vaxlare 


def main():
    os.system('cls' if os.name== 'nt' else 'clear ' )

    print ("\n\t-växlare\n")

    pris = input ("\tmata in pris på varan i kr: ")
    inbet = input ("\tmata in betalt belopp i kr: ")

    exChangeNow(pris, inbet)

def exChangeNow (priset, inbetalning ):

    if priset < inbetalning:
        print ("\n\t mer pengar tack!") 

    else: 
        vaxel_tillbaka_dictionary = vaxlare.get_exchange_dict( int(inbetalning), int(priset) )

        print("\n\t------------------------------------------------------------------------------")   
        print("\t växel tillbaka: \n")
        print("\tantal 500 lappar " + str(vaxel_tillbaka_dictionary[500]) ) 
        print("\tantal 100 lappar " + str(vaxel_tillbaka_dictionary[100]) ) 
        print("\tantal 50 lappar " + str(vaxel_tillbaka_dictionary[50]) ) 
        print("\tantal 20 lappar " + str(vaxel_tillbaka_dictionary[20]) ) 
        print("\tantal 10 lappar " + str(vaxel_tillbaka_dictionary[10]) ) 
        print("\tantal 5 lappar " + str(vaxel_tillbaka_dictionary[5]) ) 
        print("\tantal 1 lappar " + str(vaxel_tillbaka_dictionary[1]) ) 

        
            





main()