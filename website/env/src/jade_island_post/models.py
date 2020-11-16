from django.db import models
from django.utils.text import slugify
from django.conf import settings
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from account.models import Account
from django.utils.translation import gettext_lazy as _
from django_comments_xtd.models import XtdComment
from django.urls import reverse
from jade_analytics.views import saveAnalytics
from jade_island_post.categories.jade_island_post_categories import JADE_ISLAND_POST_CATEGORIES
from jade_island_post.categories.events_categories import EVENT_CATEGORIES
from jade_island_post.categories.places_categories import PLACE_CATEGORIES
from jade_island_post.categories.sales_categories import SALE_CATEGORIES
from jade_island_post.categories.job_categories import JOB_CATEGORIES, JOB_TYPE


def upload_location(instance, filename):
    file_path = 'jade_island_post/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.id), title=str(instance.title), filename=filename)
    return file_path


class JadeIslandPost(models.Model):

    title = models.CharField(max_length=200, null=False, blank=False)

    body = models.TextField(max_length=5000, null=True, blank=True)

    post_category = models.CharField(max_length=5, choices=JADE_ISLAND_POST_CATEGORIES.choices,default=JADE_ISLAND_POST_CATEGORIES.UNCATEGORIZED, null=False, blank=False)

    #event or place or shared_moments or jobs or sale (*pickup-location)
    location = models.TextField(max_length=255, null=True, blank=True)

    #event or place or job or sale
    contact = models.TextField(max_length=255, null=True, blank=True)

    # job
    job_start_date = models.DateTimeField(null=True, blank=True)

    # sale
    sale_item_price_rmb = models.PositiveIntegerField(
        default=0, null=True, blank=True)

    # event
    event_start_date = models.DateTimeField( null=True, blank=True)
    event_end_date = models.DateTimeField(null=True, blank=True)

    # advert
    url_field = models.URLField(max_length=255, null=True, blank=True)

    event_category = models.CharField(
        max_length=5, choices=EVENT_CATEGORIES.choices, default=EVENT_CATEGORIES.OTHER, null=True, blank=True)

    place_category = models.CharField(
        max_length=5, choices=PLACE_CATEGORIES.choices, default=PLACE_CATEGORIES.OTHER, null=True, blank=True)

    sale_category = models.CharField(
        max_length=5, choices=SALE_CATEGORIES.choices, default=SALE_CATEGORIES.OTHER, null=True, blank=True)

    job_category = models.CharField(max_length=5, choices=JOB_CATEGORIES.choices,
                                    default=JOB_CATEGORIES.NON_TEACHING, null=True, blank=True)

    job_type = models.CharField(max_length=5, choices=JOB_TYPE.choices,
                                default=JOB_TYPE.FULL_TIME, null=True, blank=True)

    featured_image = models.ImageField(
        upload_to=upload_location, null=True, blank=True)

    extra_image_one = models.ImageField(
        upload_to=upload_location,  null=True, blank=True)
    extra_image_two = models.ImageField(
        upload_to=upload_location,  null=True, blank=True)
    extra_image_three = models.ImageField(
        upload_to=upload_location,  null=True, blank=True)
    extra_image_four = models.ImageField(
        upload_to=upload_location,  null=True, blank=True)
    extra_image_five = models.ImageField(
        upload_to=upload_location, null=True, blank=True)
    extra_image_six = models.ImageField(
        upload_to=upload_location, null=True, blank=True)
    extra_image_seven = models.ImageField(
        upload_to=upload_location, null=True, blank=True)
    extra_image_eight = models.ImageField(
        upload_to=upload_location, null=True, blank=True)
    extra_image_nine = models.ImageField(
        upload_to=upload_location, null=True, blank=True)

    # all
    tags = models.TextField(max_length=255, null=True, blank=True)
    is_featured = models.BooleanField(default=False, null=False, blank=False)
    is_approved = models.BooleanField(default=False, null=False, blank=False)

    date_published = models.DateTimeField(
        auto_now_add=True, verbose_name="date published")

    date_updated = models.DateTimeField(
        auto_now=True, verbose_name="date updated")

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    slug = models.SlugField(blank=True, unique=True)

    views = models.IntegerField(default=0)

    likes = models.ManyToManyField(
        Account, related_name='jade_island_post_post_likes')

    dislikes = models.ManyToManyField(
        Account, related_name='jade_island_post_post_dislikes')

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    def get_absolute_url(self):
        return reverse('post_details', kwargs={'slug': self.slug})


