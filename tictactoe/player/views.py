from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from gameplay.models import Game
from .forms import InvitationForm
from .models import Invitation
# Create your views here.


@login_required
def home(request):
    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.active()

    return render(request, "player/home.html",
                  {'games': active_games})


@login_required
def new_invitation(request):
    if request.method == "POST":
        # sets the from_user field to current user
        invitation = Invitation(from_user=request.user)
        # contains the users data, provides extra data with instance
        form = InvitationForm(instance=invitation, data=request.POST)
        if form.is_valid:  # check if all fields have been filled
            form.save()  # saves a new row in db
            return redirect('player_home')  # redirects the player home
    else:  # if its a get method
        form = InvitationForm()
    return render(request, "player/new_invitation_form.html", {'form': form})
