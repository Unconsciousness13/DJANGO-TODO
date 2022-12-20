from django.db import models
from django.conf import settings

class UsersGroup(models.Model):
    name = models.CharField(max_length=55, unique=True)
    users = models.CharField(max_length=55, blank=True)
    
    
    def __str__(self) -> str:
        return self.name

class FriendList(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    
    def __str__(self):
        return  self.user.user_name
    
    def add_friend(self,account):
        if not account in self.friends.all():
            self.friends.add(account)

    def remove_friend(self,account):
        if  account in self.friends.all():
            self.friends.remove(account)
    
    def unfriend(self,removee):
        remover_friends_list = self
        remover_friends_list.remove_friend(removee)
        friends_list = FriendList.objects.get(user=removee)
        friends_list.remove_friend(self.user)
        
    def is_mutual_friend(self,friend):
        if friend in self.friends.all():
            return True
        return False
    
class FriendRequest(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender")
    reciever = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reciever")
    is_active = models.BooleanField(blank=True, null=False, default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.sender.user_name
    
    def accept(self):
        reciever_friends_list = FriendList.objects.get(user=self.reciever)
        if reciever_friends_list:
            reciever_friends_list.add_friend(self.sender)
            sender_friend_list = FriendList.objects.get(user=self.sender)
            if sender_friend_list:
                sender_friend_list.add_friend(self.reciever)
                self.is_active = False
                self.save()
    
    def decline(self):
        self.is_active = False
        self.save()
        
    def cancel(self):
        self.is_active = False
        self.save()