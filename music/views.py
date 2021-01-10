# from django.http import Http404
# from django.http import HttpResponse
# from django.shortcuts import render , get_object_or_404
# from .models import Album,song
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from django.urls import reverse_lazy
from .models import Album, song
from .forms import UserForm

class IndexView(generic.ListView):
    template_name = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()

class SongView(generic.ListView):
    template_name = 'music/songs.html'

    def get_queryset(self):
        return song.objects.all()

# class DetailView(generic.DetailView):
#     model = Album
#     template_name = 'music/detail.html'

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'
    queryset = Album.objects.all()

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['songs'] = song.objects.filter(album = self.kwargs.get('pk'))
        print(context['songs'])
        # And so on for more models
        return context


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']  

class SongCreate(CreateView):
    model = song
    fields = ['album','file_type','song_title','is_favorite']  

class SongUpdate(UpdateView):
    model = song
    fields = ['album','file_type','song_title','is_favorite']  

class SongDelete(DeleteView):
    model = song
    success_url = reverse_lazy('music:songList')

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo'] 

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit = False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objetcs if credentials are correct
            user = authenticate(username=username ,password=password)
            if user is not None :
                if user.is_active:
                    login(request , user)
                    return redirect('music:index')


        return render(request, self, template_name, {'form' : form})            

# def index(request):
#     all_albums = Album.objects.all()
    
#     context  = {
#         'all_albums' : all_albums,
#     }
#     return render(request , 'music/index.html', context)

# def detail(request, album_id):
#     album = get_object_or_404(Album, pk = album_id)
#     return render(request , 'music/detail.html', {
#         'album' : album,
#     })

# def favorite(request, album_id):
#     album = get_object_or_404(Album, pk = album_id)
#     try:
#         selected_song = album.song_set.get(pk = request.POST['song'])
#     except (KeyError , song.DoesNotExist):
#         return render(request , 'music/detail.html', {
#         'album' : album,
#         'error_message' : "You did not select a valid song"
#     })
#     else:
#         selected_song.is_favorite = True
#         selected_song.save()
#         return render(request , 'music/detail.html', {
#         'album' : album
#     })
    