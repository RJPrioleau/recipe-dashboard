from django.shortcuts import render


def home(request):
    dashboard = {
        "last_cooked_meal": {
            "name": "Chicken Alfredo",
            "cooked_on": "July 21, 2026",
        },
        "suggested_meal": {
            "name": "Beef Tacos with Spanish Rice",
            "last_cooked_on": "June 30, 2026",
            "reason": "This meal has not been cooked recently and fits a familiar weeknight dinner.",
        },
    }

    return render(request, "dashboard/home.html", {"dashboard": dashboard})
