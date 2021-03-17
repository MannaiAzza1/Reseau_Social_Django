from django.shortcuts import render
from .models import Profile, Relationship
from .forms import ProfileModelForm
from django.views.generic import ListView
from django.contrib.auth.models import User

# Create your views here.
def my_profile_view(request):
    profile=Profile.objects.get(user=request.user)
    form = ProfileModelForm(request.POST or None , request.FILES or None , instance=profile)
    confirm=False
    if(request.method == "POST"):
        if form.is_valid():
            form.save()
            confirm = True
    context={
        'profile': profile,
        'form' : form,
        'confirm':confirm,
    }
    return render(request,'profiles/myprofile.html',context)
def invates_received_view(request):
    profile=Profile.objects.get(user=request.user)
    qs = Relationship.objects.invatations_received(profile)

    context = {
        'qs' : qs, 
    }

    return render(request, 'profiles/my_invites.html', context)


def invite_profile_list_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles_to_invite(user)

    context = {
        'qs' : qs, 
    }
    return render(request, 'profiles/to_invite_List.html', context)    

def profile_list_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles(user)

    context = {
        'qs' : qs, 
    }
    return render(request, 'profiles/profile_List.html', context)

class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_List.html'
    #context_object_name = 'qs'

    def get_queryset(self):
        qs = Profile.objects.get_all_profiles(self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username__iexact=self.request.user)
        profile = Profile.objects.get(user=user)
        context['profile'] = profile
        rel_r = Relationship.objects.filter(sender=profile)
        rel_s = Relationship.objects.filter(reciever=profile)
        rel_reciever = []
        rel_sender = []
        for item in rel_r:
            rel_reciever.append(item.reciever.user)
        for item in rel_s:
            rel_reciever.append(item.sender.user)

        context['rel_reciever'] = rel_reciever
        context['rel_sender'] = rel_sender
        context['is_empty'] = False
        if len(self.get_queryset()) == 0:
              context['is_empty'] = True

        return context    


