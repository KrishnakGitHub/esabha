from django.contrib import admin
from social.models import FollowUser, MyPost, MyProfile, PostComment, PostLike, Feedback, Question, Notice
from django.contrib.admin.options import ModelAdmin


class FollowUserAdmin(ModelAdmin):
    list_display = ["profile", "followed_by"]
    search_fields = ["profile", "followed_by"]
    list_filter = ["profile", "followed_by"]


admin.site.register(FollowUser, FollowUserAdmin)


class MyPostAdmin(ModelAdmin):
    list_display = ["subject", "cr_date", "uploaded_by"]
    search_fields = ["subject", "msg", "uploaded_by"]
    list_filter = ["cr_date", "uploaded_by"]


admin.site.register(MyPost, MyPostAdmin)


class MyProfileAdmin(ModelAdmin):
    list_display = ["name"]
    search_fields = ["name", "status", "phone_no"]
    list_filter = ["status", "gender"]


admin.site.register(MyProfile, MyProfileAdmin)


class PostCommentAdmin(ModelAdmin):
    list_display = ["post", "msg"]
    search_fields = ["msg", "post", "commented_by"]
    list_filter = ["cr_date", "flag"]


admin.site.register(PostComment, PostCommentAdmin)


class PostLikeAdmin(ModelAdmin):
    list_display = ["post", "liked_by"]
    search_fields = ["post", "liked_by"]
    list_filter = ["cr_date"]


admin.site.register(PostLike, PostLikeAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('feed_name', 'feedback')
    list_filter = ('feed_name',)
    search_fields = ('feed_name', 'feed_email',)

    class Meta:
        model = Feedback


admin.site.register(Feedback, FeedbackAdmin)


class QuestionAdmin(ModelAdmin):
    list_display = ["subject", "cr_date"]
    search_fields = ["subject", "msg"]
    list_filter = ["cr_date", "user"]


admin.site.register(Question, QuestionAdmin)


class NoticeAdmin(ModelAdmin):
    list_display = ["subject", "cr_date"]
    search_fields = ["subject", "msg"]
    list_filter = ["cr_date"]


admin.site.register(Notice, NoticeAdmin)
