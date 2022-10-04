"""
    tanggal: 03 Oktober 2022, 19:11:59 WIB
    magnitudo: 4.1
    kedalaman: 2 km
    lokasi: 5.35 LS - 102.57 BT
    pusat gempa: Pusat gempa berada di laut 33 km tenggara Enggano
    dirasakan: Dirasakan (Skala MMI): II Enggano
"""


def ekstraksi_data():
    hasil = dict ()
    hasil["tanggal"] = "03 Oktober 2022"
    hasil["waktu"] = "19:11:59 WIB"
    hasil["magnitudo"] = "4.1"
    hasil["kedalaman"] = "2 km"
    hasil["lokasi"] = {"ls": 5.35,"bt" : 102.57 }
    hasil["pusat"] = "Pusat gempa berada di laut 33 km tenggara Enggano"
    hasil["dirasakan"] = "Dirasakan (Skala MMI): II Enggano"
    return hasil

def tampilkan_data(result):
    print("Gempa terakhir berdasarkan BMKG")
    print(f"Tanggal:  {result['tanggal']}")
    print(f"Waktu:  {result['waktu']}")
    print(f"magnitudo:  {result['magnitudo']}")
    print(f"kedalaman:  {result['kedalaman']}")
    print(f"lokasi:  ls= {result['lokasi']['ls']}  bt= {result['lokasi']['bt']}")
    print(f"pusat:  {result['pusat']}")
    print(f"dirasakan:  {result['dirasakan']}")