@receiver(post_delete, sender=JadeIslandPost)
def submission_delete(sender, instance, **kwargs):
    try:
        if instance.featured_image:
            instance.featured_image.delete(False)
        if instance.extra_image_one:
            instance.extra_image_one.delete(False)
        if instance.extra_image_two:
            instance.extra_image_two.delete(False)
        if instance.extra_image_three:
            instance.extra_image_three.delete(False)
        if instance.extra_image_four:
            instance.extra_image_four.delete(False)
        if instance.extra_image_five:
            instance.extra_image_five.delete(False)
        if instance.extra_image_six:
            instance.extra_image_six.delete(False)
        if instance.extra_image_seven:
            instance.extra_image_seven.delete(False)
        if instance.extra_image_eight:
            instance.extra_image_eight.delete(False)
        if instance.extra_image_nine:
            instance.extra_image_nine.delete(False)
    except Exception as err:
        msg = "jade_island_post submission_delete threw exception " + str(err)
        saveAnalytics(request=None, log_key="Exception Thrown",
                      log_value=msg, log_type='E', resolved=False)


def compress_image(image):
    im = Image.open(image)
    out = BytesIO()
    if im.mode in ("RGBA", "P"):
        im = im.convert("RGB")
    im.save(out, 'JPEG', quality=30)
    compressed = File(out, name=image.name)
    im.close()
    return compressed


def pre_save_jade_island_post_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(
            instance.author.display_name + "-" + instance.title[0:48])
    try:
        post_obj = JadeIslandPost.objects.get(pk=instance.pk)

        # the object exists, so check if the image field is updated
        # the object exists, so check if the image field is updated
        if post_obj.featured_image != instance.featured_image:
            instance.featured_image = compress_image(instance.featured_image)

        if post_obj.extra_image_one != instance.extra_image_one:
            instance.extra_image_one = compress_image(instance.extra_image_one)

        if post_obj.extra_image_two != instance.extra_image_two:
            instance.extra_image_two = compress_image(instance.extra_image_two)

        if post_obj.extra_image_three != instance.extra_image_three:
            instance.extra_image_three = compress_image(
                instance.extra_image_three)

        if post_obj.extra_image_four != instance.extra_image_four:
            instance.extra_image_four = compress_image(
                instance.extra_image_four)

        if post_obj.extra_image_five != instance.extra_image_five:
            instance.extra_image_five = compress_image(
                instance.extra_image_five)

        if post_obj.extra_image_six != instance.extra_image_six:
            instance.extra_image_six = compress_image(instance.extra_image_six)

        if post_obj.extra_image_seven != instance.extra_image_seven:
            instance.extra_image_seven = compress_image(
                instance.extra_image_seven)

        if post_obj.extra_image_eight != instance.extra_image_eight:
            instance.extra_image_eight = compress_image(
                instance.extra_image_eight)

        if post_obj.extra_image_nine != instance.extra_image_nine:
            instance.extra_image_nine = compress_image(
                instance.extra_image_nine)

    except JadeIslandPost.DoesNotExist:
        # the object does not exists, so compress the image
        if instance.featured_image:
            instance.featured_image = compress_image(instance.featured_image)
        if instance.extra_image_one:
            instance.extra_image_one = compress_image(instance.extra_image_one)
        if instance.extra_image_two:
            instance.extra_image_two = compress_image(instance.extra_image_two)
        if instance.extra_image_three:
            instance.extra_image_three = compress_image(
                instance.extra_image_three)
        if instance.extra_image_four:
            instance.extra_image_four = compress_image(
                instance.extra_image_four)
        if instance.extra_image_five:
            instance.extra_image_five = compress_image(
                instance.extra_image_five)
        if instance.extra_image_six:
            instance.extra_image_six = compress_image(instance.extra_image_six)
        if instance.extra_image_seven:
            instance.extra_image_seven = compress_image(
                instance.extra_image_seven)
        if instance.extra_image_eight:
            instance.extra_image_eight = compress_image(
                instance.extra_image_eight)
        if instance.extra_image_nine:
            instance.extra_image_nine = compress_image(
                instance.extra_image_nine)


pre_save.connect(pre_save_jade_island_post_post_receiver,
                 sender=JadeIslandPost)


# comments-xtd
class CustomComment(XtdComment):
    def save(self, *args, **kwargs):
        if self.user:
            self.user_name = self.user.display_name
        super(CustomComment, self).save(*args, **kwargs)
