from django import forms
from .models import JadeIslandPost
from django.conf import settings



class CreateJadeIslandPostForm(forms.ModelForm):
    job_start_date = forms.DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS, required=False)
    event_start_date = forms.DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS, required=False)
    event_end_date = forms.DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS, required=False)
    class Meta:
        model = JadeIslandPost
        fields = ['title', 'body', 'post_category', 'location', 'contact', 'job_start_date', 'sale_item_price_rmb', 'event_start_date', 'event_end_date', 'url_field', 'event_category', 'place_category', 'sale_category', 'job_category', 'job_type',
                  'featured_image', 'extra_image_one', 'extra_image_two', 'extra_image_three', 'extra_image_four', 'extra_image_five', 'extra_image_six', 'extra_image_seven', 'extra_image_eight', 'extra_image_nine', 'tags', 'is_featured', 'is_approved']


class UpdateJadeIslandPostForm(forms.ModelForm):
    job_start_date = forms.DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS, required=False)
    event_start_date = forms.DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS, required=False)
    event_end_date = forms.DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS, required=False)
    class Meta:
        model = JadeIslandPost
        fields = ['title', 'body', 'post_category', 'location', 'contact', 'job_start_date', 'sale_item_price_rmb', 'event_start_date', 'event_end_date', 'url_field', 'event_category', 'place_category', 'sale_category', 'job_category', 'job_type',
                  'featured_image', 'extra_image_one', 'extra_image_two', 'extra_image_three', 'extra_image_four', 'extra_image_five', 'extra_image_six', 'extra_image_seven', 'extra_image_eight', 'extra_image_nine', 'tags', 'is_featured', 'is_approved']

    def save(self, commit=True):
        # override save so that only these fields are updated
        jade_island_post = self.instance
        jade_island_post.title = self.cleaned_data['title']
        jade_island_post.body = self.cleaned_data['body']
        jade_island_post.post_category = self.cleaned_data['post_category']
        jade_island_post.location = self.cleaned_data['location']
        jade_island_post.contact = self.cleaned_data['contact']
        jade_island_post.job_start_date = self.cleaned_data['job_start_date']
        jade_island_post.sale_item_price_rmb = self.cleaned_data['sale_item_price_rmb']
        jade_island_post.event_start_date = self.cleaned_data['event_start_date']
        jade_island_post.event_end_date = self.cleaned_data['event_end_date']
        jade_island_post.url_field = self.cleaned_data['url_field']
        jade_island_post.event_category = self.cleaned_data['event_category']
        jade_island_post.place_category = self.cleaned_data['place_category']
        jade_island_post.sale_category = self.cleaned_data['sale_category']
        jade_island_post.job_category = self.cleaned_data['job_category']
        jade_island_post.job_type = self.cleaned_data['job_type']
        jade_island_post.tags = self.cleaned_data['tags']
        jade_island_post.is_featured = self.cleaned_data['is_featured']
        jade_island_post.is_approved = self.cleaned_data['is_approved']

        # update image is a new one has been provided
        if self.cleaned_data['featured_image']:
            jade_island_post.featured_image = self.cleaned_data['featured_image'] 
        if self.cleaned_data['extra_image_one']:
            jade_island_post.extra_image_one = self.cleaned_data['extra_image_one']
        if self.cleaned_data['extra_image_two']:
            jade_island_post.extra_image_two = self.cleaned_data['extra_image_two'] 
        if self.cleaned_data['extra_image_three']:
            jade_island_post.extra_image_three = self.cleaned_data['extra_image_three'] 
        if self.cleaned_data['extra_image_four']:
            jade_island_post.extra_image_four = self.cleaned_data['extra_image_four'] 
        if self.cleaned_data['extra_image_five']:
            jade_island_post.extra_image_five = self.cleaned_data['extra_image_five']
        if self.cleaned_data['extra_image_six']:
            jade_island_post.extra_image_six = self.cleaned_data['extra_image_six']
        if self.cleaned_data['extra_image_seven']:
            jade_island_post.extra_image_seven = self.cleaned_data['extra_image_seven']
        if self.cleaned_data['extra_image_eight']:
            jade_island_post.extra_image_eight = self.cleaned_data['extra_image_eight']
        if self.cleaned_data['extra_image_nine']:
            jade_island_post.extra_image_nine = self.cleaned_data['extra_image_nine']

        if commit:
            jade_island_post.save()

        return jade_island_post
