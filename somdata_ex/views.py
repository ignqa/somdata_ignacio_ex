from django.template import loader
from django.http import HttpResponse
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

from somdata_ex.models import BTCUSDT


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


class LineChartJSONView(BaseLineChartView):

    _LAST_N_VALUES = 40

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = BTCUSDT.objects.order_by('updated_at')  # Last values

    def get_labels(self):
        return [str(d.updated_at.strftime("%Y/%m/%d, %H:%M")) for d in self.data][-self._LAST_N_VALUES:]

    def get_providers(self):
        return ["High", "Low"]

    def get_data(self):
        return [
            [str(d.high) for d in self.data][-self._LAST_N_VALUES:],  # High
            [str(d.low) for d in self.data][-self._LAST_N_VALUES:]  # Low
        ]


line_chart = TemplateView.as_view(template_name='index.html')
line_chart_json = LineChartJSONView.as_view()
