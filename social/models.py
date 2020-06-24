from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, RegexValidator


# Create your models here.


class MyProfile(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    age = models.IntegerField(default=0, validators=[MinValueValidator(18)])
    gender = models.CharField(max_length=20, default="None",
                              choices=(("female", "FEMALE"), ("male", "MALE"), ("other", "OTHER")))
    YOE = models.IntegerField(default=0, null=True)
    YOP = models.IntegerField(default=0, null=True)
    YOJ = models.IntegerField(default=0, null=True)
    grduper = models.IntegerField(default=0, null=True)
    interper = models.IntegerField(default=0, null=True)
    highper = models.IntegerField(default=0, null=True)
    address = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, default="None", choices=(
        ("entrepreneur", "ENTREPRENEUR"), ("gov employee", "GOV EMPLOYEE"), ("private sector", "PRIVATE SECTER"),
        ("higher studies", "HIGHER STUDIES"), ("searching job", "SEARCHING JOB")))
    ptype = models.CharField(max_length=20, default="None",
                             choices=(("alumni", "Alumni"), ("student", "STUDENT"), ("staff", "STAFF")))
    course = models.CharField(max_length=20, default="None", choices=(
        ("b.Tech", "B.TECH"), ("m.Tech", "M.TECH"), ("phd", "PHD"), ("bca", "BCA"), ("mca", "MCA")))
    branch = models.CharField(max_length=20, default="None", choices=(
        ("cse", "CSE"), ("ece", "ECE"), ("me", "ME"), ("ee", "EE"), ("civil", "CIVIL"), ("che", "CHE")))
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=15, null=True, blank=True)
    description = models.TextField(default="none", null=True, blank=True)
    pic = models.ImageField(upload_to="images\\", null=True)
    myresume = models.FileField(upload_to="images\\", null=True, blank=True)
    def __str__(self):
        return "%s" % self.user

    # Resize the image
    # def save(self):
    #   super().save()


#
#       pic = Image.open(self.image.path)
#      # To resize the profile image
#     if image.height > 400 or image.width > 400:
#        output_size = (400, 400)
#       image.thumbnail(output_size)
#      image.save(self.image.path)


class MyPost(models.Model):
    pic = models.ImageField(upload_to="images\\", null=True)
    subject = models.CharField(max_length=200)
    msg = models.TextField(null=True, blank=True)
    cr_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return "%s" % self.subject


class PostComment(models.Model):
    post = models.ForeignKey(to=MyPost, on_delete=CASCADE)
    msg = models.TextField()
    commented_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE)
    cr_date = models.DateTimeField(auto_now_add=True)
    flag = models.CharField(max_length=20, null=True, blank=True,
                            choices=(("racist", "racist"), ("abbusing", "abbusing")))

    def __str__(self):
        return "%s" % self.msg


class PostLike(models.Model):
    post = models.ForeignKey(to=MyPost, on_delete=CASCADE)
    liked_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE)
    cr_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.liked_by


class FollowUser(models.Model):
    profile = models.ForeignKey(to=MyProfile, on_delete=CASCADE, related_name="profile")
    followed_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE, related_name="followed_by")

    def __str__(self):
        return "%s is followed by %s" % (self.profile, self.followed_by)


class Feedback(models.Model):
    feed_name = models.CharField(max_length=200)
    suggetion = models.TextField(max_length=200)
    feedback = models.IntegerField()
    feed_phone_no = models.CharField( max_length=15, null=True,
                                     blank=True)
    feed_email = models.EmailField(max_length=200)
    feed_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "%s" % self.feed_email


class Question(models.Model):
    subject = models.CharField(max_length=100)
    msg = models.TextField()
    cr_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=CASCADE, null=True, blank=True)

class Notice(models.Model):
    subject = models.CharField(max_length=100)
    msg = models.TextField()
    cr_date = models.DateTimeField(auto_now_add = True)
    pic = models.ImageField(upload_to="images\\", null=True)