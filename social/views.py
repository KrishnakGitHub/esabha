import csv

from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from reportlab.pdfgen import canvas
from requests import request


from esabha import settings

from social.models import FollowUser, MyPost, MyProfile, PostLike, Question, Feedback,Notice
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http.response import HttpResponseRedirect, HttpResponse

from social.forms import EmailForm


# Create your views here.


class AllPost(TemplateView):
    template_name = "social/all_post.html"

    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        postList = MyPost.objects.order_by("-cr_date")
        paginator = Paginator(postList, 2)
        page_number = self.request.GET.get('page')
        context["page_obj"] = paginator.get_page(page_number)
        return context;


class HomeView(TemplateView):
    template_name = "social/home.html"

    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        postList = MyPost.objects.order_by("-cr_date")[:5]
        context["mypost_list"] = postList
        context["mypost_count"] = MyPost.objects.count()
        context["notice_list"] = Notice.objects.all()[:5]
        context["notice_count"] = Notice.objects.count()
        context["user_count"] = MyProfile.objects.count()
        context["faq_list"] = Question.objects.all()
        context["feed_list"] = Feedback.objects.all()
        context["feed_count"] = Feedback.objects.count()
        return context;


class AboutView(TemplateView):
    template_name = "social/about.html"


class ContactView(TemplateView):
    template_name = "social/contact.html"


def follow(req, pk):
    user = MyProfile.objects.get(pk=pk)
    FollowUser.objects.create(profile=user, followed_by=req.user.myprofile)
    return HttpResponseRedirect(redirect_to="/social/myprofile")


def unfollow(req, pk):
    user = MyProfile.objects.get(pk=pk)
    FollowUser.objects.filter(profile=user, followed_by=req.user.myprofile).delete()
    return HttpResponseRedirect(redirect_to="/social/myprofile")


def like(req, pk):
    post = MyPost.objects.get(pk=pk)
    PostLike.objects.create(post=post, liked_by=req.user.myprofile)
    return HttpResponseRedirect(redirect_to="/social/home")


def unlike(req, pk):
    post = MyPost.objects.get(pk=pk)
    PostLike.objects.filter(post=post, liked_by=req.user.myprofile).delete()
    return HttpResponseRedirect(redirect_to="/social/home")


@method_decorator(login_required, name="dispatch")
class MyProfileUpdateView(UpdateView):
    model = MyProfile
    fields = ["name", "gender","ptype", "pic","age","phone_no","address","course", "branch","YOP", "YOJ","highper","interper","grduper",
            "status","YOE", "description","myresume"]


@method_decorator(login_required, name="dispatch")
class MyPostCreate(CreateView):
    model = MyPost
    fields = ["subject", "msg", "pic"]

    def form_valid(self, form):
        self.object = form.save()
        self.object.uploaded_by = self.request.user.myprofile
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name="dispatch")
class MyPostListView(ListView):
    model = MyPost

    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        return MyPost.objects.filter(Q(uploaded_by=self.request.user.myprofile)).filter(
            Q(subject__icontains=si) | Q(msg__icontains=si)).order_by("-id");


