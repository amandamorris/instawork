from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic


from .models import Member

class IndexView(generic.ListView):
    template_name = 'teams/index.html'
    context_object_name = 'members_list'

    """Return the 10 recently added members"""
    def get_queryset(self):
        return Member.objects.order_by('-created')[:10]

class AddView(generic.CreateView):
    model = Member
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'role']
    template_name = 'teams/add.html'

    def get_success_url(self):
            return reverse('teams:index')

class UpdateView(generic.UpdateView):
    model = Member
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'role']
    template_name = 'teams/edit.html'


def delete(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    member.delete()
    return HttpResponseRedirect(reverse('teams:index'))

def save(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    try:
        new_first_name = request.POST.get('first_name')
        new_last_name = request.POST.get('last_name')
        new_phone_number = request.POST.get('phone_number')
        new_email = request.POST.get('email')
        new_role = request.POST.get('role')
    except KeyError:
        return render(request, 'teams/edit.html', {'member': member, 'error_message': "There was an error"})
    else:
        member.first_name = new_first_name
        member.last_name = new_last_name
        member.phone_number = new_phone_number
        member.email = new_email
        member.role = new_role
        member.save()

        return HttpResponseRedirect(reverse('teams:index'))
