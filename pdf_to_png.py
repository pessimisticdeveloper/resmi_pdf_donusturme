from pdf2image import convert_from_path

images = convert_from_path('cv.pdf')


for i, image in enumerate(images):
    filename = f'cv{i+1}.png'
    image.save(filename, 'PNG')
    print(f'Sayfa {i+1} {filename} olarak kaydedildi')
