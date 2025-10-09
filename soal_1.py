# SOAL 1

score = float(input('Perfomance Score: '))
if score >= 90:
    hasil = "Excelent Perfomance"
elif score >= 80:
    hasil = "Very Good Performance"
elif score >= 70:
    hasil = "Good Performance"
elif score >= 60:
    hasil = "average Performance"
else :
    hasil = " Improve Your performance"

print(hasil)