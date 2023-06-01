URL API : http://127.0.0.1:5000/api/v1/predict USE METHOD POST

Berikut, Form yang diperlukan:
1. Location - lokasi, nama kota di Australia
2. MaxTemp - temperatur tertinggi hari itu dalam celcius
3. Rainfall - jumlah curah hujan hari itu dalam mm
4. Evaporation - jumlah evaporasi dalam mm dari Class A pan selama 24 jam sebelum jam 9 pagi hari itu
5. Sunshine - jumlah jam hari itu cerah dengan cahaya matahari
6. WindGustDir - arah kecepatan angin yang paling tinggi selama 24 jam sebelum jam 12 malam hari itu
7. WindGustSpeed - kecepatan angin yang paling tinggi dalam km/jam selama 24 jam sebelum jam 12 malam hari itu
8. WindDir9am - arah angin jam 9 pagi
9. WindDir3pm - arah angin jam 3 sore
10. WindSpeed9am - kecepatan angin jam 9 pagi dalam km/jam dihitung dari rata-rata kecepatan angin 10 menit sebelum jam 3 sore
11. WindSpeed3pm - kecepatan angin jam 3 sore dalam km/jam dihitung dari rata-rata kecepatan angin 10 menit sebelum jam 3 sore
12. Humidity3pm - humiditas jam 3 sore dalam persen
13. Pressure9am - tekanan udara jam 9 pagi dalam hpa
14. Cloud9am - persentase langit yang tertutup awan jam 9 pagi. dihitung dalam oktas, unit ⅛, menghitung berapa unit ⅛ dari langit yang tertutup awan. Jika 0, langit cerah, jika 8, langit sepenuhnya tertutup awan.
15. Cloud3pm - persentase langit yang tertutup awan jam 3 sore
16. RainToday - apakah hari ini hujan: jika curah hujan 24 jam sebelum jam 9 pagi melebihi 1mm, maka nilai ini adalah 1, jika tidak nilai nya 0
17. Year - Tahun
18. Month - Bulan (Dalam Angka)
19. Day - Hari (Dalam Angka)