from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
from tours.data import title, subtitle, description, departures, tours
from random import sample


def main_view(request):
    tours_number = sample(range(1, 17), 6)
    tour_six = {}
    for tour in tours_number:
        tour_six.update({tour: tours[tour]})

    return render(request, 'tours/index.html', context={'title': title,
                                                        'subtitle': subtitle,
                                                        'description': description,
                                                        'departures': departures,
                                                        'tour_six': tour_six})


def departure_view(request, departure):
    departure_count = sum(1 for tour in tours.values() if tour["departure"] == departure)

    price_max = max(int(tour["price"]) for tour in tours.values() if tour["departure"] == departure)
    price_min = min(int(tour["price"]) for tour in tours.values() if tour["departure"] == departure)
    nights_max = max(int(tour["nights"]) for tour in tours.values() if tour["departure"] == departure)
    nights_min = min(int(tour["nights"]) for tour in tours.values() if tour["departure"] == departure)

    return render(request, 'tours/departure.html', context={'departures': departures,
                                                            "tours": tours,
                                                            "departure": departure,
                                                            'departure_list': departures[departure],
                                                            'departure_count': departure_count,
                                                            'price_max': price_max,
                                                            'price_min': price_min,
                                                            'nights_max': nights_max,
                                                            'nights_min': nights_min})


def tour_view(request, id):
    return render(request, 'tours/tour.html', context={'tours': tours[id],
                                                       'departure': departures[tours[id]["departure"]],
                                                       'departures': departures,
                                                       'stars': int(tours[id]["stars"]) * "★"})


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ошибка сервера!')


def custom_handler500(request):
    return HttpResponseServerError('Ресурс не найден!')