def Email_Form(request):
    if request.method == 'GET':
        form = EmailForm()
    else:
        form = EmailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            to_email = form.cleaned_data['to_email']
            message = form.cleaned_data['message']
            from_email = settings.EMAIL_HOST_USER
            try:
                send_mail(subject, message, from_email, [to_email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/success')
    return render(request, "social/email.html", {'form': form})


def SendEmail(request):
    html_content = "<a href = 'http://krishpy.pythonanywhere.com/' style='position:absolute;'>Build Your Community</a>" \
                   "<img src='https://gnoptg.dm.files.1drv.com/y4mW604sezd1zDYk4YSPRR_OruFQR0fa5kVlQ36Jerbnn7OZx9LWh21Z6a1zI5l0HAAWNgiP_RaQThrDYGCT2fXnq0EmWFA68cqmh6vW_SI0x3uDH7xXvzlaCS3Aaryh5DU4d0EZousvx0r13fZ21XWK2P3tBBqwFKrzN5PGZx4aXftKn5Mxh5154rDBdSD2EVUF352bcMrL-ryHAARm1nMtA?width=179&height=256&cropmode=none' alt='Build Your Community' width='179' height='256' />"
    host_email = settings.EMAIL_HOST_USER
    email = EmailMessage("Invitation to Join SBSSTC Alumni Association", html_content, host_email,
                         ['krishnakjee2016@gmail.com'])
    email.content_subtype = "html"
    res = email.send()
    return HttpResponse('%s' % res)


@method_decorator(login_required, name="dispatch")
class MyPostDetailView(DetailView):
    model = MyPost


@method_decorator(login_required, name="dispatch")
class MyPostDeleteView(DeleteView):
    model = MyPost


@method_decorator(login_required, name="dispatch")
class MyProfileListView(ListView):
    model = MyProfile

    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        profList = MyProfile.objects.filter(
            Q(name__icontains=si) | Q(address__icontains=si) | Q(gender__icontains=si) | Q(
                status__icontains=si)).order_by("-id");
        for p1 in profList:
            p1.followed = False
            ob = FollowUser.objects.filter(profile=p1, followed_by=self.request.user.myprofile)
            if ob:
                p1.followed = True
        return profList


@method_decorator(login_required, name="dispatch")
class MyProfileDetailView(DetailView):
    model = MyProfile


def getfile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="file.csv"'
    employees = MyProfile.objects.all()
    writer = csv.writer(response)
    for alumni in employees:
        writer.writerow(
            [alumni.name, alumni.gender, alumni.pic, alumni.address, alumni.status, alumni.phone_no, alumni.description,
             alumni.age, alumni.YOE, alumni.YOP, alumni.YOJ, alumni.ptype, alumni.course, alumni.branch, alumni.grduper,
             alumni.interper, alumni.highper])
    return response


def getpdf(request):
    employees = MyProfile.objects.all()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Times-Roman", 55)
    p.drawImage(100, 700, employees)
    p.drawString(100, 700, "hello")
    p.showPage()
    p.save()
    return response


def mail(request):
    subject = "Greetings"
    msg = "Congratulations for your success"
    to = "krishnakjee2016@gmail.com"
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if (res == 1):
        msg = "Mail Sent Successfuly"
    else:
        msg = "Mail could not sent"
    return HttpResponse(msg)


def thanks(request):
    return render(request, 'social/thanks.html')


class Feedback_Form(CreateView):
    model = Feedback
    fields = ["feed_name", "feed_email", "feed_phone_no", "feedback", "suggetion"]


class FeedbackDetailView(TemplateView):
    template_name = "social/feedback_detail.html"

    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        context["feed_obj"] = Feedback.objects.all()
        context["feed_count"] = Feedback.objects.count()
        return context;


@method_decorator(login_required, name="dispatch")
class QuestionCreate(CreateView):
    model = Question
    fields = ["subject", "msg"]

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name='dispatch')
class MyList(TemplateView):
    template_name = "college/mylist.html"

    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        context["notices"] = Notice.objects.all().order_by('-id')[:3];
        context["questions"] = Question.objects.all().order_by('-id')[:3];
        return context;


def successView(request):
    return HttpResponse('Success! Thank you for your message.')


class NoticeListView(ListView):
    model = Notice


@method_decorator(login_required, name="dispatch")
class NoticeDetailView(DetailView):
    model = Notice

# @method_decorator(login_required, name="dispatch")
# class ProfileUpdateView(UpdateView):
#     model = Profile
#     fields = ["branch", "sem", "marks_10", "marks_12", "marks_aggr", "rn", "myimg", "myresume", "skills"]
# "name", "age", "address", "status", "gender", "phone_no", "description", "pic"
# alumni.name,alumni.phone_no,alumni.age,alumni.address,alumni.status,alumni.gender,alumni.description,alumni.pic
# @method_decorator(login_required, name="dispatch")    
# class QuestionCreate(CreateView):
#     model = Question
#     fields = ["subject", "msg"]
#     def form_valid(self, form):
#         self.object = form.save()
#         self.object.user = self.request.user
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())
#     
# @method_decorator(login_required, name="dispatch")    
# class MyList(TemplateView):
#     template_name = "college/mylist.html"
#     def get_context_data(self, **kwargs):
#         context = TemplateView.get_context_data(self, **kwargs)
#         context["notices"] = Notice.objects.order_by("-id")[:3]
#         context["questions"] = Question.objects.order_by("-id")[:3]
#         return context;
# 
#  p = canvas.Canvas(response)
#     p.setFont("Times-Roman", 55)
#     p.drawImage(100,700,employees)
#     p.drawString(100, 700,"hello" )
#     p.showPage()
#     p.save()
#     return response
#     
#
