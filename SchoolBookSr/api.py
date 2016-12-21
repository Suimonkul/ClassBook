from tastypie.constants import ALL_WITH_RELATIONS
from tastypie.resources import ModelResource

from SchoolBookSr.models import Schedule, Student, New, Support


class NewsResource(ModelResource):
    class Meta:
        queryset = New.objects.order_by('-created_at')
        name = 'New'


class StudentResource(ModelResource):
    class Meta:
        queryset = Student.objects.order_by('grade')
        name = 'Student'
        filtering = {
            'name': ALL_WITH_RELATIONS
        }


class SupportResource(ModelResource):
    class Meta:
        queryset = Support.objects.order_by('-created_at')
        name = 'Support'


class ScheduleResource(ModelResource):
    class Meta:
        limit = 0
        queryset = Schedule.objects.order_by('grade', 'day_of')
        name = 'Schedule'
        filtering = {
            'grade': ALL_WITH_RELATIONS,
            'day_of': ALL_WITH_RELATIONS,
        }
