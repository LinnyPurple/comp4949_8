from django.http import Http404
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
import pandas as pd
import pickle
import sklearn  # You must perform a pip install.


# Create your views here.
def home_page_view(request):
    return render(request, 'home.html', {
        'my_numbers': [1, 2, 3, 4, 5, 6],
        'first_name': 'George',
        'last_name': 'Rozitis'
    })


def about_page_view(request):
    return render(request, 'about.html')


def george_page_view(request):
    return render(request, 'george.html')


def home_post(request):
    # Use request object to extract choice.

    choice = -999
    gmat = -999

    try:
        # Extract value from request object by control name.
        current_choice = request.POST['choice']
        gmat_str = request.POST['gmat']

        # Crude debugging effort.
        print("*** Years work experience: " + str(current_choice))
        choice = int(current_choice)
        gmat = float(gmat_str)
    # Enters 'except' block if integer cannot be created.
    except:
        return render(request, 'home.html', {
            'error_message': '*** The data submitted is invalid. Please try again.',
            'my_numbers': [1, 2, 3, 4, 5, 6]})
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', kwargs={'choice': choice,
                                                               'gmat': gmat}))


def results(request, choice, gmat):
    print("*** Inside results()")
    # load saved model
    with open('../model_pkl', 'rb') as f:
        loaded_model = pickle.load(f)

    # Create a single prediction.
    single_sample_df = pd.DataFrame(columns=['gmat', 'work_experience'])

    work_experience = float(choice)
    print("*** GMAT Score: " + str(gmat))
    print("*** Years experience: " + str(work_experience))
    single_sample_df = single_sample_df.append({'gmat': gmat,
                                                'work_experience': work_experience},
                                               ignore_index=True)

    single_prediction = loaded_model.predict(single_sample_df)

    print("Single prediction: " + str(single_prediction))

    return render(request, 'results.html', {'choice': work_experience, 'gmat': gmat,
                                            'prediction': single_prediction})


