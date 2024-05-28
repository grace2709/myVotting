from django.shortcuts import render
from django.views.generic import CreateView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from  .models import Poll,Choice
# Create your views here.


class CreatePoll(LoginRequiredMixin,CreateView):
    # def get(self,request):
    #     return render(request,"app/create_poll.html")
    model = Poll
    template_name = "app/create_poll.html"
    fields = ['name','description','owner']
    success_url = "login "
    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.save()
        return super().form_valid(form)




class AddChoiceView(LoginRequiredMixin,CreateView):
    model= Choice
    fields = ['name']
    template_name="app/add_choice.html"
    success_url = "poll/"


    def form_valid(self,form):
        form.instance.poll = Poll.objects.get(id=self.kwargs['poll_id'])
        return super().form_valid(form)

class   VoteView(LoginRequiredMixin,View):
    def get(self,request,poll_id):
        poll = Poll.objects.get(id=poll_id)
        choices = poll.choice_set.all()
        return render(request,"app/vote.html",{"poll":poll,"choices":choices})

