"""
Funzione per caricare i dati dei quasar DR7 dal file locale.
Il file dr7qso.dat.gz deve essere nella cartella astroML_data.
"""

import numpy as np
import gzip
import os

def load_dr7_quasar(data_file=None):
    """
    Carica i dati dei quasar DR7 dal file .dat.gz locale.
    
    Returns:
        numpy structured array con i dati dei quasar
    """
    if data_file is None:
        data_file = os.path.expanduser('~/astroML_data/dr7qso.dat.gz')
    
    # Definisci i nomi delle colonne principali
    # Basato sulla struttura del catalogo DR7
    dtype = [
        ('sdssname', 'U20'),   # SDSS name
        ('ra', 'f8'),          # Right Ascension
        ('dec', 'f8'),         # Declination
        ('redshift', 'f8'),    # Redshift
        ('mag_u', 'f8'),       # u magnitude
        ('mag_g', 'f8'),       # g magnitude
        ('mag_r', 'f8'),       # r magnitude
        ('mag_i', 'f8'),       # i magnitude
        ('mag_z', 'f8'),       # z magnitude
    ]
    
    redshifts = []
    ras = []
    decs = []
    
    # Leggi il file gzippato
    with gzip.open(data_file, 'rt') as f:
        for line in f:
            parts = line.split()
            if len(parts) >= 4:
                try:
                    ra = float(parts[1])
                    dec = float(parts[2])
                    z_val = float(parts[3])
                    redshifts.append(z_val)
                    ras.append(ra)
                    decs.append(dec)
                except (ValueError, IndexError):
                    continue
    
    # Crea un structured array simile a quello di astroML
    n = len(redshifts)
    data = np.zeros(n, dtype=[('ra', 'f8'), ('dec', 'f8'), ('redshift', 'f8')])
    data['ra'] = ras
    data['dec'] = decs
    data['redshift'] = redshifts
    
    return data

if __name__ == "__main__":
    # Test
    data = load_dr7_quasar()
    print(f"Loaded {len(data)} quasars")
    print(f"Redshift range: {data['redshift'].min():.3f} - {data['redshift'].max():.3f}")
