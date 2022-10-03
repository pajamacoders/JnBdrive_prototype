
# Create your views here.

from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Item, Buyer, SalesHistory, InspectionLog

class IndexView(generic.ListView):
    template_name = 'item_log/index.html'
    context_object_name = 'logs'

    def get_queryset(self):
        """Return the last five published questions."""
        return InspectionLog.objects.order_by('-inspection_date')[:10]

def brief_inspection_history(request, item_id):
    logs = InspectionLog.objects.filter(item_id=item_id)
    if logs.count()>0:
        inspection_logs ={'item_id':item_id,
        'logs':logs}
    else:
        raise Http404(f"시리얼:{item_id} 에 해당하는 부품은 검사 이력이 존재 하지 않습니다.")

    return render(request, 'item_log/briefInspectionView.html', inspection_logs)

def detailed_inspection_history(request, item_id, inspection_date):
    #logs = InspectionLog.objects.filter(item_id=item_id).filter(inspection_date=inspection_date)
    """
    동일한 검사일에 두개 이상의 검사 이력이 존재 할경우 어떻게 처리 할 것인지 요구사항 확인.
    """
    logs = get_object_or_404(InspectionLog, item_id=item_id, inspection_date=inspection_date)
    inspection_logs ={'item_id':item_id,
    'indepction_date': inspection_date,
    'logs':[logs] if not isinstance(logs, list) else logs}

    return render(request, 'item_log/detailedInspectionView.html', inspection_logs)

def saleshistory(request, item_id, buyer_id):
    return HttpResponse("You're voting on question %s." % question_id)