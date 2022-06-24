import pandas as pd


def readCSV(path, separ):
    """
    legge un file .csv e lo incapsula in un dataframe pandas
    :param path: percorso file .csv da leggere
    :param separ: separatore (carattere)
    :return: dataframe contenente i dati estratti
    """
    data = pd.read_csv(path, sep=separ, error_bad_lines=False)
    return data
