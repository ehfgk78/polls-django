from django.shortcuts import render, get_object_or_404, redirect
from .models import 선택틀, 질문틀
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/첫페이지.html'
    context_object_name = '최근질문들'

    def get_queryset(self):
        return 질문틀.objects.order_by('-질문날짜')[:7]


class DetailView(generic.DetailView):
    model = 질문틀
    template_name = 'polls/개별투표.html'

class ResultsView(generic.DetailView):
    model = 질문틀
    template_name = 'polls/투표결과.html'


def 집계(request, 질문번호):
    choice = get_object_or_404(질문틀, pk = 질문번호)
    try:
        선택항목 = choice.선택틀_set.get(pk = request.POST['항목'])
    except:
        context = {"선택": choice, "에러발생": "투표하고 가세요~ "}
        return render(request, "polls/개별투표.html", context)
    else:
        선택항목.투표수 += 1
        선택항목.save()
        print("질문번호=", 질문번호)
        return redirect('polls:결과', pk=질문번호 )
