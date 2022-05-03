def get_aminoacid_mass():
    mass = {
        "G": 57,
        "A": 71,
        "S": 87,
        "P": 97,
        "V": 99,
        "T": 101,
        "C": 103,
        "I": 113,
        "L": 113,
        "N": 114,
        "D": 115,
        "K": 128,
        "Q": 128,
        "E": 129,
        "M": 131,
        "H": 137,
        "F": 147,
        "R": 156,
        "Y": 163,
        "W": 186,
    }
    return mass
  
  def Cyclospectrum(peptide):
    mass = get_aminoacid_mass()
    prosiri_peptide = peptide + peptide[:-1]
    spectrum = []
    spectrum.append(0)
    spectrum.append(sum([mass[x] for x in peptide]))
    for l in range(0,len(peptide)):
        for k in range(1, len(peptide)):
            subpeptide = prosiri_peptide[l : l + k]
            spectrum.append(sum([mass[x] for x in subpeptide]))
    return sorted(spectrum)
  
  rez=Cyclospectrum(peptide)
  " ".join([str(x) for x in rez])
