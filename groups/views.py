from django.shortcuts import render
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.views import generic as views
from .forms import CreateGroupForm
from django.http import HttpResponse
from .models import FriendRequest, FriendList
from task.models import CustomUser

# Create your views here.
class AddGroupView(LoginRequiredMixin, views.FormView):
    template_name = 'profile/create-group.html'
    form_class = CreateGroupForm
    success_url = '/profile/'
    
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
    

    # def add_user(self, ** kwargs):
    #     context = super().get_context_data(**kwargs)
    #     search_input = self.request.GET.get('search-area') or ''
    #     context['user'] = context['user'].filter(user_name__icontains = search_input)
    #     if search_input:
    #         context['completed_tasks'] = context['tasks'].filter(title__icontains = search_input) or context['tasks'].filter(description__icontains = search_input)
                   
    #     context['search_input'] = search_input
        
    #     return context
    

def friends_list_view(request, *args, **kwargs):
	context = {}
	user = request.user
	if user.is_authenticated:
		user_id = kwargs.get("user_id")
		if user_id:
			try:
				this_user = CustomUser.objects.get(pk=user_id)
				context['this_user'] = this_user
			except CustomUser.DoesNotExist:
				return HttpResponse("That user does not exist.")
			try:
				friend_list = FriendList.objects.get(user=this_user)
			except FriendList.DoesNotExist:
				return HttpResponse(f"Could not find a friends list for {this_user.username}")
			
			# Must be friends to view a friends list
			if user != this_user:
				if not user in friend_list.friends.all():
					return HttpResponse("You must be friends to view their friends list.")
			friends = [] # [(friend1, True), (friend2, False), ...]
			# get the authenticated users friend list
			auth_user_friend_list = FriendList.objects.get(user=user)
			for friend in friend_list.friends.all():
				friends.append((friend, auth_user_friend_list.is_mutual_friend(friend)))
			context['friends'] = friends
	else:		
		return HttpResponse("You must be friends to view their friends list.")
	return render(request, "groups/friends.html", context)


def groups_list_view(request, *args, **kwargs):
    return render(request, 'groups/profile-groups.html', {})