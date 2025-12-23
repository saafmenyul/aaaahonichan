import requests
from django.shortcuts import render


def get_breeds_list():
    """
    Получает список всех пород собак через GET-запрос.
    Возвращает пронумерованный список пород.
    """
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    data = response.json()
    
    # Извлекаем все породы из словаря
    breeds = []
    for breed, subbreeds in data['message'].items():
        if subbreeds:
            # Если есть подпороды, добавляем их
            for subbreed in subbreeds:
                breeds.append(f"{breed}-{subbreed}")
        else:
            breeds.append(breed)
    
    # Сортируем и нумеруем
    breeds.sort()
    numbered_breeds = [(i + 1, breed) for i, breed in enumerate(breeds)]
    
    return numbered_breeds


def index(request):
    """
    Главная страница: показывает список пород и форму для ввода.
    """
    breeds = get_breeds_list()
    return render(request, 'index.html', {'breeds': breeds})


def show_images(request):
    """
    Получает и отображает изображения собак выбранных пород.
    """
    if request.method == 'POST':
        # Получаем введенные породы через запятую
        breeds_input = request.POST.get('breeds', '').strip()
        breeds_list = [b.strip() for b in breeds_input.split(',') if b.strip()]
        
        # Получаем изображения для каждой породы
        images_by_breed = {}
        for breed in breeds_list:
            try:
                # Формируем URL для API
                if '-' in breed:
                    # Подпорода (например, afghan-hound)
                    main_breed, subbreed = breed.split('-', 1)
                    url = f'https://dog.ceo/api/breed/{main_breed}/{subbreed}/images'
                else:
                    url = f'https://dog.ceo/api/breed/{breed}/images'
                
                response = requests.get(url)
                data = response.json()
                
                if data['status'] == 'success':
                    images_by_breed[breed] = data['message'][:10]  # Первые 10 изображений
                else:
                    images_by_breed[breed] = []
            except Exception:
                images_by_breed[breed] = []
        
        return render(request, 'images.html', {'images_by_breed': images_by_breed})
    
    return render(request, 'images.html', {'images_by_breed': {}})

