from django import template
from posts.models import Post, GroupMember, Group

register = template.Library()


# @register.simple_tag(takes_context=True)
# @register.inclusion_tag("test_inclusion.html",takes_context=True)
# def jump_link(context):
#     # def jump_link(context):
#     return {"my_groups":[1,4,5,68,43]}

@register.simple_tag()
def get_all_group():
    return Group.objects.all()

@register.simple_tag(takes_context=True)
def get_your_group(context):
    return GroupMember.objects.filter(user=context['user'])

