# SOVELLUS PAINOINDEKSIN JA KEHON RASVAPROSENTIN LASKEMISEEN
# ==========================================================

# Kirjastot ja moduulit
import math

# Määritellään funktio painoindeksin laskentaan


def laske_bmi(paino, pituus):
    """Laskee painoindeksin (BMI)

    Args:
        paino (float): paino (kg)
        pituus (float): pituus (cm)

    Returns:
        float: painoindeksi desimaalin tarkkuudella
    """
    pituus = pituus / 100  # muutetaan pituus metreiksi
    bmi = paino / pituus**2
    bmi = round(bmi, 1)
    return bmi


# Määritellään funktio aikuisen kehonrasvaprosentin laskemiseen
def aikuisen_rasvaprosentti(bmi, ika, sukupuoli):
    """_summary_

    Args:
        bmi (float): painoindeksi
        ika (float): henkilön ikä
        sukupuoli (float): 1 -> mies, 0 -> nainen

    Returns:
        float: kehon rasvaprosentti (aikuinen)
    """
    rasvaprosentti = 1.20 * bmi + 0.23 * ika - 10.8 * sukupuoli - 5.4
    rasvaprosentti = round(rasvaprosentti, 1)
    return rasvaprosentti

# Määritellään funktio lapsen kehonrasvaprosentin laskemiseen


def lapsen_rasvaprosentti(bmi, ika, sukupuoli):
    """Laskee lapsen kehon rasvaprosentin

    Args:
        bmi (float): painoindeksi
        ika (float): ikä
        sukupuoli (float): poika -> 1, tyttö -> 0

    Returns:
        float: kehon rasvaprosentti (lapsi)
    """
    rasvaprosentti = 1.51 * bmi - 0.7 * ika - 3.6 * sukupuoli + 1.4
    rasvaprosentti = round(rasvaprosentti, 1)
    return rasvaprosentti


def usarasvaprosentti_mies(pituus, vyotaron_ymparys, kaulan_ymparys):
    """Laskee miehen rasvaprosentin USA:n armeijan kaavalla

    Args:
        pituus (float): pituus (cm)
        vuotaron_ymparys (float): vatsan ympärysmitta (cm)
        kaulan_ymparys (float): kaulan ympärusmitta (cm)

    Returns:
        float: rasvaprosentti
    """

    # Muutetaan mitat tuumiksi
    tuuma_pituus = pituus / 2.54
    tuuma_vyotaron_ymparys = vyotaron_ymparys / 2.54
    tuuma_kaulan_ymparys = kaulan_ymparys / 2.54

    # Lasketaan rasvaprosentti
    usarprosentti = 86.010 * math.log10(tuuma_vyotaron_ymparys -
                                        tuuma_kaulan_ymparys) - 70.041 * math.log10(tuuma_pituus) + 36.76
    return usarprosentti


def usarasvaprosentti_nainen(pituus, vyotaron_ymparys, lantion_ymparys, kaulan_ymparys):
    """Laskee naisen kehon rasvaprosentin USA:n armeijan kaavalla

    Args:
        pituus (float): pituus (cm)
        vyotaron_ymparys (float): vyötärön ympärysmitta (cm)
        lantion_ymparys (float): lantion ympärysmitta (cm)
        kaulan_ymparys (float): kaulan ympärysmitta (cm)

     Returns:
        float: rasvaprosentti
    """

    tuuma_pituus = pituus / 2.54
    tuuma_vyotaron_ymparys = vyotaron_ymparys / 2.54
    tuuma_lantion_ymparys = lantion_ymparys / 2.54
    tuuma_kaulan_ymparys = kaulan_ymparys / 2.54

    usa_rasvaprosentti = 163.205 * math.log10(tuuma_vyotaron_ymparys + tuuma_lantion_ymparys -
                                               tuuma_kaulan_ymparys) - 97.684 * math.log10(tuuma_pituus) - 78.387
    usa_rasvaprosentti = round(usa_rasvaprosentti, 1)
    return usa_rasvaprosentti


# Suoritetaan seuraavat rivit vain, jos tämä tiedosto on pääohjelma
# Mahdollistaa funktioiden lataamisen toisiin ohjelmiin
# Kun koodi ladataan toiseen tiedostoon,
# if __name__ == "__main__":n alapuolella olevaa koodia ei suoriteta
if __name__ == "__main__":

    # Kysytään käyttäjältä tiedot
    pituus_teksti = input('Kuinka pitkä olet (cm): ')
    paino_teksti = input('Kuinka paljon painat (kg): ')
    ika_teksti = input('Kuinka vanha olet: ')
    sukupuoli_teksti = input('Sukupuoli mies, vastaa 1, nainen vastaa 0: ')
    vyotaron_ymparys_teksti = input('Mikä on vyötärön ympärykseksi (cm): ')
    kaulan_ymparys_teksti = input('Mika on kaulasi ympärysmitta (cm): ')

    # Jos vastaus sukupuolikysymykseen on nainen, kysy lantion mitta
    if sukupuoli_teksti == '0':
        lantion_ymparys_teksti = input('Mikä on lantiosi ympärysmitta (cm): ')

    # Muutetaan vastaukset liukuluvuiksi
    pituus = float(pituus_teksti)
    paino = float(paino_teksti)
    ika = float(ika_teksti)
    sukupuoli = float(sukupuoli_teksti)
    vyotaron_ymparys = float(vyotaron_ymparys_teksti)
    lantion_ymparys = float(lantion_ymparys_teksti)
    kaulan_ymparys = float(kaulan_ymparys_teksti)

    # Lasketaan painoindeksi funktiolla laske_bmi
    oma_bmi = laske_bmi(paino, pituus)

    # Yli 18 vuotiailla käytetään aikuisen kaavaa
    if ika >= 18:
        oma_rasvaprosentti = aikuisen_rasvaprosentti(oma_bmi, ika, sukupuoli)

    # Muussa tapauksessa käytetään lapsen kaavaa
    else:
        oma_rasvaprosentti = lapsen_rasvaprosentti(oma_bmi, ika, sukupuoli)

    print('Painoindeksisi on', oma_bmi,
          'ja kehon rasvaprosentti on', oma_rasvaprosentti)

    # Jos mies laske miehen kaavalla, muussa tapauksessa naisen kaavalla
    if sukupuoli_teksti == '1':
        usa_rasvaprosentti = usarasvaprosentti_mies(
            pituus, vyotaron_ymparys, kaulan_ymparys)

    else:
        usa_rasvaprosentti = usarasvaprosentti_nainen(
            pituus, vyotaron_ymparys, kaulan_ymparys, lantion_ymparys)

    print('USA:n armeijan kaavalla rasvaprosenttisi on', usa_rasvaprosentti)
